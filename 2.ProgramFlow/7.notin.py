# activity =  input("What would you like to do today? ")
#
# if "Cinema" not in activity.casefold():
#     print("But I want to go to the cinema")

# Challenge
name = input("Please enter your name: ")
age = int(input("What's your age: "))

if age in range(18, 31):
    print(f"You're welcome to participate in the club🍸 holiday {name}😁!")
elif age < 18:
    print(f"Sorry {name} you're below the accepted age range 18-30years old!")
elif age > 18:
    print(f"Sorry {name} you're above the accepted age range 18-30years old!")
