a=input("Please Enter Your Name ")
print("Hello",a,"Are You Ready To Play :)..........")
print("Guess The Country Name Game")
print("Each Letter is represented by a star ( * )")
print("You have to type only one letter in one try")
print("You have 8 tries to Guess the Word")
print("Please use only small letters")
print("_____________________________________________")
l=["argentina", "thailand", "nigeria", "sweden", "mexico", "south korea", "egypt", "canada", "australia", "brazil", "poland", "peru", "japan", "south africa", "ukraine", "malaysia", "iceland", "colombia", "turkey", "new zealand","united states", "china", "germany", "france", "italy", "spain", "united kingdom", "india", "japan", "canada", "australia", "brazil", "south africa", "mexico", "south korea", "saudi arabia", "russia", "turkey", "egypt", "netherlands"]
import random
b=random.choice(l)
d="***********"
y=8
x=p=0
f=''
u=len(b)
print(('*')*u,end="")
while y>0 and p<u:
    print(f)
    x=x+1
    print("Enter Your Guess",x,end=" ")
    c=input("")
    if c in b:
        print("You found a letter! ISNT THAT EXCITING !!!")
        print("You have",y,"guesses left")
        h=b.count(c)
        for e in range(h):
            for s in range(0,u):
                if c==b[s]:
                    f=d[0:s]+b[s]+d[s+1:u]
                    d=f
                    b=(b[0:s]+"*"+b[s+1:u])
                    p=p+1
                    break      
    else:
        y=y-1
        print("Whoops! That Letter is not there!")
        if y==8:
            print("      +")
            print("      |")
            print("      |")
            print("      |")
            print("      |")
            print("      |")
            print("========='")
        elif y==7:
            print("  +---+")
            print("      |")
            print("      |")
            print("      |")
            print("      |")
            print("      |")
            print("========='")
        elif y==6:
            print("  +---+")
            print("  |   |")
            print("      |")
            print("      |")
            print("      |")
            print("      |")
            print("========='")
        elif y==5:
            print("  +---+")
            print("  |   |")
            print("  O   |")
            print("      |")
            print("      |")
            print("      |")
            print("========='")
        elif y==4:
            print("  +---+")
            print("  |   |")
            print("  O   |")
            print("  |   |")
            print("      |")
            print("      |")
            print("========='")
        elif y==3:
            print("  +---+")
            print("  |   |")
            print("  O   |")
            print(" /|   |")
            print("      |")
            print("      |")
            print("========='")
        elif y==2:
            print("  +---+")
            print("  |   |")
            print("  O   |")
            print(" /|\  |")
            print("      |")
            print("      |")
            print("========='")
        elif y==1:
            print("  +---+")
            print("  |   |")
            print("  O   |")
            print(" /|\  |")
            print(" /    |")
            print("      |")
            print("========='")
        elif y==0:
            print("  +---+")
            print("  |   |")
            print("  O   |")
            print(" /|\  |")
            print(" / \  |")
            print("      |")
            print("========='")
        print("You got",y,"tries left.")
if y==0:
    print("Sorry",a,"you Have been HANGED!")
    print("HAH LOSER")
    print("The Word was : ",b)
elif p==u:
    print("Congratulations",a,"You Guessed the Word",b)
    print("Here is your reward a TOFFEE!!!!!")
    print("HAVE A NICE DAY ;)")