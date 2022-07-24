import random
import time


class RemoteController():
    def __init__(self,TV_Status = "OFF", TV_Volume = 0, Channel_List = ["BBc1"], Channel_Name = "BBC1"):

        print("Creatinf a remote controller...")
        self.TV_status = TV_Status
        self.TV_Volume = TV_Volume
        self.Channel_List = Channel_List
        self.Channel_Name = Channel_Name

    def Power(self):
        if self.TV_status == "ON":
            print("TV is ON")

        else:
            print("TV is turning ON")
            self.TV_status == "ON"

    def PowerOff(self):
        if self.TV_status == "OFF":
            print("TV is OFF")
        else:
            print("TV is turning OFF")
            self.TV_status = "OFF"


    def Volume(self):
        while True:

            answer = input("Volume down: '-' \nVolume up: '+' \nExit: 'Exit'")

            if answer == "-":
                if self.TV_Volume !=0 :
                    self.TV_Volume -=1
                    print("Volume: ", self.TV_Volume)

                elif answer == "+":
                    if self.TV_Volume != 50:
                       self.TV_Volume +=1
                       print("Volume: ", self.TV_Volume)

                else:
                    print("The sound level has updated")
                    break

    def AddChannel(self,Channel_Name):

        print("Adding channel...")
        time.sleep(1)
        self.Channel_List.append(Channel_Name)
        print("Channel added...")

    def RandomChannel(self):
        Random = random.randint(0,len(self.Channel_List)-1)

        self.Channel_Name = self.Channel_List[Random]

        print("You are watching: ",self.Channel_Name)

    def __len__(self):
        return len(self.Channel_List)

    def __str__(self):
        return "TV Status: {} \nTV Volume: {} \nChannel List: {} \nWatching Channel: {}".format(self.TV_status,self.TV_Volume,self.Channel_List,self.Channel_Name)


RM1 = RemoteController()
print("""

1. Turn ON TV
2. Turn OFF TV
3. Volume
4. Add Channel
5. Number of channel
6. Open Random Channel
7. TV info 

For Exit pres Q

""")

while True:


    opr = input("Chose the operation that you want")

    if opr == "Q":
        print("Program closing..")
        break

    elif opr == "1":
        RM1.Power()

    elif opr == "2":
        RM1.PowerOff()

    elif opr == "3":
        RM1.Volume()

    elif opr == "4":
        chname = input("Enter a Channel name")
        chlist = chname.split(",")

        for i in chlist:
            RM1.AddChannel(i)

    elif opr == "5":
        print("Number of channels: ",len(RM1))

    elif opr == "6":
        RM1.RandomChannel()

    elif opr == "7":
        print(RM1)

    else:
        print("Invalid operations!")





