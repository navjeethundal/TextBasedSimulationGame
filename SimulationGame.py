#Author: Navjeet Hundal
#Version 1.0


#This program is simulation game where you have 13 week/turns to collect work and fun points
#Limitation: saves game stats to stats.txt
#Features: (1) Reading a file and creating the world
#(2) Playermovement
#(3) Pavol
#(4) Full working taminator ex. taminator appears and taminator movement
#(5) Full cheat menu ex. debug on and off, if on then error messages are shown, create taminator, quit cheat menu
#(6) Saving stats to stats.txt


#Creating contants and importing random module
import random
MIN = 0
SIZE = 10
NUM_TURNS = 13
STUDENT = "S"
WORK = "w"
FUN = "f"
TAMINATOR = "T"
N = 8
S = 2
W = 4
E = 6
NE = 9
SE = 3
SW = 1
NW = 7
STAY = 5
CHEAT = 0
REPLACEMENT_VALUE = " "


# Author:  James Tam
# This function was created entirely by the above author and is
# used with permission.
# '''
# @ This function comes the creation of the list with file input.
# @ It combines readFromFile() and intialize() into one function.
# @ Normally a function should only implement one well define task but in this case
# @ the creation of the list is so trivial it may be okay to combine it with file input.
# @createListFileRead()
# @Argument: None
# @Return value: the game world in the form of a 2D list (each element has
# @been initialized to values read in from the input file
# '''
#Creating a function that reads the file to create the world
#CreateListFileRead()
#Return world which is a str
def createListFileRead():
    r = -1
    c = -1
    world = []
    File = True
    while (File == True):
        inputFilename = input("Name of input file: ")
        try:
            inputFile = open(inputFilename,"r")
            r = 0
            for line in inputFile:
                world.append([])
                c = 0
                for ch in line:
                    if (c < SIZE):
                        world[r].append(ch)
                    c = c + 1
                r = r + 1
            inputFile.close()
            File = False

        except IOError:
            print("Error reading from " + inputFilename)
    
    return(world) 

# Author:  James Tam
# This function was created entirely by the above author and is
# used with permission.
# '''
# @display()
# @Argument: a reference the 2D list which is game world.
# @The list must be already created and properly initialized
# @prior to calling this function!
# @Return value: Mone
# @Displays each element of the world with each row all on one line
# @Each element is bound: above, left, right and below with a bar (to
# @make elements easier to see.
# '''
#Creating a function that displays the world
#display(str)
def display(world):
    for r in range (0, SIZE, 1):
    # Row of dashes before each row
        for i in range (0, SIZE, 1):
            print(" -", end="")
        print()
        for c in range (0, SIZE, 1):
            # Vertical bar before displaying each element
            print("|" + world[r][c], end="")
        print("|") # Vertical bar right of last element + CR to
		           # move output to the next line

    # A line of dashes before each row, one line after the last
    # row.
    for i in range (0, SIZE, 1):
        print(" -", end="")
    print()


# Author:  James Tam
# This function was created entirely by the above author and is
# used with permission.
#Creating a function that checks if location is in bounds
#inBounds(str,int,int)
#Returns bounds which is true or false
def inBounds(world,row,column):
    bounds = True
    if ((row < 0) or    \
        (row >= SIZE)or \
        (column < 0) or \
        (column >= SIZE)):
        bounds = False
    return(bounds)


#Creating a function that deletes the old students location
#modify(str)
def modify(world):
    for row in range(MIN,SIZE,1):
        for column in range(MIN,SIZE,1):
            if (world[row][column] == STUDENT): 
                bounds = inBounds(world,row,column)
                if (bounds == True):
                    world[row][column] = REPLACEMENT_VALUE #Replace old student with empty string
   

#Creating a function that shows movement info
#PlayerMovementInfo(str,int,int,int)
def PlayerMovementInfo(world,turn,fun_points,gpa):
    print("Current turn:",turn)
    print("Fun points:",fun_points, "GPA:",gpa)
    display(world)
    if turn < 13:
        print("MOVEMENT OPTIONS")
        print("""7 8 9
4 5 6
1 2 3""")
    

