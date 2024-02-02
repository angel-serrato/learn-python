"""
Dictionaries
It has two parts
Key => Value
Word => Definition
    {Key: Value}
    {
    "Bug": "An error in a program",
    "key": "value",
    "key": "value",
    "key": "value"
    }
"""
programming_dictionary = {
    "Bug": "An error",
    "Function": "A piece of code",
    "Loop": "Doing something multiple times",
}

# retieving items from a dictionary
print(programming_dictionary["Bug"])

# Adding a new entry to a dictionary
programming_dictionary["Angel"] = "Developer"
print(programming_dictionary)

# Create a dictionary
empty = {}

# Wipe a existing dictionary
programming_dictionary = {}

# Edit an item in a dictionary
programming_dictionary["Angel"] = "Colombiano"

# Loop through a dictionary
# This code only gives you the key
for thing in programming_dictionary:
    print(thing)

# print the value
for key in programming_dictionary:
    print(programming_dictionary[key])

"""
Grading program from auditorium
"""

student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
# TODO-1: Create an empty dictionary called student_grades.
student_grades = {}
# TODO-2: Write your code below to add the grades to student_grades.👇
for thing in student_scores:
  if student_scores[thing] >= 91 and student_scores[thing] < 100:
    student_grades[thing] = "Outstanding"
  elif student_scores[thing] >= 81 and student_scores[thing] <= 90:
    student_grades[thing] = "Exceeds Expectations"
  elif student_scores[thing] >= 71 and student_scores[thing] <= 80:
    student_grades[thing] = "Acceptable"
  else:
    student_grades[thing] = "Fail"
print(student_grades)