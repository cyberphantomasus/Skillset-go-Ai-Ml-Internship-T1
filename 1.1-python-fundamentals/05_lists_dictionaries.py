"""
Task 1.1 - Python Fundamentals
Topic: Lists & Dictionaries
"""


def exercise_1_list_manipulation():
    """Append, remove, sort, and slice a list."""
    numbers = [5, 3, 8, 1, 9, 2]
    numbers.append(100)
    numbers.remove(3)
    sorted_numbers = sorted(numbers)
    first_three = sorted_numbers[:3]
    return {
        "after_append_remove": numbers,
        "sorted": sorted_numbers,
        "first_three": first_three,
    }


def exercise_2_dict_from_lists(keys, values):
    """Build a dictionary from two parallel lists using zip."""
    return dict(zip(keys, values))


def exercise_3_word_frequency(text):
    """Count word frequency in a string using a dictionary."""
    freq = {}
    for word in text.lower().split():
        word = word.strip(".,!?")
        freq[word] = freq.get(word, 0) + 1
    return freq


def exercise_4_nested_structures():
    """Work with a list of dictionaries (common real-world pattern)."""
    students = [
        {"name": "Ali", "grade": 88},
        {"name": "Sara", "grade": 95},
        {"name": "Omar", "grade": 72},
    ]
    top_student = max(students, key=lambda s: s["grade"])
    average_grade = sum(s["grade"] for s in students) / len(students)
    return top_student, round(average_grade, 2)


def exercise_5_dict_comprehension():
    """Build a dictionary comprehension mapping numbers to their cubes."""
    return {n: n ** 3 for n in range(1, 8)}


if __name__ == "__main__":
    print("Exercise 1 - list ops:", exercise_1_list_manipulation())
    print("Exercise 2 - dict from lists:", exercise_2_dict_from_lists(["a", "b", "c"], [1, 2, 3]))
    print("Exercise 3 - word frequency:", exercise_3_word_frequency("the quick fox the lazy fox the dog"))
    print("Exercise 4 - nested structures:", exercise_4_nested_structures())
    print("Exercise 5 - dict comprehension (cubes):", exercise_5_dict_comprehension())
