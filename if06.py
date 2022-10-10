def main(a,b,c):
    """
    Find how many positive and how many negative numbers there are in the given numbers.
    check the following conditions:
    "there are a lot of positive numbers",
    "there are a lot of negative numbers"

    Args:
        a: first number
        b: second number
        c: third number

    Returns:
        string: string with the result
    """
    count0 = 0 
    count1 = 0
     
    if a > 0:
        count1 += 1
    else:
        count0 += 1

    if b > 0:
        count1 += 1
    else:
        count0 += 1

    if c > 0:
        count1 += 1
    else:
        count0 += 1


    if count0 < count1:
        print("there are a lot of positive numbers")
    else:
        print("there are a lot of negative numbers")

    return count0, count1

print(main(32, 4, -76))