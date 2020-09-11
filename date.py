# Name: Quang Nguyen
# File: date.py
# Desc: Determines the day of the week from the date

# Leap year function
def isLeapYear(year):
    return (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0) 

def dayOfdate():
    
    # Ask-before-iterating loop  
    again = "y"
    while (again == "y") or (again == "Y"):

        # Get the date    
        dateStr = input("\nEnter a date (mm/dd/yyyy): ")
        
        # Split date into string and integer components
        monthStr, dayStr, yearStr = dateStr.split("/")
        year = int(yearStr)
        day = int(dayStr)
        month = int(monthStr)
        
        # Convert MonthStr to monthName
        months = ["January", "February", "March", "April",
                  "May", "June", "July", "August", "September",
                  "October", "November", "December"]
        monthName = months[int(monthStr)- 1]
        
        # Display the date in month day, year format
        print("The converted date is: ", monthName, dayStr + ",", yearStr)

        # List the number of days before the first of each month
        first = [0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334]
        
        # Compute the ordinal day number for the year
        ordinal = first[month - 1] + day
        if (isLeapYear(year)) and (month > 2):
            ordinal = ordinal + 1

        # Display the ordinal day number for the year
        print("It is day {0} of the year".format(ordinal))

        # Calculate jan1Ordinal
        a = (year - 1901) % 28
        b = a // 4
        jan1Ordinal = (2 + a + b) % 7 + 1

        # Determine the ordinal position of the day within the week     
        dayWeekOrdinal = ((ordinal - 1) + (jan1Ordinal - 1)) % 7 + 1

        # Convert dayStr to dayName
        days = ["Sunday", "Monday", "Tuesday", "Wednesday",
                "Thursday", "Friday", "Saturday"]
        dayName = days[int(dayWeekOrdinal)- 1]

        # Display the day of the week
        print("It is a", dayName)

        # Ask whether to continue or not
        again = input("\nAgain? (y/n): ")

dayOfdate() 
