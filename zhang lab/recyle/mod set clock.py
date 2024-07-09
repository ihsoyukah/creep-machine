#function to set real time clock
#ask prof what we're supposed to do with the time

def set_clock():
    date=input("Please enter the time (MM DD YYYY): ")
    if len(date) == 10 and date[0:2].isdigit() and date[3:5].isdigit() and date[6:].isdigit() and date[2] == ' ' and date[5] == ' ':
        time=input("Please enter the time in 24 hour format (HH:MM:SS): ")
        time_parts = time.split(':')      
        if len(time_parts) == 3:
            hours, minutes, seconds = time_parts
            if hours.isdigit() and minutes.isdigit() and seconds.isdigit():
                hours = int(hours)
                minutes = int(minutes)
                seconds = int(seconds)
            else:
                time=input("Please use the correct format to enter the time (HH:MM:SS): ")  
            if 0 <= hours < 24 and 0 <= minutes < 60 and 0 <= seconds < 60:
                print(date, time) #this is the corect format
            else:
                time=input("Please use the correct format to enter the time (HH:MM:SS): ") 
        else:
            time=input("Please use the correct format to enter the time (HH:MM:SS): ") 
    else:
        #date=input("Please use the correct format to enter the date (MM DD YYYY): ")
        set_clock()
                    
		
#m ake separate functions to ask for the time and the date 
set_clock()


        

