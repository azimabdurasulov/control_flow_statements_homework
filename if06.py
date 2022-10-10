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
    if a < 0:
        count0 += 1

    if b > 0:
        count1 += 1
    if b < 0:
        count0 += 1

    if c > 0:
        count1 += 1
    if c < 0:
        count0 += 1

    answer = ''
    if count0 < count1:
        answer = "there are a lot of positive numbers"
    else:
        answer = "there are a lot of negative numbers"


    return answer
    

print(main(1, 0, 6))