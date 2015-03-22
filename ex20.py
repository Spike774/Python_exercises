from sys import argv

script, input_file = argv  #get initiate input

def print_all(f): #read and print all
	print f.read() 
	
def rewind(f): #return the count to start point
	f.seek(0)
	
def print_a_line(line_count, f): #read only one line
	print line_count, f.readline()
	
current_file = open(input_file) #set the para file object

print "First let's print the whole file:\n" 

print_all(current_file)

print "Now let's rewind, kind of like a tape."

rewind(current_file)

print "Let's print three lines:"

current_line = 1 # step print each line
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)