# print(150 *0.12 +150)
#print(150 * 1.12 / 5 )   # short hand
# 150 dollar with 12 persent tip it become a 168 dollar

# 12/100 = 0.12
# print(150 *0.12) = 18
#  Now rounding numbers upto two decimal places

print("Welcome to the tip calculator!") # Exclamation mark

#  If you creating areally enthusiastic calculator replace the full stop with the exclamation mark

bill = float(input("What was the total bill? $"))  # previously we getting input type as a str that's
# now we ued float
tip = int(input("Whats percentage would you like to give? 10 12 or 15"))
people = int(input("How many people to split the bill? "))
bill_with_tip = tip / 100 * bill + bill
# bill_with_tip2 = bill * (1 + tip / 100) same result
print(bill_with_tip)


# tip_as_persent = tip/100
# total_tip_amount = bill * tip_as_persent     same
# total_bill = bill + total_tip_amount
# bill_per_person = total_bill / people
# final_amount = round(bill_per_person)
# print(f"Each person should pay: ${final_amount}")
