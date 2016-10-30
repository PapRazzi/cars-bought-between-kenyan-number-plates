"""
This python script counts the number of cars sold between any two provided number plates
We calculate the number upto a given plate, ccalculate the number upto the other given plate, then find the difference between the two counts

Assumptions made is that all number plates between KAA 001A and KZZ 999Z are eligible

Given a number plate 'KCA 123G'

We first extract the individual characters K C A , the number sequence 123, and the last character G

Note:
	When a numberplate changes the third letter e.g. from KCA xxxx to KCB xxxx, 25974 cars have been sold
	When a numberplate changes the second letter e.g. from KBx xxxx to KCx xxxx, 675324 cars have been sold
	When a numberplate changes the last letter e.g. from KCA xxxA to KCA xxxB, 999 cars have been sold

Understand computation starting from the last four digits	
	When the last letter changes e.g. from A to B, 999 cars ending in A have been sold
	Use the last letter to find the number of cars ending in preceding letter that have been sold, and add the current num sequence
	E.g. for KAA 784C, we have 999 cars ending in A, and 999 cars ending in B, and 784 cars ending in C --- ((last_stop-1)*999) + 		num_seq_stop
				
	We Use the second and third letters of the number plate to find the total number of cars sold
	We use second_stop-1 because if the number plate is at KBA, (B=2), it means that all numberplates of KAx xxxx, have been used and A=1 		therefore A=B-1
	We use third_stop-1 because if the number plate is at KAC, (C=3), it means that all numberplates of KAB xxxx and KAB xxxx have been 		used, and B=2 therefore B=C-1	


Now, the total number of cars bought upto a given plaete can be found as:
total_num = ((second_stop-1)*675324) + ((third_stop-1)*25974) + ((last_stop-1)*999) + num_seq_stop

"""

import string

def count_car_sales(plate):
	total_num = 0
	#Extract number plate characters
	first = plate[0].upper()	
	second = plate[1].upper()
	third = plate[2].upper()
	num_seq = plate[4:7]
	last = plate[7].upper()
	
	#here, second_stop, third_stop and last_stop describe the where to stop counting (thus stop the iteration), as obtained from the number plate
	second_stop =  get_alpha_value(second) 
	third_stop =  get_alpha_value(third)
	num_seq_stop = int(num_seq)	
	last_stop =  get_alpha_value(last)
	
	#Calculate number of cars sold upto given number plate
	total_num = ((second_stop-1)*675324) + ((third_stop-1)*25974) + ((last_stop-1)*999) + num_seq_stop
	return total_num;

#this function returns an integer value for a given letter
def get_alpha_value(given_letter):
	letter_val =0
	#This is mapping a letter to a corresponding numeral value	
	letter_dict = { 'A':'1' , 'B':'2' , 'C':'3','D':'4' , 'E':'5' ,'F':'6','G':'7' ,'H':'8' , 'I':'9','J':'10' , 'K':'11' , 'L':'12','M':'13' ,'N':'14','O':'15','P':'16', 'Q':'17', 'R':'18','S':'19','T':'20','U':'21','V':'22' ,'W':'23', 'X':'24', 'Y':'25','Z':'26'}
	
	for letter, number in letter_dict.items():
		if(letter == given_letter):
    			letter_val = int(number)
			
	return letter_val;


def main():
	
	#user Input
	plate1 = input("Enter the first Number Plate in the form  KAA 123Z :")
	plate2 = input("Enter the second Number Plate in the form  KAA 123Z :")
		
	
	#calculate number of cars sold which is the difference between the number found for each of the two plates
	car_sales = count_car_sales(plate1) - count_car_sales(plate2)
	
	print("Total number of cars sold between the plates %s and %s is" % (plate1, plate2))		
	#show the absolute value of the difference
	print ("\tTotal number: ", abs(car_sales))
	return 0;
    
if __name__ == '__main__':
    main()
