import random

def choice():

        optList = []
        tallyList = []
        count = 0
        quit = False
        while quit == False:
                userIn = input("Enter an option, if done type 'esc': ")
                if userIn == 'esc':
                        quit = True
                else:
                        optList.append(userIn)
                        tallyList.append(0)
                        count+=1
        print("You have added "+str(count)+" options")
        size = len(optList)
        if size%2 ==0:
                times = 1001
        else:
                times = 1000
        for j in range(size):
                pos = j+1
                print("Option "+str(pos)+": "+optList[j])

        #times = int(input("How many times would you like to flip (enter large odd number for even number of options, even number for odd options): "))
        for x in range(times):
                random.seed()
                ans = random.randint(1,1000)
                temp1 = 1000/size
                for y in range(size):
                        temp2 = (y+1)*temp1
                        if ans<=temp2:
                                tallyList[y] +=1
                                break


        outPos = 0
        comp = 0
        for i in range(size):
                if comp<= tallyList[i]:
                        comp = tallyList[i]
                        outPos = i
        print("="*10)
        print("You should choose: "+optList[outPos])
        print("="*10)
        print("Scores")
        for k in range(size):
                print(optList[k]+" : "+str(tallyList[k])+"("+str(((tallyList[k]/times)*100))+"%)") 
        print("="*60)
mainExit = True
print("="*50)
print("Hi, I'm InDy, the solution to all your indecision")
print("="*50)
choice()
while mainExit:
        key = input("Would you like to make another decision? (Y/N)")
        if key.upper() == 'Y':
                choice()
        elif key.upper() == 'N':
                quit()
        else:
                print("Please select only 'Y' or 'N'")
