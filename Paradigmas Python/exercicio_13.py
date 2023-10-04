text1 = input("Diga o primeiro texto:")
text2 = input("Diga o segundo texto:")

print( text1, text2)
print(len(text1))
print(len(text2))
if text1 == text2:
    print("Textos iguais")
else:
    print("Os textos são diferentes")
if len(text1) == len(text2):
    print("comprimentos iguais")
else:
    print("comprimentos diferentes")