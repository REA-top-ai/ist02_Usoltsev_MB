from abc import ABC, abstractmethod


class AbstractEmployee(ABC):
    new_id = 1

    def __init__(self):
        self.id = AbstractEmployee.new_id
        AbstractEmployee.new_id += 1

    @abstractmethod
    def say_id(self):
        pass


class User:
    def __init__(self, username, role):
        self.username = username
        self.role = role

    def say_user_info(self):
        print(f"Username: {self.username}, Role: {self.role}")


class Employee(AbstractEmployee):
    def __init__(self, name=None):
        super().__init__()
        self._name = name
        self._id = "protected"
        self.__id = "private"

    def say_id(self):
        print(f"My id is {self.id}")

    def get_name(self):
        return self._name

    def set_name(self, name):
        if isinstance(name, str):
            self._name = name
        else:
            raise TypeError("Name must be a string")

    def del_name(self):
        del self._name


class Admin(Employee, User):
    def __init__(self):
        Employee.__init__(self)
        User.__init__(self, self.id, "Admin")

    def say_id(self):
        super().say_id()
        print("I am an Admin")


class Manager(Admin):
    def say_id(self):
        super().say_id()
        print("I am Manager")


class Meeting:
    def __init__(self):
        self.attendees = []

    def __add__(self, employee):
        self.attendees.append(employee)
        return self

    def __len__(self):
        return len(self.attendees)


e1 = Employee()
e2 = Employee()
e3 = Admin()
e4 = Manager()

e1.say_id()
e2.say_id()
e3.say_id()
e4.say_id()

e3.say_user_info()

meeting = [Employee(), Admin(), Manager()]
for person in meeting:
    person.say_id()

m1 = Meeting()
m1 = m1 + e1
m1 = m1 + e2
m1 = m1 + e3

print(len(m1))

e5 = Employee()
e5.set_name("Keyl")
print(e5.get_name())
e5.del_name()