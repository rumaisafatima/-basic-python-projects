print("Welcome to my Computer Quiz !")

playing =input(("Do you wanna play this game? "))
print(playing)

if playing != "yes":
     quit()

print("Okay! Lets Play : ")   
score = 0

text ="I AM RUMAIsa"
print(text. lower())
answer = input("What does CPU stands for? ")
if answer.lower() == "central processing unit":
    print("correct !")
    score +=1

else:
     print("wrong !")  
answer = input("What does WWW stands for? ")       
if answer.lower() == "world wide web":
    print("correct !")
    score +=1
else:
     print("wrong !")   
answer = input("What does PIA stands for? ")     
if answer.lower() == "pakistan international airlines":
    print("correct !")
    score +=1
else:
     print("wrong !")   
answer = input("What does JK stands for? ")
if answer.lower() == "jungkook":
    print("correct !")
    score +=1
else:
     print("wrong !")   

print( "You got" +  str(score) +  "questions correct!")
print( "You got" +  str((score / 4) *100)   +  "%.")

#"rum"+"1" answer will be "rum1"