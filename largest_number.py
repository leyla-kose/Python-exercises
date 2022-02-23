def largest_number():
  try:
    numbers = []
    num = int(input("Enter the 1st of 5 numbers: "))
    numbers.append(num)
    for i in range(4):
      number = int(input("Enter another number: "))
      if number > numbers[0]:
        numbers.insert(0, number)
      else:
        numbers.append(number)
    return numbers[0]
  except: 
    print("Invalid input, try again!")

largest_number()

'''
Coding Challenge 003 : Find the Largest Number

Purpose of the this coding challenge is to solve a simple sorting problem in Python.

## Learning Outcomes

At the end of the this coding challenge, students will be able to;

- get a basic understanding of sorting algorithms.
- demonstrate their knowledge of lists in python
- implement loops to solve the problems in python
- get a better understanding of computational thinking concepts

## Problem Statement
  
- Write a python code that finds the largest number among the 5 numbers given by the user as input.

- It is forbidden to use max() function.  

- Indicate which computational thinking concepts have you used.

- Example for user inputs and respective outputs

```text
Input            Output
------------     ------
1 2 3 4 5         5
67 85 19 39       85
```

'''