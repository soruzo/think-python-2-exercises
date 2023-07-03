# 1.1 in a print statement, what happens if you leave out one of the parentheses, or both?
# R: the compiler will return a syntax error

# 1.2 If you are trying to print a string, what happens if you leave out one of the quotation marks, or both?
# the compiler will return a syntax error

# 1.3 You can use a minus sign to make a negative number like -2. What happens if you put a plus sign before a
# number? What about 2++2?
# A: the compiler will reduce ++ to + and return 4

# 1.4 In math notation, leading zeros are ok, as in 02. What happens if you try this in Python?
# A: the compiler supports leading zeros

# 1.5 What happens if you have two values with no operator between them?
# A: the compiler will return a statement expected error

# 2.1 How many seconds are there in 42 minutes 42 seconds?
# A: 2545.2
def seconds_in_minutes(minutes):
    return minutes * 60


# 2.2 How many miles are there in 10 kilometers? Hint: there are 1.61 kilometers in a mile.
# A: 6.211180124223602
def kilometers_in_miles(kilometers):
    return kilometers / 1.61


# 2.3 If you run a 10 kilometer race in 42 minutes 42 seconds, what is your average pace (time per
# mile in minutes and seconds)? What is your average speed in miles per hour?
# A: 1591.3
def average_pace_in_minutes_per_mile(minutes, seconds):
    return (minutes * 60 + seconds) / 1.61


if __name__ == '__main__':
    print(seconds_in_minutes(42.42))
    print(kilometers_in_miles(10))
    print(average_pace_in_minutes_per_mile(42, 42))
