//anukarthika
s1=raw_input()
s2=""
for i in range(len(s1)):
	s2=s2+s1[i]
s3=s2[::-1]
if s2==s3:
	print("yes")
else:
	print("no")
