def classify_age():
    age = int(input("Enter your age:"))
    if age < 0:
        print("Invaluid age!")
    elif age <= 12:
        print("Child")
    elif age <= 19:
        print("Teenager")
    elif age <= 64:
        print("Senior")
classify_age()            
