import argparse
import re
from pathlib import Path


def convert_assertequal(line):
    match = re.match(
        "(\s+)self\.assertEqual\(([^\,]+)\, ([^\,]+)\)(\s+)",
        line,
    )
    if not match:
        return line

    indentation, expected_value, variable, termination = match.groups()
    return f"{indentation}assert {variable} == {expected_value}{termination}"


def convert_assertalmostequal(line):
    match = re.match(
        "(\s+)self\.assertAlmostEqual\(([^\,]+)\, ([^\,]+)\, ([^\,])\)(\s+)",
        line,
    )
    if not match:
        return line

    indentation, expected_value, variable, precision, termination = match.groups()
    return f"{indentation}assert {variable} == pytest.approx({expected_value}, abs=1e-{precision}){termination}"


def convert_assertin(line):
    match = re.match(
        "(\s+)self\.assertIn\(([^\,]+)\, ([^\,]+)\)(\s+)",
        line,
    )
    if not match:
        return line

    indentation, expected_value, variable, termination = match.groups()
    return f"{indentation}assert {expected_value} in {variable}{termination}"


def convert_assertisnone(line):
    match = re.match(
        "(\s+)self\.assertIsNone\(([^\,]+)\)(\s+)",
        line,
    )
    if not match:
        return line

    indentation, variable, termination = match.groups()
    return f"{indentation}assert {variable} is None{termination}"


def convert(filepath, dry=False):
    # Read
    with open(filepath, "r") as fp:
        lines = fp.readlines()

    # Convert
    outlines = []
    for lineno, line in enumerate(lines, 1):
        newline = convert_assertequal(line)
        newline = convert_assertalmostequal(newline)
        newline = convert_assertin(newline)
        newline = convert_assertisnone(newline)

        if newline != line:
            print(f"{lineno}: {line.strip()} -> {newline.strip()}")

        outlines.append(newline)

    # Write back
    if dry:
        return

    with open(filepath, "w") as fp:
        fp.writelines(outlines)


def main():
    parser = argparse.ArgumentParser(description="Convert unittest assertion to pytest")

    parser.add_argument("--dry", action="store_true", help="Dry run")
    parser.add_argument("filepath", nargs="+", type=Path, help="File to convert")

    args = parser.parse_args()

    for filepath in args.filepath:
        convert(filepath, args.dry)


if __name__ == "__main__":
    main()
