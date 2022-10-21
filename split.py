word=input('enter a string:')
n=len(word)
hs=int(n/2)
ts=n-3

print(word[:hs])#first half of the string
print(word[hs:])#second half of the string

print(word[ts:])#prints last three elements
print(word[:ts])#prints first three elements

print([*word])#prints all characters of the given string
