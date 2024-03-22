import pyttsx3

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 185)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

if __name__ == "__main__":
    print("Welcome To your personal ATM.")
    speak("Welcome To your personal ATM. How would you like to proceed?")
    

class ATM:
    def __init__(self):
        self.pin = ""
        self.balance = 0
        self.menu()

    def menu(self):
            user = input("""How would you like to proceed?
                            1. Enter 1 to create a pin
                            2. Enter 2 to deposit your amount
                            3. Enter 3 to withdraw
                            4. Enter 4 to check balance
                            5. Enter 5 to Exit 
                Enter your number for  process: """)

                                
            if user == "1":
               self.create_pin()
            elif user == "2":
               self.deposit()  
            elif user == "3":
               self.withdraw() 
            elif user == "4":
               self.check_balance()
            elif user == "5":
               print("Thank You for using ATM. Have a Good Day!")
               speak("Thank You for using ATM. Have a Good Day!")
               return
            else:
                print("Invalid entry")


            self.menu()
            

    def create_pin(self):
        speak("Enter your pin")
        password = input("Enter your pin: ")
        self.pin = password
        print("Pin set successfully")
        speak("Pin set successfully")


    def deposit(self):
        speak("Enter your pin")
        temp = input("Enter Your pin : ")
        if temp == str(self.pin):
            speak("Enter the Amount you wany deposit")
            amount = int(input("Enter the amount you want deposit : ")) 
            self.balance = amount + self.balance
            print("Deposit successfully")
            speak("Deposit successfully")
        else:
            print("Invalid Pin") 
            speak("Invalid Pin")    


    def withdraw(self):
        speak("Enter your pin")
        temp = input("Enter your pin : ")              
        if temp == str(self.pin):
            speak("Enter the amount to withdraw : ")
            amount = int(input("Enter the Amount to withdraw : "))
            if self.balance >= 100:
                if amount <= self.balance:
                    self.balance = self.balance - amount
                    print("Withdraw Succeessfully")
                    speak("Withdraw Succeessfully")
            else:
                print("Insufficient amount")  
                speak("Insufficient amount")  
        else :
            print("Invalid pin")
            speak("Invalid pin")   

            


    def check_balance(self):
        speak("Enter your PIN")
        entered_pin = input("Enter your PIN: ")
        if entered_pin == self.pin:
            print("Your current balance is " , self.balance)
        else:
            print("Invalid PIN.")
            speak("Invalid PIN.")
          
obj = ATM()