#Creating a function that checks players input
#PlayerInputCheck(int,str,int,int,int,true or false)
#Returns movement_option which is an int
def PlayerInputCheck(movement_option,world,turn,fun_points,gpa,debugOn):
    try:
        movement_option = input("""Type a number on the key pad to indicate
direction of movement
Type 5 to pass on movement
Selection:""")
        movement_option = int(movement_option)
        if (movement_option < 0 or movement_option > 9):
            while (movement_option < 0 or movement_option > 9):
                if debugOn == True: #show error message when debugOn = True
                    print("That direction doesn't exist please choose from 0-9")
                PlayerMovementInfo(world,turn,fun_points,gpa)
                movement_option = input("""Type a number on the key pad to indicate
direction of movement
Type 5 to pass on movement
Selection:""")
                movement_option = int(movement_option)
    except ValueError:
        if debugOn == True: #Show error message when debugOn = True
            print("Error:'" + movement_option + "'is not a integer")
   
        
    return movement_option


#Creating a function that finds the students location
#GetStudentLocation(str)
#Returns row and column which are int
def GetStudentLocation(world):
    for r in range(MIN,SIZE,1):
        for c in range(MIN,SIZE,1):
            if (world[r][c] == STUDENT):
                row = r
                column = c
 
    return row, column;


#Creating a function that counts when a student steps on a work or fun and puts student in new location
#modifyElement(str,int,int,int,int,true or false)
#Returns fun_points and gpa which are int
def modifyElement(world,row,column,fun_points,gpa,debugOn):
    bounds = inBounds(world,row,column)
    if bounds == True and world[row][column] != TAMINATOR:
        if (world[row][column] == FUN):
            fun_points = fun_points + 1
        if (world[row][column] == WORK):
            gpa = gpa + 1
        
        world[row][column] = STUDENT
    else:
        if debugOn == True: #Show error message when debugOn = True
            print("Location is not in bounds")
    return fun_points, gpa; 
 

#Creating a function where the user doesnt move
#PlayerMovementStay(str,str,int,int,str,int,true or false)
#Returns turn, tam_life which are int and tam_on which is true or false
def PlayerMovementStay(STUDENT,world,movement_option,turn,pavol,tam_life,tam_on):
    if (movement_option == STAY):
        turn,pavol = Pavol(turn,pavol,tam_on)
        tam_life,tam_on = Taminator(turn,pavol,world,tam_life,tam_on)
    return turn, tam_life, tam_on;


#Creating a function where the user can move N,NE,NW
#PlayerMovementNorth(str,str,int,int,int,int,str,int,true or false,true or false)
#Returns turn,fun_points,tam_life whic ae int and tam_on which is true or false
def PlayerMovementNorth(STUDENT,world,movement_option,turn,fun_points,gpa,pavol,tam_life,tam_on,debugOn):
        if (movement_option == N):
            row, column = GetStudentLocation(world)
            row = row - 1
            bounds = inBounds(world,row,column)
            if (bounds == True) and (world[row][column] != TAMINATOR):
                modify(world)
                fun_points,gpa = modifyElement(world,row,column,fun_points,gpa,debugOn)
                turn,pavol = Pavol(turn,pavol,tam_on)
                tam_life,tam_on = Taminator(turn,pavol,world,tam_life,tam_on)
            else:
                if debugOn == True: #Show error message when debugOn = True
                    print("out of bounds")
        if (movement_option == NE):
            row, column = GetStudentLocation(world)
            row = row - 1
            column = column + 1
            bounds = inBounds(world,row,column)
            if (bounds == True) and (world[row][column] != TAMINATOR):
                modify(world)
                fun_points,gpa = modifyElement(world,row,column,fun_points,gpa,debugOn)
                turn,pavol = Pavol(turn,pavol,tam_on)
                tam_life,tam_on = Taminator(turn,pavol,world,tam_life,tam_on)
            else:
                if debugOn == True: #Show error message when debugOn = True
                    print("out of bounds")
        if (movement_option == NW):
            row, column = GetStudentLocation(world)
            row = row - 1
            column = column - 1
            bounds = inBounds(world,row,column)
            if (bounds == True) and (world[row][column] != TAMINATOR):
                modify(world)
                fun_points,gpa = modifyElement(world,row,column,fun_points,gpa,debugOn)
                turn,pavol = Pavol(turn,pavol,tam_on)
                tam_life,tam_on = Taminator(turn,pavol,world,tam_life,tam_on)
            else:
                if debugOn == True: #Show error message when debugOn = True
                    print("out of bounds")
        return turn, fun_points, gpa, tam_life, tam_on;


