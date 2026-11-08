#!/usr/bin/env python3
"""Self-check for the loop practicum. Python 3.8+, standard library only.

Run from the repository root:
    python selfcheck.py --digit 7              check everything
    python selfcheck.py --digit 7 --target 2   check the case study up to target 2
    python selfcheck.py --task t14             check one task
    python selfcheck.py --lang en              show messages in English

The result helps you find mistakes. It is not your final grade.
"""
import argparse
import ast
import os
import subprocess
import sys
import tempfile
import threading

TIMEOUT_SECONDS = 3
MAX_OUTPUT_BYTES = 200000

RUNNER = """
import builtins, runpy, sys
_input = builtins.input
builtins.input = lambda prompt="": _input()
runpy.run_path(sys.argv[1], run_name="__main__")
"""

TEXT = {
    "id": {
        "title": "SELF-CHECK PRAKTIKUM PERULANGAN",
        "note": "Hasil ini membantu menemukan kesalahan, bukan nilai akhir.",
        "ask_digit": "Masukkan digit terakhir NIM: ",
        "bad_digit": "Digit harus berupa satu angka dari 0 sampai 9.",
        "variant": "Varian: PASS_SCORE = {score}, keluaran akhir = {label}",
        "pass": "LULUS", "fail": "GAGAL", "missing": "BELUM ADA", "skip": "DILEWATI",
        "input": "Input", "expected": "Diharapkan", "actual": "Hasil Anda",
        "timeout": "Program tidak berhenti. Periksa kondisi dan update loop.",
        "flood": "Output terlalu banyak, kemungkinan infinite loop.",
        "eof": "Program meminta input lebih banyak daripada yang seharusnya.",
        "error": "Program berhenti karena error: {detail}",
        "syntax": "Syntax error pada baris {line}.",
        "need": "Kode perlu memakai: {items}",
        "forbidden": "Batasan modul: jangan memakai {items}",
        "constant": "Tulis konstanta {name} = {value} di awal kode.",
        "count": "'{line}' harus tampil {want} kali, tetapi tampil {got} kali.",
        "summary": "Ringkasan: {ok} lulus, {bad} gagal, {none} belum ada, {skip} opsional dilewati.",
        "unknown": "Tugas tidak dikenal: {task}",
    },
    "en": {
        "title": "LOOP PRACTICUM SELF-CHECK",
        "note": "This result helps you find mistakes. It is not your final grade.",
        "ask_digit": "Enter the last digit of your student ID: ",
        "bad_digit": "The digit must be a single number from 0 to 9.",
        "variant": "Variant: PASS_SCORE = {score}, final output = {label}",
        "pass": "PASS", "fail": "FAIL", "missing": "MISSING", "skip": "SKIPPED",
        "input": "Input", "expected": "Expected", "actual": "Your output",
        "timeout": "The program did not stop. Check the loop condition and update.",
        "flood": "Too much output, probably an infinite loop.",
        "eof": "The program asked for more input than it should.",
        "error": "The program stopped with an error: {detail}",
        "syntax": "Syntax error on line {line}.",
        "need": "The code must use: {items}",
        "forbidden": "Module restriction, do not use: {items}",
        "constant": "Write the constant {name} = {value} at the top of the code.",
        "count": "'{line}' must appear {want} time(s), but appeared {got} time(s).",
        "summary": "Summary: {ok} passed, {bad} failed, {none} missing, {skip} optional skipped.",
        "unknown": "Unknown task: {task}",
    },
}


def case(stdin, lines, exact=True, counts=None):
    return {"stdin": stdin, "lines": lines, "exact": exact, "counts": counts or {}}


def table(number):
    return [f"{number} x {i} = {number * i}" for i in range(1, 11)]


