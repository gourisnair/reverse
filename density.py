#The challenge is from ASIS-QUALS(2018)- DENSITY
#The given nam of the binary was b64pack. So I use the command "base64 <filename>" and I got the string "b64dec" given below.
#Then after reversing I wrote the following script to print the flag.

b64dec="O++h+b+qcASIS++e01d+c4Nd+cGoLD+cASIS+c1De4+c4H4t+cg0e5+cf0r+cls+d++gdI++j+kM+vb++fD9W+q/Cg=="
new=""
l=len(b64dec)
fcheck="@$_!\"#%&'()*+,-./:;<=>?\n"
scheck="[\\]^{|}~`\t"
i=0
while(i<l-1):
	if(b64dec[i]=="+"):
		i=i+1
		if(b64dec[i]=="+"):
			i=i+1
			new+=scheck[ord(b64dec[i])-97]
		else:
			new+=fcheck[ord(b64dec[i])-97]
	else:
		new+=b64dec[i]
	i=i+1
print new
