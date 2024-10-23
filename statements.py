

for x in range(2, 30, 3):
  print(x)


for x in range(2, 10):
  print(x)

def factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

# Example usage
num = 5
print(f"The factorial of {num} is {factorial(num)}")


fruits = ["apple", "banana", "cherry","mango","strawberry"]
for x in fruits:
  print(x)
  if x == "cherry":
    break


print("continue statement")
for x in fruits:
  if x == "banana":
    continue
  print(x)


  