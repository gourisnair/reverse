str1="ca22197b090135d5cf5c52fd85009b82"
b=''
for x in range(-1, -len(str1), -2):
    b += str1[x-1] + str1[x]
print b
for i in range(18,32,4):
	a=b[i]+b[i+1]
	if(i==18):
		c="0x5d"
	elif(i==22):
		c="0x35"
	elif(i==26):
		c="0xffffffa5"	
	elif(i==30):
		c="0x31"
	d=hex(int(a,16)^int(c,16))
	d=str(d[-2:])
	b=b.replace(a,d)
print b

