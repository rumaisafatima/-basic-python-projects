from cryptography.fernet import Fernet

'''
def write_key():
    key = Fernet.generate_key()
    with open("key.key","wb") as key_file:
        key_file.write(key)

write_key()'''

def load_key():
    file =open("key.key", "rb")
    key = file.read()
    file.close()
    return key

 
key = load_key()
fer=Fernet(key)
 
 

def view():
    
    with open('passwords.txt', 'r') as f:
         for line in f.readlines():
            data=line.rstrip()
            user, passw = data.split("|")
            print("users:" ,user,"| password:", fer.decrypt(passw.encode()).decode())
             
            #datasplit will give all the saved item into a string split
            #if in the file it looks like this teens|ima
            #by using data.split it will show a lists ['teens','ima']
            #it will always return two elements in it


             

def add():

    name =input("Account Name: ")
    pwd = input("password: ")


    with open('passwords.txt','a') as f:
        f.write(name + "|" + fer.encrypt(pwd.encode()).decode() + "\n")


while True:
    mode =input("Would you like to add a new password or view exisiting one (view, add),press q to quit?").lower()
    if mode =="q":
        break

    if mode == "view":
        view()
    elif mode =="add":
        add()
    else:
         print("Invalid mode.")
         continue

