# cars-bought-between-kenyan-number-plates
# Calculating the number of cars bought in between any two Kenyan number plates

TThis python script counts the number of cars sold between any two provided number plates

We count the number upto a given plate, count the number upto the other given plate, then find the difference between the two counts

Assumptions made is that all number plates between KAA 001A and KZZ 999Z are eligible

Given a number plate 'KCA 123G'

We first extract the individual characters K C A , the number sequence 123, and the last character G

# Note:
When a numberplate changes the third letter e.g. from KCA xxxx to KCB xxxx, 25974 cars have been sold
When a numberplate changes the second letter e.g. from KBx xxxx to KCx xxxx, 675324 cars have been sold
When a numberplate changes the last letter e.g. from KCA xxxA to KCA xxxB, 999 cars have been sold

# Understand computation starting from the last four digits	
When the last letter changes e.g. from A to B, 999 cars ending in A have been sold

Use the last letter to find the number of cars ending in preceding letter that have been sold, and add the current num sequence
E.g. for KAA 784C, we have 999 cars ending in A, and 999 cars ending in B, and 784 cars ending in C --- ((last_stop-1)*999) + num_seq_stop				

We use second_stop-1 because if the number plate is at KBA, (B=2), it means that all numberplates of KAx xxxx, have been used and A=1 therefore A=B-1

We use third_stop-1 because if the number plate is at KAC, (C=3), it means that all numberplates of KAB xxxx and KAB xxxx have been used, and B=2 therefore B=C-1	

Now, the total number of cars bought upto a given plaete can be found as:
total_num = ((second_stop-1)*675324) + ((third_stop-1)*25974) + ((last_stop-1)*999) + num_seq_stop
