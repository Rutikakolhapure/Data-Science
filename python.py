#unit 1:
# print('Hello')
# print(1+2)

#unit 2
# def pay_tax(num_hours):
#     pre_tax=num_hours*15
#     pay_after=pre_tax*(1-.12)
#     return pay_after
# tax_amt=pay_tax(40)
# print(tax_amt)

# class Classname:
#     'Optional class documentation string'
#     class_suite 

# class Employee:
#     empCount=0
#     def __init__(self,name,salary):
#         self.name=name
#         self.salary=salary
#         Employee.empCount+=1
        
#     def displayCount(self):
#         print("Total Employee %d" % Employee.empCount)
        
#     def displayEmployee(self):
#         print ("Name:",self.name,",Salary:",self.salary)

# class Student:
#     def __init__(self,name,rollNo):
#         self.name=name
#         self.rollNo=rollNo
# s1=Student("Rahul",50)
# print(s1.name)
# print(s1.rollNo)

# def Find_sum(n):
#     sum=0
#     for i in range(1,n+1):
#         sum+=i
#     return sum

# if __name__=='__main__':
#     print(Find_sum(5))

# def Find_sum(n):
#     if n==1:
#         return 1
#     return n+Find_sum(n-1)

# if __name__=='__main__':
#     print(Find_sum(1))


# def Fib(n): # 0,1,1,2,3,5,8,13
#     if n==0 or n==1:
#         return n
#     return Fib(n-1)+Fib(n-2)

# if __name__=='__main__':
#     print(Fib(5))



# class ATMmachine:
#     def __init__(self):
#         self.pin=""
#         self.balance=0
#         self.menu
        
#     def menu(self):
#         user_input = input(
#             """ 
#             Hi how can i help you?
#             1.Press 1 to create pin
#             2.press 2 to change pin
#             press 3 to check balance
#             press 4 to withdraw
#             5.Anything to exit
#             """
#         )
        
#         if user_input == "1":
#             self.create_pin()
#         elif user_input == "2":
#             self.change_pin() 
#         elif user_input == "3":
#             pass
#         elif user_input == "4":
#             pass
#         elif user_input == "5":
#             pass
#         else:
#             exit()
        
        
#     def create_pin(self):
#         user_pin = input("Enter your pin:")
#         self.pin = user_pin
        
#         user_balance=int(input('Enter your balance:'))
#         self.balance=user_balance
        
#         print("Pin Created Successfully!")
#         self.menu()
        
#     def change_pin(self):
#         old_pin = input("Enter your old pin:")
        
#         if old_pin==self.pin:
#             new_pin = input("Enter new pin:")
#             self.pin = new_pin
#             print("Pin changed successfully!")
#             self.menu()
#         else:
#             print("Invalid Pin!")
#             self.menu()
            
        
        
        
# obj=ATMmachine() 
# obj.menu()   



#Reference Variable in OOP
# class Person:
#     def __init__(self, name, country):
#         self.name = "Rutti"
#         self.country = "india"
        
# p=Person()
# id(p)
# q=p
# id(q) #even if you change the value of the q the value of the p will also be changed.



#Pass by reference in OOP
# class Person:
#     def __init__(self, name, gender):
#         self.name = name
#         self.gender = gender 

# def greeting(Person):
#     print(f"HI my name is {Person.name} and I am {Person .gender}")
 
# p=Person("Rutika","Male") 
# greeting(p)
    


#What is instance variable in OOP
# class Person:
#     def __init__(self, name):
#         self.name = name
# p1=Person("Rutika")       
# p2=Person("Bhakti")
# p3=Person("Soumya")

# print(p1.name)
# print(p2.name)
# print(p3.name)




#static variable
# class ATMmachine:
#     customer_id=0
    
#     def __init__(self):
#         self.pin=""
#         self.balance=0
#         self.customer_id = ATMmachine.customer_id
#         ATMmachine.customer_id +=1
#         # self.menu
        
#     @staticmethod
#     def get_customer_id():
#         return ATMmachine.__customer_id
        
#     def menu(self):
#         user_input = input(
#             """ 
#             Hi how can i help you?
#             1.Press 1 to create pin
#             2.press 2 to change pin
#             press 3 to check balance
#             press 4 to withdraw
#             5.Anything to exit
#             """
#         )
        
#         if user_input == "1":
#             self.create_pin()
#         elif user_input == "2":
#             self.change_pin() 
#         elif user_input == "3":
#             pass
#         elif user_input == "4":
#             pass
#         elif user_input == "5":
#             pass
#         else:
#             exit()
        
        
#     def create_pin(self):
#         user_pin = input("Enter your pin:")
#         self.pin = user_pin
        
#         user_balance=int(input('Enter your balance:'))
#         self.balance=user_balance
        
#         print("Pin Created Successfully!")
#         self.menu()
        
#     def change_pin(self):
#         old_pin = input("Enter your old pin:")
        
#         if old_pin==self.pin:
#             new_pin = input("Enter new pin:")
#             self.pin = new_pin
#             print("Pin changed successfully!")
#             self.menu()
#         else:
#             print("Invalid Pin!")
#             self.menu()
            
# c1=ATMmachine()
# ATMmachine.customer_id
# c2=ATMmachine()
# ATMmachine.customer_id



#method overlodding
# class Shape:
#     def ares(self,radius):
#         return 3.14*radius*radius
#     def area(self,l,b):
#         return l*b
    
# s.Shape()
# s.area(2,4)






#Abstraction
# from abc import ABC,abstractmethod
# #senior
# class BankServer(ABC):
#     def database(self):
#         print("Connected to database")

#     @abstractmethod
#     def security(self):
#         print("Security passed")
    
# class MobileApp(BankServer):
#     def mobile_login(self):
#         print("Mobile app login successfull")
        
#     def security(self):
#             print("Mobile app security")