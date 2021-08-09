available= 100
# input from user
user_need=int(input("How many Chocolate do you want???"))
i=1
#Main loop for print no. of canddy 
while i<=user_need:
#To get stock after each itration 
  stock=i-available
  if i>available:
    print("out stock")
    break
  i+=1
# To print stock
if stock<0:
  print(abs(stock),"item left")
