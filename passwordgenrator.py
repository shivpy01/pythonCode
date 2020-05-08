import random


def genratepassword():
    passw = ''
    for i in range(3):
        passw += str(random.randint(0,9))+chr(random.randint(97,122))+chr(random.randint(65,90))+random.choices(['*','/','-','+','!','@','#','$','%','&','^'])[0]


    print(passw)
    password = list(passw)
    random.shuffle(password)
    passwords = ''.join(password)
    return passwords


print(genratepassword())