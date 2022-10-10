def main(temp):
    """
    Display the message according to the following temperature conditions given to you in Celsius:
    Temp<0: "Freezing"
    Temp 1-10: "Very Cold"
    Temp 11-20: "Cold"
    Temp 21-30: "Normal"
    Temp 31-40: "Hot"
    Temp >40: "Very Hot"

    Args:
        temp: integer
    Returns:
        string: the message to print
    """
    if temp < 0:
        answer = "Freezing"

    if temp > 0 and temp < 10:
        answer = "Very Cold"

    if temp > 10 and temp < 20:
        answer = "Cold"

    if temp > 20 and temp < 30:
        answer = "Normal"

    if temp > 30 and temp < 40:
        answer = "Hot"
    if temp > 40:
        answer = "Very Hot"

    return answer

print(main(87))