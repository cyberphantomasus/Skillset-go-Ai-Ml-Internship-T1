"""
Task 1.1 - Python Fundamentals
Topic: Variables & Data Types
"""


def exercise_1_variable_swap():
    """Swap two variables without a temp variable."""
    a, b = 5, 10
    a, b = b, a
    return a, b


def exercise_2_type_conversion():
    """Convert between int, float, str and show the results."""
    num_str = "42"
    as_int = int(num_str)
    as_float = float(num_str)
    back_to_str = str(as_int + 8)
    return {
        "original": num_str,
        "as_int": as_int,
        "as_float": as_float,
        "back_to_str": back_to_str,
        "types": (type(num_str).__name__, type(as_int).__name__, type(as_float).__name__),
    }


def exercise_3_multiple_assignment():
    """Assign three variables in one line and compute their average."""
    x, y, z = 12, 8, 20
    average = (x + y + z) / 3
    return x, y, z, average


def exercise_4_string_formatting():
    """Build a formatted string using an f-string with variables of different types."""
    name = "Mahdi"
    age = 19
    gpa = 3.7
    return f"{name} is {age} years old with a GPA of {gpa:.2f}"


def exercise_5_constants_and_scope():
    """Demonstrate a module-level constant vs a local variable shadowing it."""
    PI = 3.14159  # noqa: N806  (constant-style naming intentional)

    def circle_area(radius):
        return PI * radius ** 2

    return circle_area(3)


if __name__ == "__main__":
    print("Exercise 1 - swap:", exercise_1_variable_swap())
    print("Exercise 2 - conversion:", exercise_2_type_conversion())
    print("Exercise 3 - multiple assignment:", exercise_3_multiple_assignment())
    print("Exercise 4 - formatting:", exercise_4_string_formatting())
    print("Exercise 5 - constants:", exercise_5_constants_and_scope())
