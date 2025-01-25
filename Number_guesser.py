import random
#r=random.randint(-1,31)# will include 31 also due to rand'int'can be written as(31)also
#will not include 31 ,only till 30
top_of_range =input("Type a Number : ")
if top_of_range.isdigit():
     # if a user type a digit then it will be converted into int 
    #,if not ,user writes like'rum21'it will give error ,when "24" is wriiten python consider it a string
    #what we need is 24 which is int ,so we put int(top_of_range )so that any number entered by user can be 
    #can be converted into integer(int)
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print("Please Enter a number which is larger than 0. ")
        quit()

else:
    print("Please type a number next time. ") 
    quit()       


random_number = random.randint(0,top_of_range)
guesses = 0

while True:
    guesses +=1
    user_guess = input("Make a Guess : ")
     
    if user_guess.isdigit():  
        user_guess = int(user_guess)

    else:
        print("Please type a number next time. ")        
        continue

    if user_guess == random_number:
        print("You Got It ! ")
        break
    elif  user_guess > random_number:
        print("You choose a larger number ")
    else:
        print("You choose a smaller number") 


print("YOU GOT IT IN", guesses, "Guesses")            