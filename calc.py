## One Rep Max Calculator

# Collect the weight lifted and reps completed
weight = float(input("How much weight? "))
reps = float(input("How many reps? "))

# Compute the one rep max
one_rep_max = int(weight * (36 / (37 - reps)))

# Print the result
if reps > 12:
	print 'This calculator is less effective with reps above 12'
else:
	print "Your one rep max is %s" % one_rep_max