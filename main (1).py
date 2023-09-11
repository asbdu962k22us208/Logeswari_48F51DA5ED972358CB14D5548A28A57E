# to find leap year or not leap year

def checkleap(year):
  if((year%400==0)or 
    (year%100!=0)and   
     (year%4==0)):
    print("given is a leap year")
  else:
    print("given year is not a leap year")
year=int(input("enter the number"))
checkleap(year)