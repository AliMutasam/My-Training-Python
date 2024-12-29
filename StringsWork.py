print("****************** Made By Ali Mutasam ********************")
print("\t      Welcome To My Text Index Word, Length, Count Project! ")
print("**********************************************************")

AskAgain = True

while AskAgain:
 myText = str(input("Enter Your Text: "))
 print("**********************************************************")
 myChoice = str(input("Enter Your Choice [1. Know Index, 2. Length of Sentnce, 3. Count Repeated Char, 4. Exit]: "))
 print("**********************************************************")
 if myChoice == "1":
    myIndex = str(input("Enter Your Word That You Wrote In Sentence To Know It's Index: "))
    print("**********************************************************")
    print(f"Your Text Word Index Is: {myText.index(myIndex)}")
    print("**********************************************************")
 elif myChoice == "2":
     myT = len(myText)
     print(f"Your Length of Your Text is: {myT}")
     print("**********************************************************")
 elif myChoice == "3":
     myR = str(input("Enter Your Char: "))
     print("**********************************************************")
     print(f"Your Char Mentioned in: {myText.count(myR)}")
     print("**********************************************************")
     # It's Sensitve so you should Type the char lower or capital like you wrote in the text...
 elif myChoice == "4":
     print("Happy Day!")
     quit()
 else:
   AskAgain = False