#Creating a function where the user can move S,SE,SW
#PlayerMovementSouth(str,str,int,int,int,int,str,int,true or false,true or false)
#Returns turn,fun_points,gpa,tam_life which are int and tam_on which is true or false
def PlayerMovementSouth(STUDENT,world,movement_option,turn,fun_points,gpa,pavol,tam_life,tam_on,debugOn):
    if (movement_option == S):
        row, column = GetStudentLocation(world)
        row = row + 1 
        bounds = inBounds(world,row,column)
        if (bounds == True) and (world[row][column] != TAMINATOR):
            modify(world)
            fun_points,gpa = modifyElement(world,row,column,fun_points,gpa,debugOn)
            turn,pavol = Pavol(turn,pavol,tam_on)
            tam_life,tam_on = Taminator(turn,pavol,world,tam_life,tam_on)
        else:
            if debugOn == True: #Show error message when debugOn = True
                print("out of bounds")
    if (movement_option == SE):
        row, column = GetStudentLocation(world)
        row = row + 1
        column = column + 1
        bounds = inBounds(world,row,column)
        if (bounds == True) and (world[row][column] != TAMINATOR):
            modify(world)
            fun_points,gpa = modifyElement(world,row,column,fun_points,gpa,debugOn)
            turn,pavol = Pavol(turn,pavol,tam_on)
            tam_life,tam_on = Taminator(turn,pavol,world,tam_life,tam_on)
        else:
            if debugOn == True: #Show error message when debugOn = True
                print("out of bounds")
    if (movement_option == SW):
        row, column = GetStudentLocation(world)
        row = row + 1
        column = column - 1
        bounds = inBounds(world,row,column)
        if (bounds == True) and (world[row][column] != TAMINATOR):
            modify(world)
            fun_points,gpa = modifyElement(world,row,column,fun_points,gpa,debugOn)
            turn,pavol = Pavol(turn,pavol,tam_on)
            tam_life,tam_on = Taminator(turn,pavol,world,tam_life,tam_on)
        else:
            if debugOn == True: #Show error message when debugOn = True
                print("out of bounds")
    return turn, fun_points, gpa, tam_life, tam_on;


#Creating a function where the user can move east
#PlayerMovementEast(str,str,int,int,int,int,str,int,true or false,true or false)
#Returns turn,fun_points,gpa,tam_life which are int and tam_on which is true or false
def PlayerMovementEast(STUDENT,world,movement_option,turn,fun_points,gpa,pavol,tam_life,tam_on,debugOn):
    if (movement_option == E):
        row, column = GetStudentLocation(world)
        column = column + 1
        bounds = inBounds(world,row,column)
        if (bounds == True) and (world[row][column] != TAMINATOR):
            modify(world)
            fun_points,gpa = modifyElement(world,row,column,fun_points,gpa,debugOn)
            turn,pavol = Pavol(turn,pavol,tam_on)
            tam_life,tam_on = Taminator(turn,pavol,world,tam_life,tam_on)
        else:
            if debugOn == True: #Show error message when debugOn = True
                print("out of bounds")
    return turn, fun_points, gpa, tam_life, tam_on;


