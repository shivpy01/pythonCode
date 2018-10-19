from cric_class import cricket
target = 25
x = 0
import random
target = random.randint(1,25)

for i in range(1,7):
	import random
	our = [1, 2, 3, 4, 6, "out"]
	t = random.choice(our)
	try:
		player = cricket(t)
		x = x+t
		print(t)
		if x> target:
			break
		else:
			continue
	except TypeError:
			print("out")
			break
	
print(x,"total")
if x > target:
	print("target was :",target,"winner($$)")
elif x == target:
	print("tied",target,"(-^-)")
else:
	print("target was :",target,"bad luck(00)")

	
