import datetime

'''
1: Use "main"
2: "While" loop using function
3: change type direct in "input"
4: Muss have "return" to take back the value
5: Just need to have "height_meter" because feet has already calculated with "METER_TO_FEET"
6: Muss: certain order 
7: Defind also in "main"
8: Python is atomatically know the year
9: Function in function
#condense
10: "While" is already fixed the case "wrong type"
import datetime
'''
def ask_yes_no(promt):
	while True: #2: While loop using function
		answer  = input(promt)  #
		if answer == "yes":
			return True #4: Must have "return" to take back and print the value
		elif answer == "no":
			return False
		else:
			continue

def	calc_age(Year_born): #current_year: Disapper #8
	now = datetime.datetime.now()
	CURRENT_YEAR = now.year
	return CURRENT_YEAR - Year_born

def convert_meter_to_feet(meter):
	METER_TO_FEET = 3.281
	feet = meter * METER_TO_FEET
	feet = round(feet,1)
	return feet 


def print_height_info(Height_feet, is_male): #6
	### Compare with assign ##
	# if is_male == None:
	# 	print("Invalid")
	if is_male == True:
		if Height_feet > 6.5:
			print("You are very tall as a man")
		elif Height_feet < 5.9:
			print("You are ", end = "")  ### One "="
			i=0 ##initialtion 
			while i<11: ## Asign a value
				i +=1
				print("very", end = " ")
			print("short as a man")
		else:
			print("You are short as a man")
	else:					# is_male == False: Do not type this
		if Height_feet > 6.2:
			print("You are very tall as a girl")
		elif Height_feet < 5.2:
			print("You are", end = " ")
			for i in range(10):
				i += 1
				print("very", end = " ")
			print("short as a girl")
		else:
			print("You are short as a girl") #Between 5.2 and 6.2
	# else: #With nothing => with : #10
	# 	print("Syntax error")

def print_person_info(firstname, lastname, age, Height_feet, is_male, is_vietnamese):
	now = datetime.datetime.now()
	CURRENT_YEAR = now.year
	print("\n---")
	print("Your name is: {0} {1}".format(firstname,lastname))
	print("You are {0} years old in {1}".format(age,CURRENT_YEAR))
	print("Your height is " + str(Height_feet) + " feet tall")
	if is_vietnamese == True:
		print("You are vietnamese")
	else:
		print("You are not vietnamese")
	print_height_info(Height_feet, is_male) #9

def ask_person_info():
	firstname = input("Your firstname is: ") #1
	lastname = input("Your lastname is: ")
	Year_born = int(input("When were you born?: ")) #3: Change type direct in 'input'
	Height_meter = float(input("Your height in Meter is: ")) #3
	is_male = ask_yes_no("Are you male? (yes/no): ") #2 : Use while loop in function
	is_vietnamese = ask_yes_no("Are you vietnamese (yes/no): ")
	return firstname, lastname, Year_born, Height_meter, is_male, is_vietnamese

def main(): #1: Use "main"
	firstname, lastname, Year_born, Height_meter, is_male, is_vietnamese = ask_person_info() #
	age = calc_age(Year_born) #7 #8
	Height_feet = convert_meter_to_feet(Height_meter) #5
	print_person_info(firstname, lastname, age, Height_feet, is_male, is_vietnamese)

main()