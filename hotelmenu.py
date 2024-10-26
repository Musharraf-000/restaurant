# USED TOPICS OF PYTHON IN THIS CODE.
# 1) dictionary
# 2) escape sequence character
# 3) user input
# 4) if-elif-else conditional statement
# 5) formatted String
# 6) for loop
# 7) while loop
# 8) break statement
# 9) l.just() - to fixe length
# 10) \t - for space

# AUTHOR : MUSHARRAF KHAN



menu = {
    'water'     : 20,
    'tea'       : 10,
    'coffee'    : 20,
    'biryani'   : 80,
    'tahari'    : 70,
    'nan_kalya' : 100
}

total_bill = 0
bill_detail = {}

print("WELCOME TO AURANGABAD RESTAURANT.\nHERE'S THE MENU: ")
for key in menu:
    print(key.ljust(9),":",menu[key])

while True:
  order = input("please enter the order : or type done to end : ")
  if order == "done":
   print("thank's for visit.")
   break
  elif order in menu:
    quantity = int(input("enter order quantity : "))
    bill_detail[order] = quantity

  else:
    print("please enter correct item.\nsorry this item are not available!")

for item in bill_detail:
  item_cost = bill_detail[item]*menu[item]
  total_bill += item_cost
  print(f"{item.ljust(9)}\t{bill_detail[item]}\t{item_cost}")

print("total bill :",total_bill)
print("total bill with GST :",total_bill + ((18/100)*total_bill)) 




    
