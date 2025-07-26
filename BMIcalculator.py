# Making my first BMI calculator

weight = float(input("Enter your weight in Kg " ))
height = float(input("Enter your height in m "))
bmi = weight/(height*height)
print("Your BMI score is : " , bmi )

if bmi < 18.5:
    print("You are under weight")
elif bmi < 25:
    print("You are normal weight")
else:
    print("You are over weight")