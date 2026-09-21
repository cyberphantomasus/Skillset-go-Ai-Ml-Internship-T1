"""
Task 1.1 - Python Fundamentals
Topic: Loops (for, while, nested, comprehensions)
"""


def exercise_1_fizzbuzz(n=20):
    """Classic FizzBuzz using a for loop."""
    result = []
    for i in range(1, n + 1):
        if i % 15 == 0:
            result.append("FizzBuzz")
        elif i % 3 == 0:
            result.append("Fizz")
        elif i % 5 == 0:
            result.append("Buzz")
        else:
            result.append(str(i))
    return result


def exercise_2_sum_with_while(target=100):
    """Sum numbers 1..n using a while loop until the sum exceeds target."""
    total = 0
    n = 0
    while total <= target:
        n += 1
        total += n
    return n, total


def exercise_3_nested_loop_pattern(rows=5):
    """Print a right-angled triangle pattern using nested loops."""
    lines = []
    for i in range(1, rows + 1):
        lines.append("*" * i)
    return lines


def exercise_4_list_comprehension_squares(n=10):
    """Generate squares of even numbers from 0..n using a list comprehension."""
    return [x ** 2 for x in range(n + 1) if x % 2 == 0]


def exercise_5_break_continue(numbers):
    """Skip negative numbers, stop entirely once a number > 100 is seen."""
    kept = []
    for num in numbers:
        if num < 0:
            continue
        if num > 100:
            break
        kept.append(num)
    return kept


if __name__ == "__main__":
    print("Exercise 1 - FizzBuzz:", exercise_1_fizzbuzz(15))
    print("Exercise 2 - sum until >100:", exercise_2_sum_with_while())
    print("Exercise 3 - triangle:")
    for line in exercise_3_nested_loop_pattern():
        print(" ", line)
    print("Exercise 4 - even squares:", exercise_4_list_comprehension_squares())
    print("Exercise 5 - break/continue:", exercise_5_break_continue([5, -3, 20, 150, 40, -1]))
