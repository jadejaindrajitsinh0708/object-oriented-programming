print("--- Python OPP Project : Employee Manegment System ")



class Employee :
    
    def __init__(self,Employee_id=None, name=None , age=None , salary=None ):
        self.__Employee_id = Employee_id
        self.name = name
        self.age = age 
        self.__salary = salary
        
    def display(self):
        
        print(f"Employee id is {self.__Employee_id}")
        print(f"Employee name  is {self.name}")
        print(f"Employee age  is {self.age}")
        print(f"Employee salary  is {self.__salary}")
        
    def set_id(self,Employee_id):
        self.__Employee_id = Employee_id
        
    def set_salary(self,salary):
        self.__salary = salary
        
    def get_id(self):
        return self.__Employee_id  
    
    def get_salary(self):
        return self.__salary
    
    def __del__(self):
        pass 
        
class Manager(Employee):
    def __init__(self,Employee_id , name , age , salary,department):
        super().__init__(Employee_id , name , age ,salary)
        
        self.department = department
        
    def display(self):
        Employee.display(self)
        print(f"Manager Department is {self.department}")

class devlopment(Employee):
    def __init__(self, Employee_id, name, age, salary,programming_language):
        super().__init__(Employee_id, name, age, salary,)
        self.programming_language = programming_language
        
    def display(self):
        super().display()
        print(f"devlopment is {self.programming_language}")
        
        
print(f" Is Manager Class Is Sub Class Of Employee Class {issubclass(Manager,Employee)}")
print(f" Is devlopment Class Is Sub Class Of Employee Class {issubclass(devlopment,Employee)}")
        
person = None
employee = None
manager = None

while True:
    
    print("Choose The Option ")
    print("1. Create a Person  ")
    print("2. Create a Employee  ")
    print("3. Create a Manager ")
    print("4. Show Details ")
    print("5. Exit.....")
    
    choice = int(input("Enter Your Choice (1-5) :- "))
    
    
    if choice == 1 :
        name = input("Enter Your Name :- ")
        age = int(input("Enter Your Age :- "))
        
        person = Employee(name=name,age=age)
        
        print(f"Person Create With Name :- {name} And Age :- {age}")
        
        
    elif choice == 2 :
        
        employee_id = int(input("Enter Employee ID :- "))
        name = input("Enter Your Name :- ")
        age = int(input("Enter Your Age :- "))
        salary = int(input("Enter Your Salary :- "))
        
        employee = Employee(employee_id,name,age,salary)
        
        print(f"Employee Created With Name :- {name} Age :- {age} ID :- {employee_id} And Salary :- {salary}")
        
    elif choice == 3 :
        
        employee_id = int(input("Enter Employee ID :- "))
        name = input("Enter Your Name :- ")
        age = int(input("Enter Your Age :- "))
        salary = int(input("Enter Your Salary :- "))
        department = input("Enter Your Department :- ")
        
        manager = Manager(employee_id,name,age,salary,department)
        
        print(f"Manager Created With Name :- {name} Age :- {age} ID :- {employee_id}  Salary :- {salary} And Department :- {department} ")
        
        
    elif choice == 4 :
        
        print("Enter Your Choose ") 
        print("1. Show Person")   
        print("2. Show Employee")   
        print("3. Show Manager")   
        
        choice = int(input("Enter Your choose (1-3):- "))
        
        if choice == 1:
            if person is None:
                print("Not Data Found In Person ")
            else:
                person.display()
        elif choice == 2:
            if not employee :
                print("Not Data Found In Employee")
            else:
                employee.display()
        elif choice == 3 :
            if manager is None :
                print("Not Data Found In Manager")
            else:
                manager.display()
                
        else:
            print("Invalid Choose ")
            
    elif choice == 5:
        break
    
    else:
        print("Invalid Choice")

print("GoodBye...")