#Creating a function where user can move west
#PlayerMovementWest(str,str,int,int,int,int,str,int,true or false,true or false)
#Returns turn,fun_points,gpa,tam_life which are int and tam_on which is true or false
def PlayerMovementWest(STUDENT,world,movement_option,turn,fun_points,gpa,pavol,tam_life,tam_on,debugOn):
    if (movement_option == W):
        row, column = GetStudentLocation(world)
        column = column - 1
        bounds = inBounds(world,row,column)
        if (bounds == True) and (world[row][column] != TAMINATOR):
            modify(world)
            fun_points,gpa = modifyElement(world,row,column,fun_points,gpa,debugOn)
            turn,pavol = Pavol(turn,pavol,tam_on)
            tam_life,tam_on = Taminator(turn,pavol,world,tam_life,tam_on)
        else:
            if debugOn == True: #Show error when debugOn = True
                print("out of bounds")
    return turn, fun_points, gpa, tam_life, tam_on;


#Creating a function that makes the pavol
#Pavol(int,str,true or false)
#Returns turn which is an int and pavol which is a str
def Pavol(turn,pavol,tam_on):
    pavol = "off"
    chance = random.randint(1,100)
    if chance <= 10 and tam_on == False:
        turn = turn
        pavol = "on"
        print("The Pavol manefest itself and stops time for one turn")
        
    else:
        if (turn <= NUM_TURNS):
            turn = turn + 1
            pavol = "off"
    return turn, pavol;


#Creating a function that actives the taminator randomly
#TaminatorActive(int,str,str,true or false)
#Returns pavol which is a str and tam_life which is an int
def TaminatorActive(turn,pavol,world,tam_life):
    row = random.randint(0,9)
    column = random.randint(0,9)
    if world[row][column] != STUDENT:
        world[row][column] = TAMINATOR
        print("The taminator appeared")
 
        tam_life = 0
    else:
        while True:
            row = random.randint(0,9)
            column = random.randint(0,9)
            if world[row][column] != STUDENT:
                world[row][column] = TAMINATOR
                tam_life = 0
                break
        print("The taminator appeared")
    return pavol, tam_life;


#Creating a function that checks  user row input when they try to place the taminator
#TamInputRowCheck(int,str,int,true or false)
#Return row which is an int
def TamInputRowCheck(row,world,turn,debugOn):
    tam_input = True
    while tam_input == True:
        try:
            row = input("Enter row 0-9: ")
            row = int(row)
            if (row < 0 or row > 9):
                while (row < 0 or row > 9):
                    if debugOn == True: #Show error message when debugOn = True
                        print("That row doesn't exist please choose from 0-9")
                    
                    row = input("Enter row 0-9: ")
                    row = int(row)
            tam_input = False
          
        except ValueError:
            if debugOn == True: #Show error message when debugOn = True
                print("Error:'" + row + "'is not a interger")
 
    return row


#Creating a function that checks user column input when they try to place the taminator
#TamInputColumnCheck(int,str,int,true or false)
#Returns column which is an int
def TamInputColumnCheck(column,world,turn,debugOn):
    tam_input = True
    while tam_input == True:
        try:
            column = input("Enter column from 0-9: ")
            column = int(column)
            if (column < 0 or column > 9):
                while (column < 0 or column > 9):
                    if debugOn == True: #Show error message when debugOn = True
                        print("That column doesn't exist please choose from 0-9")
                        
                    row = input("Enter column from 0-9: ")
                    column = int(column)
            tam_input = False
          
        except ValueError:
            if debugOn == True: #Show error message when debugOn = True
                print("Error:'" + column + "'is not a interger")
 
    return column


