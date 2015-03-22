formatter = "%r %r %r %r" # var with 4 raw data

print formatter % (1, 2, 3, 4) # print 4 num
print formatter % ("one", "two", "three", "four") # print 4 strings
print formatter % (True, False, False, True) # print 4 boolean
print formatter % (formatter , formatter, formatter, formatter) # the raw data %r
print formatter % (
	"I had this thing.",
	"That you could type up right.",
	"But it didn't sing.",
	"So I said goodnight."
)   # thought they should be printed in the same line
