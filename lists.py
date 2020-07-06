#new code, experimenting with lists

alphabet=["a", "b", "c","d"]
print("This is the right order:")
print(alphabet)

alphabet.reverse()
print("Reverse order:")
print(alphabet)
#Now returning in right order:
alphabet.reverse()

alphabet.pop()
print("popped the last one:")
print(alphabet)

alphabet.append("d")
alphabet.append("e")
alphabet.append("f")
print("appended three letters:")
print(alphabet)

alphabet.reverse()
alphabet.sort()
print("reversed and sorted:")
print(alphabet)

print("Letters in alphabet:" + str(len(alphabet)))