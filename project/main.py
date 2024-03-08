from delete_customer import deleteCustomer
from add_customer import addCustomer
from view_customer import viewCustomer
from edit_customer import editCustomer
from add_bill import addBill
from view_bill import viewBill
from add_stock import addStock
from view_stock import viewStock
from delete_stock import deleteStock
from edit_stock import editStock
print("Enter 1 to work with customers ")
print("Enter 2 to work with bills ")
print("Enter 3 to work with stock ")
print("Enter 4 to work with reports ")
choice = int(input("Select anyone from above "))

if choice == 1 :
     # customer 
     print("\n===============================================================\n")
     print("Enter 1 to add customer ")
     print("Enter 2 to delete customer ")
     print("Enter 3 to edit customer ")
     print("Enter 4 to view customer ")
     customer_choice = int(input("Select anyone option from above "))
     if customer_choice == 1 :
          print()
          addCustomer()
          # add customer 
     elif customer_choice == 2 :
          print()
          deleteCustomer()
          # delete customer 
     elif customer_choice == 3 :
          print()
          editCustomer()
          # edit customer 
     elif customer_choice == 4 :
          print()
          viewCustomer()
          # view customer 
     else :
          print("Invalid Choice ")
elif choice == 2 :
     # bills 
     print("\n===============================================================\n")
     print("Enter 1 for add bill ")
     print("Enter 2 for view bill ")
     customer_choice = int(input("Select anyone from above "))
     if customer_choice == 1 :
          print("")
          addBill()
          # add bill
     elif customer_choice ==2 :
          print("")
          viewBill()
          #view bill 
     else:
          print("Invalid Option ")
elif choice == 3 :
     # stock 
     print("\n===============================================================\n")
     print("Enter 1 to add stock ")
     print("Enter 2 to delete stock ")
     print("Enter 3 to edit stock ")
     print("Enter 4 to view stock ")
     customer_choice = int(input("Select anyone option from above "))
     if customer_choice == 1 :
          print()
          addStock()
          # add stock 
     elif customer_choice == 2 :
          print()
          deleteStock()
          # delete stock 
     elif customer_choice == 3 :
          print()
          editStock()
          # edit stock 
     elif customer_choice == 4 :
          print()
          # view stock 
          viewStock()
     else :
          print("Invalid Choice ")
elif choice == 4:
     # reports 
     print("")
else:
     print("Invalid Choice ")