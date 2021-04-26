#1: decoupling: divide the program into many different modules so  you can fix problem without affecting the others
#2: Define others function: "return" the value of elements from "main"
#3: return -1: Wrong input
#4: Change the type of variable: change in "main"
#5: Constant: Upper letters
#6: Contant variale is already a integer
#7: function muss be defined
#8: Output takes the other output and  also input
#9: "Main: call the funcions" ; "Other functions: calculation"
#10: Because in calc_total_price: all the type of element is already changed in "main"
#11: Compare the definition of "return 1" to print the value 
#12: Call the new function -> return  to print it in "main"
#13: def "cal_total_price" do first to defind variable in "main"
#14: if change the type of APPLE_PRICE to str -> change the other element
########## main: Input + Output ; Other functions: calculation ########
 

def calc_total_price(apple_weight, APPLE_PRICE): #13
	return apple_weight * APPLE_PRICE  #2

def calc_return(total_price, monney_given): #13
	if monney_given < total_price:
		return -1 #2
	return monney_given - total_price #2

def print_return_info(total):
	count_500 = int(total/500)
	total = total - 500*count_500
	if total != 0:
		print("500: " + str(count_500))

	count_200 = int(total/200)
	total = total - 200*count_200
	if total != 0:
		print("200: " + str(count_200))

	count_100 = int(total/100)
	total = total - 100*count_100
	if total !=0:
		print("100: " + str(count_100))

	count_50 = int(total/50)
	total = total - 50*count_50
	if total != 0:
		print("50: " + str(count_50))

	count_20 = int(total/20)
	total = total - 20*count_20
	if total != 0:
		print("20: " + str(count_20))

	count_10 = int(total/10)
	total = total  - 10*count_10
	if total != 0:
		print("10: " + str(count_10))	

	count_1 = total
	print("1: " + str(int(count_1)))


def main():
	APPLE_PRICE = 21 #5
	apple_weight = input("Enter the weight: ")
	monney_given = input("Enter the money: ")

	apple_weight = float(apple_weight) #4
	monney_given = float(monney_given) #4 


	total_price = calc_total_price(apple_weight, APPLE_PRICE) #8
	total_money_return = calc_return(total_price, monney_given) #9 

	print("total price: " + str(round(total_price)))

	if total_money_return == -1:
		print("Not enough cash")
	else:
		print("You need to return to customer: " + str(total_money_return))
		print_return_info(total_money_return) #12


main()	