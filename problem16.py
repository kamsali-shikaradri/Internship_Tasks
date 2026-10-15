# Problem 16: Nested Lists
# https://www.hackerrank.com/challenges/nested-list/problem

students = []

for _ in range(int(input())):
    name = input().strip()
    score = float(input())
    students.append([name, score])

scores = sorted(set(score for name, score in students))
second_lowest = scores[1]

names = sorted(
    name for name, score in students
    if score == second_lowest
)

for name in names:
    print(name)