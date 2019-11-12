if __name__ == '__main__':
    
    s = input()
for i in range(0,len(s)):
    if s[i].isalnum():
        print("True")
        break
else:
    print("False")
for i in range(0,len(s)):
    if s[i].isalpha():
        print("True")
        break
else:
    print("False")
for i in range(0,len(s)):
    if s[i].isdigit():
        print("True")
        break
else:
    print("False")
for i in range(0,len(s)):
    if s[i].islower():
        print("True")
        break
else:
    print("False")
for i in range(0,len(s)):
    if s[i].isupper():
        print("True")
        break
else:
    print("False")

