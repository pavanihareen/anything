# assignment.py
doubt clarification
trouble coding the second half of the question please help with the coding part and correct the mistakes 

#Li3
WAP to check if a specific employee e is present in a company or not. Employee names are saved in a list.
e is taken as input from the user.

For example: empList = ["Ashwin", "Rachit", "Sanjana", "David", "Komal"]
            Input1: "Komal"
            Output1: "Employee is present"
            
            Input2: "Harshil"
            Output2: "Employee is not present"
 answer is 
 l=[]
#r=int(input('Enter the number of employee:'))
while(1):
    li=str(input('Enter employee name:'))
    if li.lower()=='stop':
        print('No more inputs.')
        break
    l.append(li)
print(l)       
e=str(input('Enter the employee name to check:'))
for x in l:
    l.find(e)=y
    l.index(y)
    print(y)
    print("Employee is present.")
else:
    print("Employee is not present")
