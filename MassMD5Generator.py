import string, random, hashlib
alpha = string.ascii_letters
rlist = []

nums = int(input("(Hashes)> "))
length = int(input("(Length)> "))

for m in range(nums):
	randomstring = ''
	for x in range(length):
		randomstring += random.choice(alpha)
	rlist.append(hashlib.md5(randomstring.encode()).hexdigest())

rlist.sort()
f = open(str(nums) + "_" + str(length) + ".txt","w+")
for index in rlist:
	f.write(index)
	f.write("\n")