#Creating a function that calls the taminator from the cheat menu
#TaminatorUserCall(int,str,str,int,true or false,true or false)
#Returns pavol which is a str and tam_life which is an int and tam_on which is true or false
def TaminatorUserCall(turn,pavol,world,tam_life,tam_on,debugOn):
    row = 0
    column = 0
    row = TamInputRowCheck(row,world,turn,debugOn)
    column = TamInputColumnCheck(column,world,turn,debugOn)
    if world[row][column] != STUDENT:
        world[row][column] = TAMINATOR
        print("The taminator appeared")
 
        tam_life = 0
        tam_on = True
    else:
        while True:
            if debugOn == True: #Show error message when debugOn = True
                print("Taminator can't be place on top of student please pick another position")
            row = TamInputRowCheck(row,world,turn,debugOn)
            column = TamInputColumnCheck(column,world,turn,debugOn)
            if world[row][column] != STUDENT:
                world[row][column] = TAMINATOR
                print("The taminator appeared")
 
                tam_life = 0
                tam_on = True
                break
        
    return pavol, tam_life, tam_on;
        
    
#Creating a function that has a 25 percent chance to call the taminator
#Taminator(int,str,str,int,true or false)
#Returns tam_life which is an int and tam_on which is true or false
def Taminator(turn,pavol,world,tam_life,tam_on):
    chance = random.randint(1,100)
    if (chance <= 25) and (pavol == "off") and (tam_life == 1):
        pavol, tam_life = TaminatorActive(turn,pavol,world,tam_life)
        tam_on = True
    return tam_life, tam_on


#Creating a function that gets the taminators location
#GetTaminatorLocation(str,int,int)
#Returns row_tam,column_tam which are int
def GetTaminatorLocation(world,row_tam,column_tam):
    for r in range(MIN,SIZE,1):
        for c in range(MIN,SIZE,1):
            if (world[r][c] == TAMINATOR):
                row_tam = r
                column_tam = c
    return row_tam, column_tam;


#Creating a function that removes the taminaators last location
#modifyTam(str)
def modifyTam(world):
    for row in range(MIN,SIZE,1):
        for column in range(MIN,SIZE,1):
            if (world[row][column] == TAMINATOR):
                bounds = inBounds(world,row,column)
                if (bounds == True):
                    world[row][column] = REPLACEMENT_VALUE


# Author:  James Tam
# This function was created entirely by the above author and is
# used with permission.
#Creating a function that checks the bounds for the taminator
#inBoundsTam(str,int,int)
#Returns bounds which is true or false
def inBoundsTam(world,row_tam,column_tam):
    bounds = True
    if ((row_tam < 0) or    \
        (row_tam >= SIZE)or \
        (column_tam < 0) or \
        (column_tam >= SIZE)):
        bounds = True
    return(bounds)


#Creating a function that destroyes the work or fun collectibles if the taminator stops on them
#Placing the taminator at his new location
#modifyTamElement(str,int,int,int,int,true or false)
#Returns fun_points,gpa whch are int
def modifyTamElement(world,row_tam,column_tam,fun_points,gpa,debugOn):
    bounds = inBoundsTam(world,row_tam,column_tam)
    if bounds == True and world[row_tam][column_tam] != STUDENT:
        if (world[row_tam][column_tam] == FUN):
            fun_points = fun_points 
        if (world[row_tam][column_tam] == WORK):
            gpa = gpa 
        
        world[row_tam][column_tam] = TAMINATOR
    else:
        if debugOn == True: #Show when debugOn = True
            print("Location is not in bounds")
    return fun_points, gpa; 


