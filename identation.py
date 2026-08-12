temperature = int(input("Enter the temperature: "))

if temperature > 30:
    print("It's hot outside!")
else:
    print("It's not hot outside.")

age = int(input("Enter your age: "))

print("the value of age is", age)

if age >= 18:
    print("You can vote.")
else:
    print("You cannot vote.")

is_raining = input("Is it raining? (yes/no): ")

if is_raining.lower() == "yes":
    print("Take an umbrella")
else:
    print("No need for an umbrella.")

name = input("Enter your name: ")
if name == "Nia":
    print("Hello, Nia!")
else:
    print("Hello, stranger!")