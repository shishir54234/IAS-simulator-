#ADD OVERFLOW CONDITIONS 
#MULTIPLY functionS
#divison function
#average of numbers

PC=0
IBR=0
IR=0
AC=0
MBR=0
MQ=0
def execute(y,memory):
    global AC
    global PC
    global MBR
    global MQ
    MAR=PC
    IBR=y%(0b1<<20)
    IR=y>>32 
    MAR=(y>>20)%(0b1<<12)
    if(IR==0b00000000): #HALT
    
        print("HALT")
        return 0
    
    elif(IR==0b00000001): #LOAD
        print(f"LOAD ", MAR)
        MBR=memory[MAR]
        AC=MBR
        if(int(AC)>2**40):
            print("overflow")
            quit()
    elif(IR==0b00000101): #ADD
        AC=int(AC)
        memory[MAR]=int(memory[MAR])
        print("WE are adding now")
        AC=AC+memory[MAR]
        if(AC>2*40):
            print("overflow")
            quit()



    elif(IR==0b00000110): #subtracting 
        AC=int(AC)
        memory[MAR]=int(memory[MAR])    
        print("we are subtracting now")
        AC=AC-memory[MAR]



    elif(IR==0b00100001): #STORE
        print(f"ac is", AC)
        MBR=AC
        memory[MAR]=MBR
        print(f"output is", memory[MAR])


    elif(IR==0b00001011): #multiply
        MBR=int(memory[MAR])
        MBR=MBR*MQ 
        
        if(MBR<<80):
            print("overflow")
            quit()
        MQ=MBR<<40
        AC=MBR%(1<<40)

    elif(IR==0b00001001): #LOAD M(x) onto MQ
        MBR=memory[MAR]
        MQ=int(MBR)


    elif(IR==0b00001010):#transfering contents of MQ to AC
        AC=MQ
        print(f"product is", AC)


    elif(IR==0b00001111): #JUMP + M(X, 0:19)
        if(AC>=0):
            PC=MAR
            AC=memory[1]
            MBR=memory[MAR]
            execute(MBR,memory)
            return 0
        if(AC<0):
            AC=memory[0]
            print(f"AC IS", AC)



    elif(IR==0b00001101): #JUMP
        execute(memory[MAR],memory)


    elif(IR==0b00001100): #divison
        memory[MAR]=int(memory[MAR])
        quotient=AC//(memory[MAR])
        remainder=AC%(memory[MAR])
        AC=remainder 
        MQ=quotient


    elif(IR==0b00010110): #STOR M(Q)
        (memory[MAR])=MQ
        print("output is", memory[MAR])


    IR=(IBR>>12)
    MAR=(IBR)%(0b1<<12)
    print(f"NEW IR IS ", IR)
    print(f"NEW MaR IS", MAR)
    if(IR==0b00000000): #HALT
    
        print("HALT")
        quit()
    
    elif(IR==0b00000001): #load
        print(f"LOAD ", MAR)
        MBR=memory[MAR]
        AC=MBR
        if(int(AC)<<40):
            print("overflow")
            quit()


    elif(IR==0b00000101): #adding
        AC=int(AC)
        memory[MAR]=int(memory[MAR])
        print("We are adding now")
        AC=AC+memory[MAR]
        if(AC>2**40):
            print("overflow")
            quit()


    elif(IR==0b00000110): #subtracting
        AC=int(AC)
        memory[MAR]=int(memory[MAR])
        print("we are subtracting now")
        AC=AC-memory[MAR]
        if(AC>>40==1):
            print("overflow")
            quit()


    elif(IR==0b00100001): #STOR M(X)
        print("MAR IS ", MAR)
        memory[MAR]=AC


    elif(IR==0b00001011): #multiply
        MBR=int(memory[MAR])
        MBR=MBR*MQ
        if(MBR>2**80):
            print("overflow")
            quit()        
        AC=MBR>>40
        MQ=MBR%(1<<40)


    elif(IR==0b00010000): #STORE
        MBR=AC
        memory[MAR]=MBR
        print(f"output is", memory[MAR])


    elif(IR==0b00001001): #LOAD M(x) onto MQ
        MBR=memory[MAR]
        MQ=int(MBR)


    elif(IR==0b00001010): #transfering contents of MQ to AC
        AC=MQ
        print(f"output is", AC)


    if(IR==0b00001101): #JUMP
        AC=memory[0]
        execute(memory[MAR],memory)


    elif(IR==0b00001100): #divison
        memory[MAR]=int(memory[MAR])
        AC=int(AC)
        quotient=AC//(memory[MAR])
        remainder=AC%(memory[MAR])
        AC=remainder 
        MQ=quotient

    print(f"PC is", PC)
    PC=PC+1 