#Creating an algorithm that makes the taminator move
#TaminatorMovement(str,str,int,int,int,int,str,int,int,true or false,int,int,true or false)
#Returns tam_on which is true or false and tam_turn,row_tam,column_tam which are int
def TaminatorMovement(STUDENT,world,movement_option,turn,fun_points,gpa,pavol,tam_life,tam_turn,tam_on,row_tam,column_tam,debugOn):
    row = 0
    column = 0
    if tam_turn < 3:
        row_tam, column_tam = GetTaminatorLocation(world,row_tam,column_tam)
        row, column = GetStudentLocation(world)
        if row_tam < row:
            if row_tam + 1 < row:
                if row_tam + 2 < row and row_tam != STUDENT:
                    row_tam = row_tam + 2
                else:
                    if row_tam + 1 < row and row_tam != STUDENT:
                        row_tam = row_tam + 1
        if row_tam > row:
            if row_tam - 1 > row:
                if row_tam - 2 > row and row_tam != STUDENT:
                    row_tam = row_tam - 2
                else:
                    if row_tam - 1 > row and row_tam != STUDENT:
                        row_tam = row_tam - 1


        if column_tam < column:
            if column_tam + 1 < column:
                if column_tam + 2 < column and column_tam != STUDENT:
                    column_tam = column_tam + 2
                else:
                    if column_tam + 1 < column and column_tam != STUDENT:
                        column_tam = column_tam + 1
        if column_tam > column:
            if column_tam - 1 > column:
                if column_tam - 2 > column and column_tam != STUDENT:
                    column_tam = column_tam - 2
                else:
                    if column_tam - 1 > column and column_tam != STUDENT:
                          column_tam = column_tam - 1

        modifyTam(world)
        modifyTamElement(world,row_tam,column_tam,fun_points,gpa,debugOn)
        tam_turn = tam_turn + 1
                
    else:
        modifyTam(world)
        tam_on = False
        print("The taminator ran out of power and vanished into thin air")

    return tam_turn, tam_on, row_tam, column_tam;


#Creating a function that checks user cheat input
#CheatInputCheck(int,true or false)
#Returns movement_option which is an int
def CheatInputCheck(movement_options,debugOn):
    options = ["q","m","t"]
    try:
        if debugOn == True: #Show when debugOn = True
            print("""Type:
(t)oggle debug mode off""")
        else:
            print("""Type:
(t)oggle debug mode on""")
        print("""(m)ake the taminator appear
(q)uit cheat menu""")

        movement_option = str(input("Cheat menu selection:"))
        if (movement_option not in options):
            while (movement_option not in options):
                if debugOn == True: #Show when debugOn = True
                    print("Error:'" + movement_option + "'is not a string of either t,m,q")
                if debugOn == True: #Show when debugOn = True
                    print("""Type:
(t)oggle debug mode off""")
                else:
                    print("""Type:
(t)oggle debug mode on""")
                print("""(m)ake the taminator appear
(q)uit cheat menu""")
                movement_option = str(input("Cheat menu selection:"))

    except TypeError:
        if debugOn == True: #Show when debugOn = True
            print("Error:'" + movement_option + "'is not a integer")
    return movement_option


#Creating a function that makes the cheat menu
#CheatMenu(int,str,int,str,int,true or false,true or false)
#Returns pavol which is a str and tam_life,turn which are int and tam_on,debugOn which are true or false
def CheatMenu(movement_option,world,turn,pavol,tam_life,tam_on,debugOn):
    movement_option = CheatInputCheck(movement_option,debugOn)
    if movement_option == "m":
        if tam_life == 1:
            turn = turn + 1
            pavol, tam_life, tam_on = TaminatorUserCall(turn,pavol,world,tam_life,tam_on,debugOn)
        else:
            print(".....seems like taminator can't be called anymore")
        return pavol, tam_life, tam_on, turn, debugOn;
    if movement_option == "q":
        turn = turn + 1
        return pavol, tam_life, tam_on, turn, debugOn;
    if movement_option == "t":
        turn = turn + 1
        if debugOn == True:
            debugOn = False #turning off debugging messages
        else:
            if debugOn == False:
                debugOn = True #Turning on debugging messages
        
    return pavol, tam_life, tam_on, turn, debugOn;                               
               
                                      
