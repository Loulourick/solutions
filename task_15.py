def days_in_month(month, year):
    if month in [1,3,5,7,8,10,12]:
        return 31
    elif month in [4,6,9,11]:
        return 30
    elif month == 2:
        god = (year % 4 == 0  and year % 100 != 0) or (year % 400 == 0)
        if god:
            return 29
        else:
            return 28
if __name__ == "__main__":
    print (days_in_month(1, 2001))
    print (days_in_month(2, 2001))
    print (days_in_month(2, 2000))
    print (days_in_month(2, 1900))
    print (days_in_month(11, 2025))
