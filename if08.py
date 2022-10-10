def main(a):
    """
    Given an integer a, check the following conditions:
    "two-digit odd number",
    "two-digit even number",
    "three-digit odd number",
    "three-digit even number"

    Args:
        a: integer
    Returns:
        string: the message to print
    """
    if a % 2 == 1 and a >= 10 and a <= 99:
        answer = "two-digit odd number"

    if a % 2 == 0 and a >= 10 and a <= 99:
        answer = "two-digit even number"

    if a % 2 == 1 and a >= 100 and a <= 999:
        answer = "three-digit odd number"

    if a % 2 == 0 and a >= 100 and a <= 999:
       answer = "three-digit even number"

    return answer

print(main(348))