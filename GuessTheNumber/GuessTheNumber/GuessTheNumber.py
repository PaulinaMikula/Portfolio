import random
isloggedin = False

def getData():                                                              #Class: to open, read and get data from txt file
    fp=open(r'D:\Users\Paulina\Moje\Python\UsersTable.txt','r')
    myData=fp.read()
    myData=myData.split('\n')
    myData=[l.split('\t') for l in myData]
    fp.close()
    return myData

def login(myData):                                                          #Class: to log in (data in the text file)
    global isloggedin
    rowNr=0
    print("Welcome to the game!\nIt's time to log in.")
    eUsername=input("Enter Your username: ")
    for row in myData:
        if eUsername in row:
            ePsswrd=input("Enter Your password: ")
            if row[2]==ePsswrd:
                print("You are in!")
                isloggedin=True
                return rowNr
            else: print("That's not the right password!")
        rowNr=rowNr+1    
    return rowNr

def writeData(myData, rowNr):                                               #writing data back to the text file 
    fp=open("D:\\Users\\Paulina\\Moje\\Python\\UsersTable.txt",'w')
    for i in myData:
        for j in i:
            fp.write(str(j)+'\t')
        fp.write('\n')
    return

def TheGame(myData, rowNr):                                                 #game's algorythm
    i=0 
    print("Guess The Number - let's start the game!")
    range_up=int(input("Enter the upper range: "))
    range_down=1
    print("Generated number will be from range: "+str(range_down)+"-"+str(range_up))
    y=random.randint(range_down,range_up)

    while True:
        x=int(input("Enter Your number in range from "+str(range_down)+" to "+str(range_up)+": "))
        if x>y:
            print("This number is too high")
        elif x<y:
            print("This number is too low")
        elif x==y:
            print("Congratulations! You found the number")
            
            score=int(myData[rowNr][4])
            score=score+1
            myData[rowNr][4]=str(score)
                         
            print("Your current score is: "+ myData[rowNr][4])
            break

        i=i+1
        if i%3==0:                                                          #after every 3 failed attempts, You can use a lifebuoy
            wybor_kola=input("You can use a lifebuoy as a help. Choose option:\nA - You can be given an approximate range\nB - I don't want help\n")
            wybor_kola=wybor_kola.upper()
            match wybor_kola:
                case "A":                                                   #if that's possible, the upper range is reduced to a value that is a sum                                                   
                    if y+(range_up//2)<range_down:                          #of the generated number and half of its previous size   
                        range_up=y+(range_up//2)
                    if y-(range_up//2)>range_down:              
                        range_down=y-(range_down//2)
                    print("The numbers You are looking for is in range from "+str(range_down)+" to "+str(range_up))
                case "B":
                    pass
    return

myData=getData()                                                            #Loading data
rowNr=login(myData)

if isloggedin==True:                                                        #Main program
    TheGame(myData, rowNr)
    while True:
        option=input("Do you want to play again? (Y/N) ")
        option=option.upper()
        if option=="Y":
            TheGame(myData, rowNr)
        else:
            print("Thank You for playing!")
            break
writeData(myData, rowNr)                                                    #Saving data