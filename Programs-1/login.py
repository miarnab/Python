email="abc@gmail.com"
password=1234
e1=input("Enter the email")
p1=input("Enter the password")
if email==e1 and password==p1:
	print("Hello! Welcome User")
elif email==e1 and passowrd!=p1:
    print("Incorrect Password")
    p2=input("Enter the new password")
    if password==p2:
        print("Welcome")
    else:
        print("Incorrect Password")
else:
	print("Incorrect email or password")
