#WAP to find the length of the longest substring without repeating characters

s = str(input("Enter the string "))
l = len(s)
c1 = 0
c2 = 0
s1 = ""
s2 = ""
for i in range(l):
    if(s[i]!=' '):
        if(s[i] in s1):
            if(c1 > c2):
                c2 = c1
                s2 = s1
            c1 = 0
            s1 = 0
        else:
            c1 += 1
            s1 += s[i]
print("The length of the longest substring is ",c2)
print("Longest substring is ",s2)