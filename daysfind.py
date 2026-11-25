total_days= int(input("Enter the total number of days: "))
weeks = total_days // 7
remaining_days = total_days % 7
print("There are", weeks,"weeks", "and", remaining_days, "day(s)")