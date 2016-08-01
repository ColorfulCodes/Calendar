"""This is a multiline comment everyone. So we will basically be building a calendar."""

from time import sleep, strftime

USER_FIRST_NAME = raw_input("Hello and Welcome to our calendar. My name is Jaylin, what is yours? ")

calendar = {}

def welcome():
  print "\n"
  sleep(1)
  print "Welcome " + USER_FIRST_NAME + "!"
  sleep(2)
  print "The calendar is opening..."
  sleep(2)
  print "Today is: " + strftime("%A %B %d, %Y")
  sleep(2)
  print "And the time is now " + strftime("%H:%M:%S")
  print "\n"
  sleep(2)
  print "So..."
  print "\n"
  sleep(2)
  print "What would you like to do today?"
  
def start_calendar():
    welcome()
    start = True
    while start:
        user_choice = raw_input("Type A to Add, U to Update, V to view, D to Delete, or X to Exit: ") 
        user_choice = user_choice.upper()
        if user_choice == "V":
            if calendar == len(calendar.keys()) < 1:
                print "Your calendar is empty."
            else:
                print calendar
        elif user_choice == "U":
            date = raw_input("What date? ")
            update = raw_input("Enter the update: ")
            calendar[date] = update
            print "The update was a success!"
            print calendar
        elif user_choice == "A":
            event = raw_input("Enter an event: ")
            date = raw_input("Enter a date (MM/DD/YYYY) ")
            if (len(date) > 10 or int(date[6:]) < int(strftime("%Y"))):
                print "An invalid date has been entered, try again?"
                try_again = raw_input("Y for yes, N for No: ")
                try_again = try_again.upper()
                if try_again == 'Y':
                    continue
                else:
                    start = False
            else:
              calendar[date] = event
              print "The event was successfully added!"
        elif user_choice == "D":
            if len(calendar.keys()) < 1:
                print "your calendar is empty."
            else:
                event = raw_input("What event? ")
                for date in calendar.keys():
                    if event == calendar[date]:
                        del calendar[date]
                        print "The event was successfully deleted."
                    else:
                         print "An incorrect event was specified."
              
        elif user_choice == "X":
            start = False
              
        else:
            print "Invalid Command. Game Over."
                    
start_calendar()
            
            
            
      
  





