# Monthly budget planner 

print("********************************Monthly Budget****************************")


income = float(input("input your income £"))
additional = float(input("enter any side hustles £"))

total_income= income + additional

print("total income= £"+str(total_income))

def gather_expenses():
    rent = float(input("input your rent: £ "))
    phone_bill= float(input("input your Phone bill: £ "))
    Wifi= float(input("input your Wifi bills: £ "))
    Transportation = float(input("input your Total transport cost: £ "))
    Gym_membership = float(input("input your Gym member cost: £ "))
    total_expenses = rent + phone_bill + Wifi + Transportation +Gym_membership
    return total_expenses

expenses_total = gather_expenses()  
print ("Expenses total to £ "+ str(expenses_total))

Margin = total_income - expenses_total

percentage_margin = (expenses_total/total_income) * 100
expected_margin = (total_income/2) 

if Margin >=0:
    print("Total Surplus for the month will be £" + str(Margin))
else:
    print ("You will be £" +str(Margin)+" Negitive")

if percentage_margin <= 50:
    print("Your Bills compared to your income are in the right level at %"+str(percentage_margin)+" of your Income.")
else:
    neg = expenses_total - expected_margin
    print("Your Bills are too high at % "+str(percentage_margin)+" of your income. Should be £" +str(expected_margin)+" per month and you use £"+str(expenses_total)+". take off or make £"+str(neg)+".") 
    print("MAKE MORE MONEY!")

print("*****************Finito*************************")