def leap_year(year):
    if year%400 == 0 or (year%4 == 0 and year %100 !=0):
        print(year," is a leap year")
    else:
        print(year , " is not a leap year")

year = int(input("Enter a year: "))
leap_year(year)        
