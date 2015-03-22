def cheese_and_crackers (cheese_count, boxes_of_crackers): #define the function of 2 para
	print "You have %d cheeses!" % cheese_count #print para1
	print "You have %d boxes of crackers!" % boxes_of_crackers #print para2
	print "Man that's enough for a party!" 
	print "Get a blanket.\n"
	

print "We can just give the function numbers directly:"
cheese_and_crackers(20, 30) #use function directly with para inside


print "OR, we can use variables from our script:" #use function with var
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers) 


print "We can even do math inside too:"
cheese_and_crackers(10 + 20, 5 + 6) #use function to do math


print "And we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000) #use function to combine para and math