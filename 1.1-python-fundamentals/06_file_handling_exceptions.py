"""
Task 1.1 - Python Fundamentals
Topic: File Handling & Exceptions
"""

import os
import json


DATA_DIR = os.path.join(os.path.dirname(__file__), "sample_data")


def exercise_1_write_and_read_text_file():
    """Write lines to a text file, then read them back."""
    os.makedirs(DATA_DIR, exist_ok=True)
    path = os.path.join(DATA_DIR, "notes.txt")

    with open(path, "w") as f:
        f.write("Week 1 - Python Fundamentals\n")
        f.write("Skill Set Go EduTech AI/ML Internship\n")

    with open(path, "r") as f:
        lines = f.readlines()

    return [line.strip() for line in lines]


def exercise_2_json_read_write():
    """Write a dictionary to a JSON file and read it back."""
    path = os.path.join(DATA_DIR, "profile.json")
    data = {"intern": "Mahdi Ahmed Fouad", "track": "AI/ML", "week": 1}

    with open(path, "w") as f:
        json.dump(data, f, indent=2)

    with open(path, "r") as f:
        loaded = json.load(f)

    return loaded


def exercise_3_handle_missing_file():
    """Gracefully handle a FileNotFoundError."""
    try:
        with open(os.path.join(DATA_DIR, "does_not_exist.txt"), "r") as f:
            f.read()
    except FileNotFoundError as e:
        return f"Caught expected error: {e.__class__.__name__}"
    return "No error raised (unexpected)"


def exercise_4_custom_exception():
    """Define and raise a custom exception."""

    class NegativeValueError(Exception):
        """Raised when a value that must be non-negative is negative."""

    def check_battery(level):
        if level < 0:
            raise NegativeValueError(f"Battery level cannot be negative, got {level}")
        return f"Battery level OK: {level}%"

    try:
        check_battery(-5)
    except NegativeValueError as e:
        return f"Caught custom exception: {e}"


def exercise_5_multiple_except_and_finally():
    """Demonstrate multiple except blocks plus a finally clause."""
    results = []
    for value in ["10", "abc", "0"]:
        try:
            result = 100 / int(value)
            results.append(f"100 / {value} = {result}")
        except ZeroDivisionError:
            results.append(f"{value}: division by zero")
        except ValueError:
            results.append(f"{value}: not a valid integer")
        finally:
            results.append(f"-- finished attempt for input '{value}' --")
    return results


if __name__ == "__main__":
    print("Exercise 1 - text file:", exercise_1_write_and_read_text_file())
    print("Exercise 2 - JSON file:", exercise_2_json_read_write())
    print("Exercise 3 - missing file:", exercise_3_handle_missing_file())
    print("Exercise 4 - custom exception:", exercise_4_custom_exception())
    print("Exercise 5 - multiple except/finally:")
    for line in exercise_5_multiple_except_and_finally():
        print(" ", line)
