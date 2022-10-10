def main(a,b,c):
    """
    Find how many positive numbers there are in the given numbers.
    Args:
        a: integer
        b: integer
        c: integer
    returns:
        integer: the number of positive numbers in the given numbers
    """
    count0 = 0

    if a > 0:
        count0 += 1
   
    if b > 0:
        count0 += 1

    if c > 0:
        count0 += 1

    return count0

print(main(43, 45, -65))