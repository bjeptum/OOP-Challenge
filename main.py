#!/usr/bin/python3
from pet import Pet

# Create the pet
my_pet = Pet("Max")

# Simulate some actions
my_pet.eat()
my_pet.play()
my_pet.sleep()

# Teach tricks
my_pet.train("roll over")
my_pet.train("play dead")

# Show pet status
my_pet.get_status()

# Show learned tricks
my_pet.show_tricks()
