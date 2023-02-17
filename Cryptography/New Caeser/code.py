import string

LOWERCASE_OFFSET = ord("a")
ALPHABET = string.ascii_lowercase[:16]

enc = "lkmjkemjmkiekeijiiigljlhilihliikiliginliljimiklligljiflhiniiiniiihlhilimlhijil"




def shift(c, k):
	t1 = ord(c) - LOWERCASE_OFFSET
	t2 = ord(k) - LOWERCASE_OFFSET
	return ALPHABET[(t1 + t2) % len(ALPHABET)]
def b16_decode(enc):
	list=[]
	list1=[]
	list2=[]
	for c in enc:
		for i in range(16):
			if ALPHABET[i] == c:
				list.append(i)
	count = 0
	for i in list:
		if count % 2 == 1:
			list2.append(i)
		else:
			list1.append(i)
		count += 1

	flag = ""
	for i in range(39):
		flag += chr((list1[i] << 4) + list2[i])
	return(flag)

for k in ALPHABET:
	plain = ""
	for i in enc:
		plain += shift(i, k)
	print(b16_decode(plain))