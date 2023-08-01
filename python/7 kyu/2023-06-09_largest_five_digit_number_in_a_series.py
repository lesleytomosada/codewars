# In the following 6 digit number:

# 283910
# 91 is the greatest sequence of 2 consecutive digits.

# In the following 10 digit number:

# 1234567890
# 67890 is the greatest sequence of 5 consecutive digits.

# Complete the solution so that it returns the greatest sequence of five
# consecutive digits found within the number given. The number will be passed
# in as a string of only digits. It should return a five digit integer. The
# number passed may be as large as 1000 digits.

def solution(digits):
    max_seq = int(digits[0:5])
    for i in range(1, len(digits)):
        if digits[i-1] <= digits[i]:
            seq = int(digits[i:i+5])
            max_seq = max(max_seq, seq)
    return max_seq


def solution2(digits):
    numlist = [int(digits[i:i+5]) for i in range(0, len(digits)-4)]
    return max(numlist)
