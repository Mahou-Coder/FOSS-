print("Welcome, I don't know you, but I'll tell you if a number is even or odd")
a=int(input('Enter a number: '))
if a==0:
 print(a, 'is neither even nor odd')
elif a%2==0:
 print(a,'is even')
else:
 print(a,' is odd')