TASKS = [
    {"id": "t13", "file": "blok1/t13_countdown.py", "need": ["while"],
     "cases": [case([], ["5", "4", "3", "2", "1", "Go!"])]},
    {"id": "t14", "file": "blok1/t14_pin.py", "need": ["while"],
     "cases": [
         case(["1234"], ["Access granted"]),
         case(["1", "2", "1234"], ["Incorrect PIN.", "Incorrect PIN.", "Access granted"]),
         case(["1", "2", "3"], ["Incorrect PIN.", "Incorrect PIN.", "Account locked"]),
     ]},
    {"id": "t15", "file": "blok1/t15_saving.py", "need": ["while"], "optional": True,
     "cases": [case(["300000", "1000000"], ["Months needed: 4", "Final balance: 1200000"])]},
    {"id": "t24", "file": "blok2/t24_multiplication.py", "need": ["for", "range"],
     "cases": [case(["7"], table(7)), case(["3"], table(3))]},
    {"id": "t26", "file": "blok2/t26_sum_multiples.py", "need": ["for"], "optional": True,
     "cases": [case(["10"], ["Total: 18"]), case(["3"], ["Total: 3"]), case(["2"], ["Total: 0"])]},
    {"id": "t34", "file": "blok3/t34_rectangle.py", "need": ["nested"],
     "cases": [case([], ["* * * *"] * 3)]},
    {"id": "t35", "file": "blok3/t35_number_triangle.py", "need": ["nested"],
     "cases": [case(["4"], ["1", "1 2", "1 2 3", "1 2 3 4"]), case(["1"], ["1"])]},
    {"id": "t36", "file": "blok3/t36_inverted_triangle.py", "need": ["nested"],
     "cases": [case(["4"], ["* * * *", "* * *", "* *", "*"]), case(["1"], ["*"])]},
    {"id": "t37", "file": "blok3/t37_table.py", "need": ["nested"], "optional": True,
     "cases": [case([], [" ".join(str(r * c) for c in range(1, 6)) for r in range(1, 6)])]},
    {"id": "t43", "file": "blok4/t43_odd_numbers.py", "need": ["while", "continue"],
     "cases": [case([], ["1", "3", "5"])]},
    {"id": "t44", "file": "blok4/t44_seats.py", "need": ["nested", "break"],
     "cases": [
         case(["3"], ["Row 1: 1 2", "Row 2: 1 2", "Row 3: 1 2"]),
         case(["1"], ["Row 1:", "Row 2:", "Row 3:"]),
         case(["6"], ["Row 1: 1 2 3 4 5", "Row 2: 1 2 3 4 5", "Row 3: 1 2 3 4 5"]),
     ]},
    {"id": "t45", "file": "blok4/t45_positive_total.py", "need": ["while", "break", "continue"],
     "cases": [
         case(["5", "0", "7", "-1"], ["Positive number: 5", "Positive number: 7", "Total: 12"]),
         case(["-1"], ["Total: 0"]),
     ]},
]


def variant_of(digit):
    if digit in (0, 3, 6, 9):
        return 60, "highest", "Highest score"
    if digit in (1, 4, 7):
        return 65, "lowest", "Lowest score"
    return 70, "excellent", "Excellent count"


def final_line(scores, mode):
    if mode == "highest":
        return f"Highest score: {max(scores)}"
    if mode == "lowest":
        return f"Lowest score: {min(scores)}"
    return f"Excellent count: {sum(1 for s in scores if s >= 85)}"


def recap_lines(scores, pass_score=None, mode=None):
    lines = [f"Total score: {sum(scores)}",
             f"Average score: {round(sum(scores) / len(scores), 2)}"]
    if pass_score is not None:
        lines.append(f"Passed: {sum(1 for s in scores if s >= pass_score)}")
    if mode is not None:
        lines.append(final_line(scores, mode))
    return lines


def recap_input(scores):
    return [str(len(scores))] + [str(s) for s in scores]


