weight = float(input("Enter your weight in kgs :"))
height = float(input("Enter your height in cm  :"))

meter = height/100

bmi = weight/meter**2

print("Your Body Mass Index is",bmi)
if bmi < 18.5 :
    print("Under Weight")
elif bmi < 25 :
    print("Healthy")
else:
    print("Over Weight")