memory=list(range(1000))
for i in range(1000):

    memory[i]=0

print("\n 1 --> Simple Addition of 10 numbers\n 2 --> Simple Subtraction (1st Number - 2nd Number)\n 3 --> Simple Multiplication\n 4-->finding the minimum of two numbers using jump \n 5-->Divison of two numbers")
choice=int(input("Tell us what you wanna do: "))
if (choice==1): #addition

    memory[0]=(input("Number 1: "))
    memory[1]=(input("Number 2: "))
    memory[2]=(input("Number 3: "))
    memory[3]=(input("Number 4: "))
    memory[4]=(input("Number 5: "))
    memory[5]=(input("Number 6: "))
    memory[6]=(input("Number 7: "))
    memory[7]=(input("Number 8: "))
    memory[8]=(input("Number 9: "))
    memory[9]=(input("Number 10: "))
    execute(0b0000000100000000000000000101000000000001,memory) #LOAD M(0) ADD M(1)
    execute(0b0000010100000000001000000101000000000011,memory) #ADD M(2) ADD M(3)
    execute(0b0000010100000000010000000101000000000101,memory) #ADD M(4) ADD M(5)
    execute(0b0000010100000000011000000101000000000111,memory) #ADD M(6) ADD M(7)
    execute(0b0000010100000000100000000101000000001001,memory) #ADD M(8) ADD M(9)
    execute(0b0010000100000000101000000000000000000000,memory) #STOR M(10) HALT 

if (choice==2): #subtraction
    memory[0]=input("Number 1 is ")
    memory[1]=input("Number 2 is ")
    execute(0b0000000100000000000000000110000000000001,memory) #LOAD M(0) SUB M(1)
    execute(0b0010000100000000001000000000000000000000,memory) #STOR HALT
if (choice==3): #multiplication
    memory[0]=input("Number 1: ")
    memory[1]=input("Number 2: ")
    execute(0b0000100100000000000000001011000000000001,memory) #LOAD MQ,M(0)  MUL M(1)
    execute(0b0000101000000000000000000000000000000000,memory) #LOAD MQ HALT
if (choice==4): #find the minimum of two numbers
    memory[0]=input("Number 1: ")
    memory[1]=input("Number 2: ")
    memory[2]=0b0010000100000000001000000000000000000000 #STOR M(1) HALT
    memory[3]=0b0010000100000000000000000000000000000000 #STOR M(0) HALT
    execute(0b0000000100000000000000000110000000000001,memory) #LOAD M(0) subtract M(1)
    execute(0b0000111100000000001100001101000000000011,memory)#JUMP + M(X,0:19) #STORE M(0)
if(choice==5): #division of 2 numbers
    memory[0]=input("Number 1: ")
    memory[1]=input("Number 2: ")
    execute(0b0000000100000000000000001100000000000001,memory) #LOAD M(0) div M(1) 
    execute(0b0001011000000000001000000000000000000000,memory) #STOR MQ onto M(X) HALT


    # 0b00000000; --> HALT
    #  0b00001010; --> LOAD MQ
    #  0b00001001; --> LOAD MQ,M(X)
    #  0b00100001; --> STOR M(X)
    #  0b00000001; --> LOAD M(X)
    #  0b00000010; --> LOAD -M(X)
    #  0b00000011; --> LOAD|M(X)|
    #  0b00000100; --> -LOAD|M(X)|
    #  0b00001101; --> JUMP M(X,0:19)
    #  0b00001110; --> JUMP M(X,10:39)
    #  0b00001111; --> JUMP + M(X,0:19)
    #  0b00010000; --> JUMP + M(X,20:39)
    #  0b00000101; --> ADD M(X)
    #  0b00000111; --> ADD |M(X)|
    #  0b00000110; --> SUB M(X)
    #  0b00001000; --> SUB |M(X)|
    #  0b00001011; --> MUL M(X)
    #  0b00001100; --> DIV M(X)
    #  0b00010100; --> LSH
    #  0b00010101; --> RSH

        





