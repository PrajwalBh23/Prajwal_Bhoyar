print("\n############################################")
print("\n######## WELCOME TO HOTEL RAJESHAHI ########")
print("\n############################################\n")

name="Y"  ## For while continuty
total=0
no=1
i=1
j=0
arr=[0]*10    # --> for quantity saving
quantityM=0
quantityR=0
quantityS=0
quantitySWEET=0


while(name=="Y"):
	print("\n\t\tRajesahi Menu\n")
	print("\n   Dishes\t\tPrice/-\n")
	print("\n1.Maharashtraian Tali \t60 \n2.Rajestani Tali \t70\n3.IDLI DOSA\t\t50\n4.Sweets\t\t60\n")
	give=int(input("\nEnter the dish number\t:"))
	quantity=int(input("\nEnter the quantity\t:"))
	
	if(give==1):
		bill=60*quantity
		arr[0]=arr[0]+quantity
		quantityM=arr[0]
	elif(give==2):
		bill=70*quantity
		arr[1]=arr[1]+quantity
		quantityR=arr[1]
	elif(give==3):
		bill=50*quantity
		arr[2]=arr[2]+quantity
		quantityS=arr[2]
	elif(give==4):
		bill=60*quantity
		arr[3]=arr[3]+quantity
		quantitySWEET=arr[3]
	else:
		print("\nInvalid Input....\n")
		
	no+=1
	total=total+bill
	
	name=input("\nDo your want choose Y/N\t:")
print("--------------------------------------------------")
print("\n\t\t Bill Details\n")
print("--------------------------------------------------")
print("\n  Dish\t\t       Qty    Price    Value\n")
print("--------------------------------------------------")

if(total>100 and total<200):
	discount=0.05*total
elif(total>200 and total<500):
	discount=0.07*total
elif(total>500):
	discount=0.10*total
else:
	discount=0

if(quantityM!=0):
    print("Maharashtraian Tali\t"+str(quantityM)+"  x  60"+"\t"+str(quantityM*60))
if(quantityR!=0):
    print("\nRajasthani Tali\t\t"+str(quantityR)+"  x  70"+"\t"+str(quantityR*70))
if(quantityS!=0):
    print("\nSouth Indian\t\t"+str(quantityS)+"  x  50"+"\t"+str(quantityS*50))
if(quantitySWEET!=0):
    print("\nSweet\t\t\t"+str(quantitySWEET)+"  x  60"+"\t"+str(quantitySWEET*60))
    
round_discout = round(discount, 3)
print("\n-----------------------------------------------\n")
print("Bill\t\t\t\t\t"+str(total))
print("Discount\t\t\t\t"+str(- round_discout))
print("\n-----------------------------------------------\n")
print("Total Bill\t\t\t\t"+str(total-discount))
print("\n-----------------------------------------------\n")