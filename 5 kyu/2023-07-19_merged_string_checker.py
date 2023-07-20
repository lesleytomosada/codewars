# At a job interview, you are challenged to write an algorithm to check if a
# given string, s, can be formed from two other strings, part1 and part2.

# The restriction is that the characters in part1 and part2 should be in the
# same order as in s.

# The interviewer gives you the following example and tells you to figure out
# the rest from the given test cases.

# For example:

# 'codewars' is a merge from 'cdw' and 'oears':

#     s:  c o d e w a r s   = codewars
# part1:  c   d   w         = cdw
# part2:    o   e   a r s   = oears


def solution(s, part1, part2):
    if sorted(s) != sorted(part1 + part2):
        return False
    s1 = s2 = ""
    for i in s:
        if part1 and part1[0] == i:
            s1 += i
            part1 = part1[1:]
        if part2 and part2[0] == i:
            s2 += i
            part2 = part2[1:]
    return sorted(s1 + s2) == sorted(s)
