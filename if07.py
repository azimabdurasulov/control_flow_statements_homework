def main(a):
    """
    Given an integer a, check the following conditions:
    "positive odd number",
    "positive even number",
    "negative odd number",
    "negative even number",
    "the number is zero"

    Args:
        a: integer
    Returns:
        string: the message to print
    """
    if a % 2 == 1 and a > 0:
        print("positive odd number", a)
    
    if a % 2 == 0 and a > 0:
        print("positive even number", a)

    if a % 2 == 1 and a < 0:
        print("negative odd number", a)

    if a % 2 == 0 and a < 0:
        print("negative even number", a)


    if a == 0: 
        print("the number is zero", a)
    return a

print(main(44))