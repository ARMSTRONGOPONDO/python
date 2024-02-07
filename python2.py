
# Online Python - IDE, Editor, Compiler, Interpreter
time = int(input('Enter time period of service '))
salary = int(input("Enter the salary:"))

if time >= 10:
    netsalary = (salary * 0.1) + salary
    print(netsalary)
elif 6 <= time < 10:
    netsalary = (salary * 0.8) + salary
    print(netsalary)
else:
    netsalary = salary
    print(netsalary)
    
