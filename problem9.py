# Problem 9: Mutations
# https://www.hackerrank.com/challenges/python-mutations/problem

s = input()
i, c = input().split()
i = int(i)

s = s[:i] + c + s[i + 1:]
print(s)