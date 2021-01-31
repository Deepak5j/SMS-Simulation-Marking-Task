# check old-Code-Analysis.py for feedback of your code
# An SMS Simulation class SMSMessage(object)
class SMSMessage:
    #class variables initialized with default value
    hasBeenRead = False
    messageText = "text" 
    fromNumber = 12345

    #for initializing object
    def __init__(self, hasBeenRead, messageText, fromNumber):
        self.hasBeenRead = hasBeenRead
        self.messageText = messageText 
        self.fromNumber = fromNumber

    #this method called under "read" choice
    def MarkASRead(self):
        self.hasBeenRead = True
        print('Message marked as read!!')
    
    #this method called under "read" choice
    def get_message(self): 
        print('Next Message: ', self.messageText)

#used to initialising SMSStore 
def add_sms(smsList): 
    global SMSStore 
    SMSStore = smsList

#gives counts of messages inside SMSStore
def get_count(): 
    global SMSStore
    return len(SMSStore) 

#this method called under "read" choice
#return unreaded sms
def get_unread_messages(): 
    global SMSStore
    tmp = []
    for i in SMSStore:
        if(not i.hasBeenRead):
            tmp.append(i)
    return tmp

#delete sms object from SMSStore
def remove(a):
    global SMSStore
    SMSStore.remove(a)

#defining SMSMessage objects
no_1 = SMSMessage(False, "Hello", "0798653452")
no_2 = SMSMessage(False, "WYD", "0845673864")
no_3 = SMSMessage(False, "How are you?", "0631873298")

#defining container for storing SMSMessage object
SMSStore = [] 

#this variables not required
userChoice = ""

#adding SMSMessage objedcts to container
add_sms([no_1, no_2, no_3])

while userChoice != "quit":
    #there are 3 chice given to user read, send, quit
    userChoice = input("What would you like to do - read/send/quit ? :")
    if userChoice == "read":
        print()
        #get tha unreaded message
        unread = get_unread_messages()
        #get count of unreaded messages, used for looping purpose 
        messageCount = len(unread)
        messageCounttmp = messageCount
        print('Total unreaded message: ', messageCount)
        #True is used as infinte loop but breaking condition is defined on "messageCount" at very begening
        #and "messageCount" is decreasing, it's fail safe
        while True:
            #loop breaking condition
            if messageCount == 0:
                break
            #shows message
            unread[messageCounttmp-messageCount].get_message()
            #asking user if want to mark as read or skip, or quit from "read"
            inp = input('Want to mark message ' + str(messageCounttmp-messageCount) + ' as read - yes/no/quit ? :')
            if inp == 'yes':
                #mark message as read, this will declrease count of unreaded message
                unread[messageCounttmp-messageCount].MarkASRead()
                messageCount -= 1
            elif inp == 'no':
                #skiping message, doesn't mark as read, decreasing count for moving to next message
                messageCount -= 1
            elif inp == 'quit':
                #quit from "read" choice
                break
            else:
                #showing user yes/no/quit allowed choice
                print('Wrong choice, try again')
        #shows total left number of unreaded messages
        print('Total unreaded message left: ', len(get_unread_messages()))          
        print()     
        #print("Goodbye")
    
    elif userChoice == "send":
        print()
        #get count of total message object
        messageCount, i = get_count(), 0
        print('Total message count: ', messageCount)
        #looping system same as in "read" choice
        while True:
            if messageCount == 0:
                break
            #showing message
            SMSStore[get_count()-messageCount].get_message()
            inp = input('Want to send message ' + str(get_count()-messageCount) + ' - yes/no/quit ? :')
            if inp == 'yes':
                #this will remove messge object from container SMSStore
                remove(SMSStore[get_count()-messageCount])
                messageCount -= 1
                print('Message send!!')
            elif inp == 'no':
                #skiping message from deletion
                messageCount -= 1
            elif inp == 'quit':
                #quit from "send" choice
                break
            else:
                print('Wrong choice, try again')
        #shows total number of left messages in the container SMSStore
        print('Total message left: ', get_count())     
        print()     

    #this choice is useless as inside the while, "quit" is used
    #you can use "True" in place of "quit" for while test condition
    #then thsi choice will useful
    elif userChoice == "quit":
        exit()

    #default response, if wrong input given by user    
    else:
        print("Oops - incorrect input")