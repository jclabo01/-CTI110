# Jeffrey Clabo
 # 3/19/2026
 # P2HW2
 # change counter

change = float (input ("enter an amount of money : $") )

change = int (change * 100)


num_dollars = change // 100
change = change - (num_dollars * 100)

num_quarters = change // 25
change = change - (num_quarters * 25)

num_dimes = change // 10
change = change - (num_dimes * 10)

num_nickels = change // 5
change = change - (num_nickels * 5)

num_pennies = change // 1
change = change - (num_pennies * 1)

if num_dollars > 0:
     if num_dollars == 1:
        print (f"{num_dollars} Dollar ")
     else: 
        print (f"{num_dollars} Dollars ")


if num_quarters > 0:
     if num_quarters == 1:
        print (f"{num_quarters} quarter ")
     else: 
        print (f"{num_quarters} quarters ")


if num_dimes > 0:
     if num_dollars == 1:
        print (f"{num_dimes} Dime ")
     else: 
        print (f"{num_dimes} Dimes ")

if num_nickels > 0:
     if num_nickels == 1:
        print (f"{num_nickels} Nickel ")
     else: 
        print (f"{num_nickels} Nickels ")

if num_pennies > 0:
     if num_pennies == 1:
        print (f"{num_pennies} Pennie ")
     else: 
        print (f"{num_pennies} Pennies ")







