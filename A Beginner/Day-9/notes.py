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