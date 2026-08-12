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

has_puddles = input("Are there puddles on the ground? (yes/no):")
if has_puddles == "yes":
    shoes="boots"
    print("Wear boots.", shoes)
else:
    shoes="sneakers"
    print("Wear sneakers.", shoes)
pizza = int(input("How many slices of pizza do you want? "))
if pizza > 3:
    print("That's a lot of pizza!")
else:
    print("Enjoy your pizza!")
mom_saw = input("Did mom see you eating the pizza? (yes/no): ")
if mom_saw.lower() == "yes":
    print("Run mom knows🏃‍♂️")
else:
    print("Enjoy your pizza without getting caught!🍕")
sleep_hours= int(input("How many hours did you sleep last night? "))

if sleep_hours >= 8:
    print("You had a good night's sleep!😴")
else:
    print("You should get more sleep!😴")