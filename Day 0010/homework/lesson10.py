authorised = False
password = "irakliusa025"

while authorised != True:
    user_pass = input("please enter your password: ")
    if user_pass == password:
        print("Accses granted")