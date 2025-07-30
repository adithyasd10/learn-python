def reverseString(s):
    l=list(s)
    print(l)
    l.reverse()
    print(l)
    return "".join(l)
    
s=input('Enter a string')
result = reverseString(s)
print("Reversed String:", result)

# Sample Output:
# Enter a string: Hi
# Original as list: ['H', 'i']
# Reversed list: ['i', 'H']
# Reversed String: iH
