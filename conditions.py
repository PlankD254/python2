#Python uses 'if' statements to evaluate conditions
#driver_age=int(input("Please enter age: "))
#if(driver_age>= 18):
 #   print("Eligibal to acquire licence")
#else:   
 #   print(f"Grow up a bit kid, another {18-driver_age} years to go")
student_mark=int(input("Enter final mark: "))

if(student_mark >=70):
    print("Pass:Grade A")
elif (student_mark>=60):
    print("Pass:Grade B")
elif(student_mark>=50) :
    print("Pass:Grade C")
elif(student_mark>=40) :       
     print("Pass:Grade D")
else:
    print("Fail")