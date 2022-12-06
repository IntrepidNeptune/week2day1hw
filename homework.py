# Q1: Print out all cubed numbers up to the total value 1000. Meaning that if the total value is over 1000 break the loop.
list_num = []

for i in range(0, 1000):
    list_num.append(i**3)
    if i**3 >= 1000:
        break

print(list_num)

# Q2: Get first prime numbers up to 100
N = 100

def isPrime(n):
  if(n==1 or n==0):
    return False 
  for i in range(2,n):
    if(n%i==0):
      return False
  return True
  
for i in range(1,N+1):
  if(isPrime(i)):
    print(i,end=" ")

# Q3: Take in a users input for their age, if they are younger than 18 print kids, if they're 18 to 65 print adults, else print seniors
age = int(input("Enter your age: "))

if age < 18:
    print("kids")
elif age > 65:
    print("seniors")
else: 
    print("adults")