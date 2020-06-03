class Store:
    def __init__(self, name, departments):
        self.name = name
        # Departments will be a list of strings
        self.departments = self.init_departments(departments)

    def __str__(self):
        output = f"{self.name}\n"
        for d in self.departments:
            output += " id: " + str(d.id()) + ", name: " + d.name() + "\n"
        return output 

    def init_departments(self, departments):
        '''
        instances = []
        for i, d in enumerate(departments):
            instances.append(Department(i + 1, d))
        return instances
        '''
        return [Department(i + 1, d) for i, d in enumerate(departments)]

class Department:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __str__(self):
        return f"Department {self.id}: {self.name}"

    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

departments = [
    "Running",
    "Fishing",
    "Food"]

my_store = Store("General Store", departments)
print(my_store)


# add a way for a user to select departments
selection = int(input("Select a department number: "))

print(f"\nYou selected department number {selection}, {department[selection-1].get_name()}")