def case_study_cases(target, pass_score, mode):
    cases = []
    for scores in ([80, 70, 90], [100, 100, 99]):
        cases.append(case(recap_input(scores), recap_lines(scores), exact=False))
    if target >= 2:
        data = ["2", "101", "80", "-1", "-5", "70"]
        cases.append(case(data, recap_lines([80, 70]), exact=False,
                          counts={"Invalid score!": 3}))
        edge = ["2", "0", "100"]
        cases.append(case(edge, recap_lines([0, 100]), exact=False,
                          counts={"Invalid score!": 0}))
    if target >= 3:
        for scores in ([pass_score, pass_score - 1, 90], [10, 20], [100]):
            cases.append(case(recap_input(scores), recap_lines(scores, pass_score),
                              exact=False))
    if target >= 4:
        for scores in ([85, 60, 65, 70], [84, 40], [0, 100, 50], [100]):
            cases.append(case(recap_input(scores), recap_lines(scores, pass_score, mode),
                              exact=False))
        retry = ["0", "-2", "2", "90", "50"]
        cases.append(case(retry, recap_lines([90, 50], pass_score, mode), exact=False,
                          counts={"Invalid student count!": 2}))
    return cases


def normalize(text):
    result = []
    for line in text.splitlines():
        clean = " ".join(line.split())
        if clean:
            result.append(clean)
    return result


def run_program(path, stdin_lines, runner_path):
    stdin_text = "".join(line + "\n" for line in stdin_lines)
    env = dict(os.environ, PYTHONIOENCODING="utf-8", PYTHONUNBUFFERED="1")
    process = subprocess.Popen(
        [sys.executable, runner_path, os.path.abspath(path)],
        stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
        cwd=os.path.dirname(os.path.abspath(path)), env=env)
    state = {"timeout": False, "flood": False}

    def on_timeout():
        state["timeout"] = True
        process.kill()

    timer = threading.Timer(TIMEOUT_SECONDS, on_timeout)
    timer.start()
    chunks = []
    size = 0
    try:
        try:
            process.stdin.write(stdin_text.encode("utf-8"))
            process.stdin.close()
        except OSError:
            pass
        while True:
            chunk = process.stdout.read(8192)
            if not chunk:
                break
            size += len(chunk)
            if size > MAX_OUTPUT_BYTES:
                state["flood"] = True
                process.kill()
                break
            chunks.append(chunk)
    finally:
        timer.cancel()
        process.wait()
        process.stdout.close()
    output = b"".join(chunks).decode("utf-8", "replace")
    return output, process.returncode, state


def in_order(expected, actual):
    position = 0
    for line in actual:
        if position < len(expected) and line == expected[position]:
            position += 1
    return position == len(expected)


def describe_failure(output, code, state, t):
    if state["flood"]:
        return t["flood"]
    if state["timeout"]:
        return t["timeout"]
    if code != 0:
        if "EOFError" in output:
            return t["eof"]
        last = output.strip().splitlines()[-1] if output.strip() else str(code)
        return t["error"].format(detail=last)
    return None


def check_case(path, item, runner_path, t):
    output, code, state = run_program(path, item["stdin"], runner_path)
    problem = describe_failure(output, code, state, t)
    if problem:
        return [problem, f"{t['input']}: {item['stdin']}"]
    actual = normalize(output)
    matched = actual == item["lines"] if item["exact"] else in_order(item["lines"], actual)
    messages = []
    if not matched:
        messages += [f"{t['input']}: {item['stdin']}",
                     f"{t['expected']}: {item['lines']}",
                     f"{t['actual']}: {actual[:20]}"]
    for line, want in item["counts"].items():
        got = actual.count(line)
        if got != want:
            messages.append(t["count"].format(line=line, want=want, got=got))
    return messages


def inspect_code(tree):
    found = set()
    nested = False
    break_in_nested = False
    for node in ast.walk(tree):
        if isinstance(node, ast.While):
            found.add("while")
        elif isinstance(node, ast.For):
            found.add("for")
            for inner in ast.walk(node):
                if inner is not node and isinstance(inner, (ast.For, ast.While)):
                    nested = True
        elif isinstance(node, ast.Break):
            found.add("break")
        elif isinstance(node, ast.Continue):
            found.add("continue")
        elif isinstance(node, ast.Call) and isinstance(node.func, ast.Name):
            found.add(node.func.id)
    if nested:
        found.add("nested")
    forbidden = set()
    for node in ast.walk(tree):
        if isinstance(node, (ast.FunctionDef, ast.Lambda)):
            forbidden.add("def/lambda")
        elif isinstance(node, (ast.List, ast.ListComp)):
            forbidden.add("list")
        elif isinstance(node, ast.JoinedStr):
            forbidden.add("f-string")
        elif isinstance(node, ast.Try):
            forbidden.add("try-except")
        elif isinstance(node, (ast.Import, ast.ImportFrom)):
            forbidden.add("import")
    return found, sorted(forbidden)


