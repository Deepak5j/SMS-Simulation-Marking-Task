### This is Regarding given code (page 5, 6) 
### mycomments starts with triple hash (###)

# An SMS Simulation class SMSMessage(object):
### this is wrong way of declaring variables in same line. If you  want to declare variables in same line.
### then use samecolon like to saperate each vaiables. eg as follows
### hasBeenRead = False; messageText = text; fromNumber = number
### best way is to declare each new variables in new line  
hasBeenRead = False messageText = text fromNumber = number
def __init__(self,hasBeenRead,messageText,fromNumber):
    ### initialiation of class variable is wrong
    ### text and number is undefine. Use constant values
    self.hasBeenRead = False self.messageText = text self.fromNumber = number

### class methods must be defined inside the class block
def MarkASRead(self):
    if userChoice == read:
        self.hasBeenRead = True

### all the methods which is required for class, should be define inside the class
### rest can be define outside the class
### check main.py code for definitions of these methodds
def add_sms():
def get_count():
def get_message():
def get_unread_messages():
def remove():

### undefine SMSMessage error because of class is not defined.
### before line no 9, class SMSMessage should be defined to fix this error.
no_1 = SMSMessage(False, "Hello", "0798653452")
no_2 = SMSMessage(False, "WYD", "0845673864")
no_3 = SMSMessage(False, "How are you?", "0631873298")

### again variables are seperated by semicolon, or define then in seperate lines
SMSStore = [] userChoice = ""

### check main.py for detailed code for following
while userChoice != "quit":
    ### raw_input() is not used in python3
    ### use inout()
    userChoice = raw_input("What would you like to do - read/send/quit?")
    if userChoice == "read":
        # Place your logic here elif userChoice == "send": # Place your logic here elif userChoice== "quit":
        print("Goodbye")
    else:
        print("Oops - incorrect input")