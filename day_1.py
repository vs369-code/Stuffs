'''member = True
age = 18

if member and age >= 18:
    print("you can enter.")
else:
    print("you cannot enter.")  '''

'''member = False
special_guest = True

if member or special_guest:
    print("welcome")
else:
    print("Entry denied.")'''

'''member = False

if not member:
    print("please register first.")
else:
    print("welcome member.")    '''



#1. level basic condition
member = True
if member:
    print("welcome member")
else:
    print("please register")  

#2. age check
member = True
age = 50

if member and age >= 18:
    print("adult")
elif member == False:
    print("please register your name")    
else:
    print("minor")    

#3. age check
enter = input("enter your password:")
password = "python123"

if password == enter:
    print("login successful")
 
else:
    print("wrong password")    

# level 2: 4. condition

member = True
age = 12

if member and age >= 18:
    print("entry allowed")
else:
    print("entry denied")   

#5. driving license 

license = True
age = input("Enter your age:")

if license and int(age) >= 18:
    print("You can drive.")

elif license != True:
    print("You have to pay fine.") 

else:
    print("Please don't ride becasue it's a road not your gf ass ")

#6. exam eligibility
attendance = 60
fee_paid = True

if fee_paid and attendance >= 75:
    print("you are eligible for exam")
else:
    print("you are not eligible for exam")    

#7. special entry
member = False
special_guest = True

if member or special_guest:
    print("you're getting special entry")
else:
    print("you're not getting special entry")  

#8. discount system 
student = True
member = False

if student or member:print("Discount available")
else:print("Discount not available")

#Level - 4: 9. marks grade
marks = 82
if marks >= 90:print("A")
elif marks >= 80:print("B")
elif marks >= 60:print("C")
elif marks >= 40:print("D")
else:print("fail")

#10. age category
age = int(input("enter your age:"))

if age > 0 and age < 12:print("child")
elif age > 10 and age <= 19:print("teenager")
elif age >= 20 and age <= 59:print("adult")
else:print("senior")

#11. largest number in between three number
a = 20
b = 10
c = 30

if a>b and a>c:
    largest = a 
elif b>a and b>c:
    largest=b
else:
    largest = c

print("largest is:", largest)  

#12. smallest number in between three number

a = 20
b = 30
c = 40

if a < b and a < c:
    smallest = a
elif b < a and b < c:
    smallest = b
else:
    smallest = c
print("smallest is:", smallest)        



  


