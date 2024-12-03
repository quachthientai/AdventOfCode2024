from typing import List

fileName = "./input.txt"

def isSafe(report: List[int]) -> bool:
   isIncreasing = report[0] < report[1]

   for index, num in enumerate(report):
      if index == 0:
         continue

      diff = max(report[index - 1], num) - min(report[index - 1], num)
      if isIncreasing != (report[index-1] < report[index]) or diff <= 0 or diff > 3:
         return False

   return True


with open(fileName) as file:
   count = 0
   for line in file:
      line = [int(x) for x in line.split()]
      count += 1 if isSafe(line) == True else 0
   
   print(count)
