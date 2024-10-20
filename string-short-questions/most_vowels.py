#WAP to accept a sentence and print the word with the most vowels

s = str(input("Enter the sentence "))
l = len(s)
v = 0
w = ''
temp1 = 0
temp2 = ''
for i in range(l):
    temp2 += s[i]
    if s[i] == 'a' or s[i] == 'e' or s[i] == 'i' or s[i] == 'o' or s[i] == 'u' or s[i] == 'A' or s[i] == 'E' or s[i] == 'I' or s[i] == 'O' or s[i] == 'U':
        temp1 += 1
    if s[i] == ' ':
        if temp1 > v:
            v = temp1
            w = temp2
        temp1 = 0
        temp2 = ''
print("The word with the largest number of vowels is ",w," with ",v," vowels")
