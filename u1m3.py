# Store

class Store:
    def __init__(self, name, departments):
        self.name = name

        # Departments will be a list of strings
        self.departments = departments

    def __str__(self):
        output = f"{self.name}\n"
        for d in self.departments:
            outputs += " " + d ", \n"
        return output 

my_store("General Store", ["Sports", "Food", "Garden"])