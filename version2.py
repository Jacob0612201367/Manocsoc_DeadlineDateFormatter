from datetime import date
import calendar

event = input("Enter event title: ")
year = int(input("Enter year: "))
month = int(input("Enter month: "))
day = int(input("Enter day: "))

event_date = date(year, month, day)

print("\nFormatted Output:")
print("Event:", event.upper())
print("Date:", event_date.strftime("%B"), day, ",", year)
print("Year:", year)
print("Month:", calendar.month_name[month])
print("Day:", day)
print("Weekday:", event_date.strftime("%A"))
