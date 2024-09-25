#Write a program called 'printmonth.py' that asks the user for a month name and start day and then prints the calendar for that month in a 6 row by 7 column grid

#Lwazi Somtsewu
# 22 August 2024
month= input("Enter the name of a month (e.g. January, ..., December):\n")
start_day= (input("Enter the start day (1 for Monday, ..., 7 for Sunday):\n"))

if (not month in ('January','February','March','April','May','June','July','August','September','October','November','December')) or (start_day < 1) or (start_day > 7):
    print('Invalid calendar: you have either entered an incorrect month name or start day.')
    exit()

print(month)
print('Mo Tu We Th Fr Sa Su')

if month in ('January','March','May','July','August','October','December'):
    max_days = 31
elif month == 'February':
    max_days = 28
    print()
else:
    max_days = 30
    
counter = 1

for i in range(6):
    for j in range(1,8):
        if i == 0:
            if j >= start_day:
                if counter > 9:
                    print('{} '.format(counter),end='')
                else:
                    print(' {} '.format(counter),end='')
                counter += 1 
            else:
                print('   ',end='')
        else:
            if counter < max_days+1:           
                if counter > 9:
                    print('{} '.format(counter),end='')
                else:
                    print(' {} '.format(counter),end='')
            else:
                print("",end="")
            counter += 1
   
    print()