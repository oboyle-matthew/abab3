import random

for i in range(10):
	for j in range(4):
		letter = chr(i+97)
		netid1 = letter + letter + str(j*2)
		netid2 = letter + letter + str(j*2+1)
		random.randint(0,9)
		print(netid1 + "," + netid2 + "," + str(random.randint(1,7)) + "," + str(random.randint(1,7)) + "," + str(random.randint(1,7)))
	netid3 = letter + letter + str(8)
	print(netid3 + "," + str(random.randint(1,7)) + "," + str(random.randint(1,7)) + "," + str(random.randint(1,7)))
	netid4 = letter + letter + str(9)
	print(netid3 + "," + str(random.randint(1,7)) + "," + str(random.randint(1,7)) + "," + str(random.randint(1,7)))