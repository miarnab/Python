import random
a=random.randint(1,100)
b=int(input("Enter your guess"))
c=1
while b!=a:
    c+=1
    if b<a:
        print("Guess Higher")
        b=int(input("Enter your guess"))
    else:
        print("Guess Lower")
        b=int(input("Enter your guess"))
print("You are correct")
print("You took",c,"attempts")
