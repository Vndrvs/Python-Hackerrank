# EXTRA STEPS ADDED BY ME FOR PRACTICE

if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    
    #SIMPLY PRINT COORDINATES

    coordinates = [x, y, z]
    print(coordinates)

    #PRINT ALL PERMUTATIONS
    
    myList=[]
    
    for i in range(x+1):
        for j in range(y+1):
            for k in range(z+1):
                myList.append([i, j, k])

    print(myList)
 
    #DISABLE PRINTING VARIATIONS WHERE SUM EQUALS N

    for i in range(x+1):
        for j in range(y+1):
            for k in range(z+1):
                if [x + z + n]!=n:
                    myList.append([i, j, k])

    print(myList)

    #"Please use list comprehensions rather than multiple loops, as a learning exercise."


    myList = [[X,Y,Z] for X in range(x+1) for Y in range(y+1) for Z in range(z+1) if X+Y+Z != n]
    print(myList)