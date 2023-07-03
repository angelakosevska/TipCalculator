print("Welcome to the tip calculator.")

total_bill=input("What was the total bill? $")
tb=float(total_bill)

tip=input("What percentage tip would you like to give? 10, 12, or 15? ")
ttip=int(tip)/100

num_of_people= input("How many people to split the bill? ")
nop=int(num_of_people)

each_person_pays=round((tb/nop)*(ttip)+(tb/nop), 2)
final="{:.2f}".format(each_person_pays)
print(f"Each person should pay: ${final}")
