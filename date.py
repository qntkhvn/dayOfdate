# Name: Quang Nguyen
# File: date.py
# Desc: Determines the day of the week from the date

def isLeapYear(year): # Leap year function
    return (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0) 

def dayOfdate(): # main function
    
    # Ask-before-iterating loop  
    again = "y"
    while (again == "y") or (again == "Y"):
        
        dateStr = input("\nEnter a date (mm/dd/yyyy): ")  # Get the date
        monthStr, dayStr, yearStr = dateStr.split("/")  # Split date into string and integer components
        year = int(yearStr)
        day = int(dayStr)
        month = int(monthStr)
        
        # Convert monthStr to monthName
        months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
        monthName = months[int(monthStr)- 1] 
        
        print("The converted date is: ", monthName, dayStr + ",", yearStr) # Display the date in Month DD, YYYY format

        first = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334] # List the number of days before the first of each month
        
        # Compute the ordinal day number for the year
        ordinal = first[month - 1] + day
        if (isLeapYear(year)) and (month > 2):
            ordinal = ordinal + 1
        print("It is day {0} of the year".format(ordinal)) # Display the ordinal day number for the year

        # Calculate jan1Ordinal
        a = (year - 1901) % 28
        b = a // 4
        jan1Ordinal = (2 + a + b) % 7 + 1
        
        dayWeekOrdinal = ((ordinal - 1) + (jan1Ordinal - 1)) % 7 + 1 # Determine the ordinal position of the day within the week     

        # Convert dayStr to dayName
        days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
        dayName = days[int(dayWeekOrdinal)- 1]
        print("It is a", dayName) # Display the day of the week

        again = input("\nAgain? (y/n): ") # Ask whether to continue or not

dayOfdate() 
