'''
import numpy as np

import calendar
dict={}
while(True):
    num = random_numbers = np.random.random(5)
    print("Are you looking for :\n1.change the plan\n2.purchage the plan ")
    enter=int(input())
    print("did you like to purchase the 1.yearly plan(1200)\n 2.premium plan(2400)")
    if enter==2:
        print("did you like to purchase the 1.yearly plan(1200)\n 2.premium plan(2400)")
        plan=int(input())
        print("may i know your name please : ")
        name_of_customer=input()
        dict[name_of_customer]=[num,plan]
        if plan==1:
            print("thank you for purchasing the yearly plan")
        else:
            print("thank you for purchasing the premium plan")
    if enter==2:
        print("may i know your name please : ")
        name_of_customer=input()
        if name_of_customer in dict:
            if dict[name_of_customer][1]==1:
                month=dict[name_of_customer][0]
                print("your plan is yearly plan ",calendar.month_name[month],"2024" )
                how_many_months=(5-month)*100-1200
                print("your balance amount to pay is ",how_many_months-2400)
                print("your plan is changed to premium")
            if dict[name_of_customer][1]==2:
                month=dict[name_of_customer][0]
                print("your plan is premium plan ",calendar.month_name[month],"2024" )
                how_many_months=(5-month)*200-2400
                print("now your premium plan is changed to yearly")

                
        else:
            print("your name is not in our data base you canot change the plan")
            exit(0)
    print("do you want to continue :\n 1. yes\n 0. no")
    cont=int(input())
    if cont == 0:
        break


        
    print("thank you for choosing us")'''

import numpy as np
import calendar
print("this is for the jan 2024 plan")
# Initialize the dictionary to store customer data
customer_data = {}

while True:
    # Generate a random month index between 1 and 12
    month_index = np.random.randint(1, 6)
    
    print("Are you looking for :\n1. Change the plan\n2. Purchase the plan")
    enter = int(input())
    
    if enter == 2:
        print("Would you like to purchase the\n1. Yearly plan (1200)\n2. Premium plan (2400)")
        plan = int(input())
        print("May I know your name, please?")
        customer_name = input()
        
        # Store the customer data
        customer_data[customer_name] = [month_index, plan]
        
        if plan == 1:
            print("Thank you for purchasing the yearly plan")
        else:
            print("Thank you for purchasing the premium plan")
    
    elif enter == 1:
        print("May I know your name, please?")
        customer_name = input()
        
        if customer_name in customer_data:
            month_index, current_plan = customer_data[customer_name]
            month_name = calendar.month_name[month_index]
            
                        
            if current_plan == 1:
                # Yearly plan to Premium plan
                print(f"Your plan is a yearly plan starting in {month_name} 2024.")
                months_remaining = 12 - month_index + 1
                balance_amount = months_remaining * 100
                amount_to_upgrade = 2400 - balance_amount
                if amount_to_upgrade > 0:
                    print(f"Your balance amount to pay is {amount_to_upgrade} to upgrade to the premium plan.")
                else:
                    print(f"Your remaining amount of {-amount_to_upgrade} is added to your wallet. You can use this amount in your next plan.")
                print("Your plan is changed to premium.")
                customer_data[customer_name][1] = 2
            elif current_plan == 2:
                # Premium plan to Yearly plan
                print(f"Your plan is a premium plan starting in {month_name} 2024.")
                months_remaining = 12 - month_index + 1
                balance_amount = months_remaining * 200
                amount_to_downgrade = 2400 - balance_amount
                if amount_to_downgrade > 0:
                    print(f"Your balance amount to pay is {amount_to_downgrade} to downgrade to the yearly plan.")
                else:
                    print(f"Your remaining amount of {-amount_to_downgrade} is added to your wallet. You can use this amount in your next plan.")
                print("Your plan is changed to yearly.")
                customer_data[customer_name][1] = 1

        else:
            print("Your name is not in our database. You cannot change the plan.")
    
    else:
        print("Invalid option selected.")
    
    print("Do you want to continue?\n1. Yes\n0. No")
    cont = int(input())
    
    if cont == 0:
        print("Thank you for choosing us!")
        break
