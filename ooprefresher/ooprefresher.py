class SpacialUser:
    
    def specialFeatues(self):
        return "i am special"
        
    def classFunction(self):
        return "I am SpacialUser's accountFunction"


class Account:
    SalRaise = 10
    
    def __init__(self, name, salary, StartOfEmployment):
        self.name = name
        self.salary =salary
        self.StartOfEmployment = StartOfEmployment
    
    def classFunction(self):
        return "I am Account's accountFunction"
     
    def __repr__(self):
        return "Name: {} - Salary: {} - SOE: {}".format(self.name, self.salary, self.StartOfEmployment)
    
    
class User(Account):
    
    def __init__(self, name, salary, StartOfEmployment, posts):
        self.posts = posts
        super().__init__(name, salary, StartOfEmployment)

    def classFunction(self):
        print(super().classFunction())
        return "I am user's accountFunction"

class Admin(Account, SpacialUser):
    SalRaise = 20
    
    def __init__(self, name, salary, StartOfEmployment, accessLevel):
        self.accessLevel = accessLevel
        super().__init__(name, salary, StartOfEmployment)

def applyYearlyRise(arg):
    for i in arg:
        i.salary = i.salary*(i.SalRaise/100)

def main():
    employees = [Admin("Jon",100, 5)]
    applyYearlyRise(employees)
    print(employees[0])
    

if __name__ == "__main__":
    main()
    
    