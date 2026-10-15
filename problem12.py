# Problem 12: Introduction to Sets
# https://www.hackerrank.com/challenges/py-introduction-to-sets/problem

def average(array):
    distinct_heights = set(array)
    return sum(distinct_heights) / len(distinct_heights)

n = int(input())
arr = list(map(int, input().split()))
print(average(arr))