# Creating classes
# Pascal Case: MiVariableImportante
# Camel Case: miVariableImportante
# Snake Case: mi_variable_importante
# Kebab Case: mi-variable-importante
# Upper Case Snake Case: MI_VARIABLE_IMPORTANTE
# Dot Notation: mi.variable.importante

class User:
    # Constructor
    def __init__(self, name, id):
        self.name = name
        self.id = id
        # Initial value
        self.followers = 0

    def walk(self):
        return f"The {self.name} walks"

user = User("angel", "001")
print(user.walk())
