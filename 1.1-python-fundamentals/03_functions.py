"""
Task 1.1 - Python Fundamentals
Topic: Functions (args, kwargs, defaults, recursion, higher-order)
"""


def exercise_1_default_and_keyword_args(name, greeting="Hello", punctuation="!"):
    """Function with default parameters."""
    return f"{greeting}, {name}{punctuation}"


def exercise_2_variable_args(*args, **kwargs):
    """Function accepting *args and **kwargs."""
    total = sum(args)
    details = ", ".join(f"{k}={v}" for k, v in kwargs.items())
    return {"sum_of_args": total, "kwargs": details}


def exercise_3_recursive_factorial(n):
    """Recursive factorial."""
    if n < 0:
        raise ValueError("factorial undefined for negative numbers")
    if n in (0, 1):
        return 1
    return n * exercise_3_recursive_factorial(n - 1)


def exercise_4_higher_order_function(numbers, operation):
    """Accept a function as an argument (higher-order function)."""
    return [operation(n) for n in numbers]


def exercise_5_closures_counter():
    """Return a closure that maintains state between calls."""
    count = 0

    def counter():
        nonlocal count
        count += 1
        return count

    return counter


if __name__ == "__main__":
    print("Exercise 1 - default args:", exercise_1_default_and_keyword_args("Mahdi"))
    print("Exercise 2 - *args/**kwargs:", exercise_2_variable_args(1, 2, 3, city="Baghdad", track="AI/ML"))
    print("Exercise 3 - factorial(6):", exercise_3_recursive_factorial(6))
    print("Exercise 4 - higher-order (square):", exercise_4_higher_order_function([1, 2, 3, 4], lambda x: x ** 2))

    counter = exercise_5_closures_counter()
    print("Exercise 5 - closure counter calls:", counter(), counter(), counter())
