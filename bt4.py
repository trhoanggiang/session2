ghit = int(input("Enter Your Height(cm) ? "))
weight = int(input("Enter Your Weight(kg) ? "))
height = ghit / 100
BMI = weight / (height*height)

if BMI < 16 :
    print("You are Severely underweight!")
elif 16 < BMI < 18.5 :
    print("You are underweight!")

elif 18.5 < BMI < 25 :
    print("You are normal!")
elif BMI >= 30 :
    print("You are obese!")



print(BMI, "is your BMI. ")