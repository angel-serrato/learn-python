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
# TODO: 1: Create an empty dictionary called student_grades.
student_grades = {}
# TODO: 2: Write your code below to add the grades to student_grades.👇
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

# for student in student_scores:
#   score = student_scores[student]
#   if score > 90:
#     student_grades[student] = "Outstanding"
#   elif score > 80:
#     student_grades[student] = "Exceeds Expectations"
#   elif score > 70:
#     student_grades[student] = "Acceptable"
#   else:
#     student_grades[student] = "Fail"
# print(student_grades)

"""
Nesting lists and dictionaries
{
   Key: [List],
   Key2: {Dictionary},
}
Each key can only have one value
"""

capitals = {
   "France": "Paris",
   "Germany": "Berlin",
}

# Nesting a list in a dictionary
travel = {
   "France": ["Paris", "Lille", "Dijon"],
   "Germany": ["One", "Two", "Three"],
}

# Nesting a dicionary in a dictionary
travel = {
   "France": {"cities_visited": ["Paris", "Lille", "Dijon",], "total_visits" : 12},
   "Germany": [
      "One",
      "Two",
      "Three"
      ],
}

family = {
   "child1": {
      "name": "Angel",
      "year": 2002,
   },
   "child2": {
      "name": "Didier",
      "year": 1987,
   },
   "child3": {
      "name": "Ana",
      "year": 1957,
   }
}

# Nesting a dicionary in a list
travel = [
   {
      "country": "France",
      "cities_visited": ["Paris", "Lille", "Dijon"],
      "total_visits": 12
   },
   {
      "country": "Germany",
      "cities_visited": ["Berlin", "Hamburg", "Other"],
      "total_visits": 5
   },
]

"""
Dictionary in list exercise in auditorium
"""

country = input() # Add country name
visits = int(input()) # Number of visits
list_of_cities = eval(input()) # create list from formatted string

travel_log = [
  {
    "country": "France",
    "visits": 12,
    "cities": ["Paris", "Lille", "Dijon"]
  },
  {
    "country": "Germany",
    "visits": 5,
    "cities": ["Berlin", "Hamburg", "Stuttgart"]
  },
]
# Do NOT change the code above 👆

# TODO: Write the function that will allow new countries
# to be added to the travel_log. 
def add_new_country(pais, visitas, ciudades):
  new_country = {}
  new_country["country"] = pais
  new_country["visits"] = visitas
  new_country["cities"] = ciudades
  travel_log.append(new_country)

# Do not change the code below 👇
add_new_country(country, visits, list_of_cities)
print(f"I've been to {travel_log[2]['country']} {travel_log[2]['visits']} times.")
print(f"My favourite city was {travel_log[2]['cities'][0]}.")