def module_constant(tree, name):
    for node in tree.body:
        if isinstance(node, ast.Assign):
            for target in node.targets:
                if isinstance(target, ast.Name) and target.id == name:
                    if isinstance(node.value, ast.Constant):
                        return node.value.value
    return None


def check_task(task, runner_path, t):
    path = task["file"]
    if not os.path.isfile(path):
        return "skip" if task.get("optional") else "missing", []
    with open(path, encoding="utf-8") as source:
        code = source.read()
    try:
        tree = ast.parse(code)
    except SyntaxError as error:
        return "fail", [t["syntax"].format(line=error.lineno)]
    found, forbidden = inspect_code(tree)
    messages = []
    absent = [item for item in task["need"] if item not in found]
    if absent:
        messages.append(t["need"].format(items=", ".join(absent)))
    if forbidden:
        messages.append(t["forbidden"].format(items=", ".join(forbidden)))
    for name, value in task.get("constants", {}).items():
        if module_constant(tree, name) != value:
            messages.append(t["constant"].format(name=name, value=value))
    for item in task["cases"]:
        result = check_case(path, item, runner_path, t)
        if result:
            messages += result
            break
    return ("fail" if messages else "pass"), messages


def read_digit(args, t):
    if args.digit is not None:
        return args.digit
    answer = input(t["ask_digit"]).strip()
    return int(answer) if answer.isdigit() and len(answer) == 1 else -1


def main():
    parser = argparse.ArgumentParser(description="Self-check for the loop practicum")
    parser.add_argument("--digit", type=int, help="last digit of the student ID")
    parser.add_argument("--target", type=int, choices=[1, 2, 3, 4], default=4,
                        help="case study target to check up to")
    parser.add_argument("--task", help="one task ID, such as t14 or score")
    parser.add_argument("--lang", choices=["id", "en"], default="id")
    args = parser.parse_args()
    t = TEXT[args.lang]

    tasks = list(TASKS)
    known = [task["id"] for task in tasks] + ["score"]
    if args.task and args.task not in known:
        print(t["unknown"].format(task=args.task))
        return 2

    print(t["title"])
    print(t["note"])
    if args.task in (None, "score"):
        digit = read_digit(args, t)
        if not 0 <= digit <= 9:
            print(t["bad_digit"])
            return 2
        pass_score, mode, label = variant_of(digit)
        print(t["variant"].format(score=pass_score, label=label))
        need = ["for"] if args.target < 2 else ["for", "while"]
        if args.target >= 1:
            need.append("round")
        tasks.append({"id": "score", "file": "studi_kasus/score_recap.py", "need": need,
                      "constants": {"PASS_SCORE": pass_score} if args.target >= 3 else {},
                      "cases": case_study_cases(args.target, pass_score, mode)})
    if args.task:
        tasks = [task for task in tasks if task["id"] == args.task]
    print()

    totals = {"pass": 0, "fail": 0, "missing": 0, "skip": 0}
    with tempfile.TemporaryDirectory() as folder:
        runner_path = os.path.join(folder, "runner.py")
        with open(runner_path, "w", encoding="utf-8") as runner:
            runner.write(RUNNER)
        for task in tasks:
            status, messages = check_task(task, runner_path, t)
            totals[status] += 1
            print(f"[{t[status]}] {task['id']}  {task['file']}")
            for message in messages:
                print("    " + message)

    print()
    print(t["summary"].format(ok=totals["pass"], bad=totals["fail"],
                              none=totals["missing"], skip=totals["skip"]))
    return 0 if totals["fail"] == 0 and totals["missing"] == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
