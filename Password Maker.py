import random
import string

characters = list(string.ascii_letters + string.digits + string.punctuation)

def get_size_of_password ():
    while True :
        try :
            size_obtained = int(input("What will be the password's size?\n"))
            return size_obtained
        except ValueError:
            print("Please enter an integer, thanks.\n")
size = get_size_of_password()
password = ''
for _ in range(size):
    character=random.choice(characters)
    password += character
print("Here is the generated password ==> " , password)
