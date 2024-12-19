# Dictionaries and nesting
# Every dictionary has a key and a value
dictionary = {
    "Bug": "An error in a program that prevents the program form running as expected.",
    "Loop": "The action of doing something over and over again.",
}
# Printing an item
print(dictionary["Bug"])
print(dictionary)
# Adding an item
dictionary["Angel"] = "It's me."
print(dictionary)
# Wiping an entire dictionary
empty_dictionary = {}
# Edit an item
dictionary["Bug"] = "A moth in your computer."
print(dictionary)
# Loop through a dictionary
for key in dictionary:
    print(key)
    print(dictionary[key])
# You have access to a database of student_scores in the format of a dictionary. The keys in student_scores are the names of the students and the values are their exam scores.
# Write a program that converts their scores to grades.
# By the end of your program, you should have a new dictionary called student_grades that should contain student names as keys and their assessed grades for values.
# The final version of the student_grades dictionary will be checked.
# **DO NOT** modify lines 1-7 to change the existing student_scores dictionary.
# This is the scoring criteria:
# - Scores 91 - 100: Grade = "Outstanding"
# - Scores 81 - 90: Grade = "Exceeds Expectations"
# - Scores 71 - 80: Grade = "Acceptable"
# - Scores 70 or lower: Grade = "Fail"
student_scores = {
    'Harry': 88,
    'Ron': 78,
    'Hermione': 95,
    'Draco': 75,
    'Neville': 60
}
student_grades = {}
for key, value in student_scores.items():
    if value >= 91:
        student_grades[key] = "Outstanding"
    elif value >= 81 and value < 90:
        student_grades[key] = "Exceeds Expectations"
    elif value >= 71 and value < 80:
        student_grades[key] = "Acceptable"
    elif value < 70:
        student_grades[key] = "Fail"
print(student_grades)
# Nested lists and dictionaries
capitals = {
    "France": "Paris",
    "Germany": "Berlin",
}
travel_log = {
    "France": ["one", "two", "three"],
    "Colombia": ["four", "five", "six"],
}
print(travel_log["France"][1])
nested_list = ["a", "b", "c", ["d", "e", "f"]]
print(nested_list[3][1])
trabel_log = {
    "France": {
        "one": "value for one",
        "two": ["Paris", "Berlin", "Lille"],
        "three": "value for three",
    },
    "Colombia": ["four", "five", "six"],
}
print("#######################")
print(trabel_log["France"]["two"][2])
#