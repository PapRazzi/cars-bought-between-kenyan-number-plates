"""
This python script counts the number of cars sold between any two provided number plates

Assumptions made is that all number plates between KAA 001A and KZZ 999Z are eligible

Given a number plate 'KCA 123G'

We first extract the individual characters K C A , the number sequence 123, and the last character G
We then loop through the last four letters - i.e. the 123G part to get the number of cars sold upto the point of the plate and get num_cars

When a numberplate changes the third letter e.g. from KCA xxxx to KCB xxxx, 25974 cars have been sold
When a numberplate changes the second letter e.g. from KBx xxxx to KCx xxxx, 675324 cars have been sold

Now, the total number of cars can be found as:
total_num = ((second_stop-1)*675324) + ((third_stop-1)*25974) +num_cars	

We use second_stop-1 because if the number plate is at KBA, (B=2), it means that all numberplates of KAx xxxx, have been used and A=1 therefore A=B-1
We use third_stop-1 because if the number plate is at KAC, (C=3), it means that all numberplates of KAB xxxx and KAB xxxx have been used, and B=2 therefore B=C-1


"""

import string

def count_car_sales(plate):
	num_cars = 0
	total_num = 0
	i_stop = 0;
	j_stop = 0;
	k_stop = 0;
	l_stop = 0;

	#Extract number plate characters
	first = plate[0].upper()	
	second = plate[1].upper()
	third = plate[2].upper()
	num_seq = plate[4:7]
	last = plate[7].upper()
	
	#here, second_stop third_stop and last_stop describe the where to stop counting (thus stop the iteration), as obtained from the number plate
	second_stop =  get_alpha_value(second) 
	third_stop =  get_alpha_value(third)
	num_seq_stop = int(num_seq)	
	last_stop =  get_alpha_value(last)
	
	#Here, we count the number of cars on the last four characters of the number plate
	for k in range(1,num_seq_stop+1):
		for l in range(1,last_stop+1):
			num_cars = num_cars + 1
	
	#We then use the second and third letters of the number plate to find the total number of cars sold
	#We use second_stop-1 because if the number plate is at KBA, (B=2), it means that all numberplates of KAx xxxx, have been used and A=1 therefore A=B-1
	#We use third_stop-1 because if the number plate is at KAC, (C=3), it means that all numberplates of KAB xxxx and KAB xxxx have been used, and B=2 therefore B=C-1
	total_num = ((second_stop-1)*675324) + ((third_stop-1)*25974) + num_cars	
	return total_num;

#this function returns an integer value for a given letter
def get_alpha_value(given_letter):
	letter_val =0
	letter_dict = { 'A':'1' , 'B':'2' , 'C':'3','D':'4' , 'E':'5' ,'F':'6','G':'7' ,'H':'8' , 'I':'9','J':'10' , 'K':'11' , 'L':'12','M':'13' ,'N':'14','O':'15','P':'16', 'Q':'17', 'R':'18','S':'19','T':'20','U':'21','V':'22' ,'W':'23', 'X':'24', 'Y':'25','Z':'26'}
	
	for letter, number in letter_dict.items():
		if(letter == given_letter):
    			letter_val = int(number)
			
	return letter_val;
	

def main():
	
	#user Input
	plate1 = input("Enter the first Number Plate in the form 'KAA 123Z' :")
	plate2 = input("Enter the second Number Plate in the form 'KAA 123Z' :")
		
	
	#calculate number of cars sold
	car_sales = count_car_sales(plate1) - count_car_sales(plate2)
	
	print("Total number of cars sold between the plates %s is %s  " % (plate1, plate2))		
	#show the absolute value of the difference
	print ("\tTotal number: ", abs(car_sales))
	return 0;
    
if __name__ == '__main__':
    main()
