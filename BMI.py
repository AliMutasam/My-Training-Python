print("****************** Made By Ali Mutasam********************")
print("\t      Welcome To The BMI Calculator! ")
print("**********************************************************")

ChoiceInput = str(input("Do You Want To Start(Y/N): ").capitalize())
print("*****************************************")
if ChoiceInput == "Y":
    YourWeight = float(input("Enter Your Weight in KGs: "))
    print("*****************************************")
    YourHeight = float(input("Enter Your Height in Meters: "))
    print("*****************************************")
else:
    print("Good Luck! (;")
    quit()

BMI = YourWeight / YourHeight**2

if BMI < 18.5:
    print(f"Your BMI is {BMI} and You Are [Underweight]")
elif BMI <= 24.9:
    print(f"Your BMI is {BMI} and You Are [Normal Weight]")
elif BMI <= 29.9:
    print(f"Your BMI is {BMI} and You Are [Overweight]")
elif BMI >= 30:
    print(f"Your BMI is {BMI} and You Are [Obese]")