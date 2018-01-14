import re

s1 = '''PASTE YOUR CODE HERE
'''

t = re.split(r".*\*\*\*.*", s1)

for i in range(1, len(t) - 1):
	t[i] = "GO\n" + t[i]
	s1 = t[i]
	s2 = re.sub(r"[\[\]]", "", s1)
	s2 = re.sub(r"GO(.*\n)*CREATE", "CREATE", s2)
	s2 = re.sub(r"dbo\.", "", s2)
	s2 = re.sub(r"CLUSTERED\s*\(\s*([\w_]*)(.*\n)\)(.*\n)(.*\n)", "(\g<1>)\n)\n;", s2)
	s2 = re.sub(r"GO", "", s2)
	s2 = s2.replace("int", "INTEGER").replace("varchar", "VARCHAR")
	print (s2)

t = re.split(r"ALTER", t[-1])
t[0] = "GO\n" + t[0]
s1 = t[0]
s2 = re.sub(r"[\[\]]", "", s1)
s2 = re.sub(r"GO(.*\n)*CREATE", "CREATE", s2)
s2 = re.sub(r"dbo\.", "", s2)
s2 = re.sub(r"CLUSTERED\s*\(\s*([\w_]*)(.*\n)\)(.*\n)(.*\n)", "(\g<1>)\n)\n;", s2)
s2 = re.sub(r"GO", "", s2)
s2 = s2.replace("int", "INTEGER").replace("varchar", "VARCHAR")
print (s2)

for i in range(1, len(t)):
	t[i] = "ALTER" + t[i]
	s2 = re.sub(r"[\[\]]", "", t[i])
	s2 = re.sub(r"dbo\.", "", s2)
	s2 = re.sub(r"GO\n", "", s2)
	s2 = s2.replace(" WITH CHECK ", "")
	print (s2 + ";")