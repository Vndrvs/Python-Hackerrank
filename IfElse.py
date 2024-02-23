myString1="Weird"
myString2="Not Weird"

n=int(input())
if n%2!=0:
    print(myString1)
else:
    if n >= 2 and n<=5:
        print(myString2)
    elif n >= 6 and n <= 20:
        print(myString1)
    else:
        print(myString2)