#Creating a function that that calls player movement
#GameHandling(str,str,int,int,int,str,int,int,true or false,int,int,true or false)
def GameHandling(STUDENT,world,turn,fun_points,gpa,pavol,tam_life,tam_turn,tam_on,row_tam,column_tam,debugOn):
    Game = True
    tam_start = 0
    while (Game == True):
        movement_option = -1
        try: #To see if all elements in the file that was opened is in bounds
            PlayerMovementInfo(world,turn,fun_points,gpa)
        except IndexError:
            print("Error: File has elements out of range")
            world = createListFileRead()
            PlayerMovementInfo(world,turn,fun_points,gpa)
            
            
        if turn >= 13:
            break
        
        movement_option = PlayerInputCheck(movement_option,world,turn,fun_points,gpa,debugOn)
        turn,fun_points,gpa,tam_life,tam_on = PlayerMovementNorth(STUDENT,world,movement_option,turn,fun_points,gpa,pavol,tam_life,tam_on,debugOn)
        turn,fun_points,gpa,tam_life,tam_on = PlayerMovementSouth(STUDENT,world,movement_option,turn,fun_points,gpa,pavol,tam_life,tam_on,debugOn)
        turn,fun_points,gpa,tam_life,tam_on = PlayerMovementEast(STUDENT,world,movement_option,turn,fun_points,gpa,pavol,tam_life,tam_on,debugOn)
        turn,fun_points,gpa,tam_life,tam_on = PlayerMovementWest(STUDENT,world,movement_option,turn,fun_points,gpa,pavol,tam_life,tam_on,debugOn)
        turn,tam_life,tam_on = PlayerMovementStay(STUDENT,world,movement_option,turn,pavol,tam_life,tam_on)
        if (movement_option == CHEAT):
            pavol,tam_life,tam_on,turn,debugOn = CheatMenu(movement_option,world,turn,pavol,tam_life,tam_on,debugOn)
        if tam_on == True and tam_start == 1:
            tam_turn,tam_on,row_tam,column_tam = TaminatorMovement(STUDENT,world,movement_option,turn,fun_points,gpa,pavol,tam_life,tam_turn,tam_on,row_tam,column_tam,debugOn)
            if world[row_tam + 1][column_tam] == STUDENT:
                turn = turn + 2

            if world[row_tam -1 ][column_tam] == STUDENT:
                turn = turn + 2

            if world[row_tam][column_tam + 1] == STUDENT:
                turn = turn + 2

            if world[row_tam][column_tam + 1] == STUDENT:
                turn = turn + 2

            if world[row_tam + 1][column_tam + 1] == STUDENT:
                turn = turn + 2
                
            if world[row_tam -1 ][column_tam + 1] == STUDENT:
                turn = turn + 2

            if world[row_tam + 1][column_tam - 1] == STUDENT:
                turn = turn + 2

            if world[row_tam -1 ][column_tam - 1] == STUDENT:
                turn = turn + 2
        if tam_start == 0 and tam_on == True:
            tam_start = 1
    SaveStatsFile(gpa,fun_points) # calls the function that saves when game ends
        

#Creating a function that saves the games stats into a file called stats.txt
#SaveStatsFile(int,int)
def SaveStatsFile(gpa,fun_points):
    File = True
    while File == True:
        try:
            file = open("stats.txt","w")
            
            if gpa >= 4:
                file.write("GPA: 4""\n")
                file.write("Letter grade point: A""\n")
            if gpa == 3:
                file.write("GPA: 3""\n")
                file.write("Letter grade point: B""\n")
            if gpa == 2:
                file.write("GPA: 2""\n")
                file.write("Letter grade point: C""\n")
            if gpa == 1:
                file.write("GPA: 1""\n")
                file.write("Letter grade point: D""\n")
            if gpa == 0:
                file.write("GPA: 0""\n")
                file.write("Letter grade point: F""\n")
            fun_points = "Fun points collected: " + str(fun_points)
            file.write(fun_points)
            file.close()
            print("Completed writing to file: " + "stats.txt")
            File = False
                
        except IOError:
            print("Error closing stats.txt")
            print("File not saved")
            File = False
            
               
            
#################################################################
# Author:  James Tam
# This function was created entirely by the above author and is
# used with permission.
#Starting function
def start():
    turn = 0
    fun_points = 0
    gpa = 0
    pavol = "off"
    tam_life = 1
    tam_turn = 1
    row_tam = 0
    column_tam = 0
    tam_on = False
    debugOn = True
    world = createListFileRead()
    GameHandling(STUDENT,world,turn,fun_points,gpa,pavol,tam_life,tam_turn,tam_on,row_tam,column_tam,debugOn)

start() #Calls the start function
