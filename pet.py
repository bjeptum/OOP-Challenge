#!/usr/bin/python3
class Pet:
    """A class representing a virtual pet."""
    def __init__(self, name):
        """Initialize the pet with a name and default attributes."""
        self.name = name
        self.hunger = 5
        self.energy = 5
        self.happiness = 5
        self.tricks = []

    def eat(self):
        """Feed the pet to reduce hunger and increase happiness.
        If the pet is too hungry, it will eat more.
        If the pet is too happy, it will eat less.

        Args:
            None
        """
        print(f"{self.name} is eating... 🍽️")
        self.hunger = max(0, self.hunger - 3)
        self.happiness = min(10, self.happiness + 1)

    def sleep(self):
        """Let the pet sleep to restore energy and happiness.
        If the pet is too happy, it will sleep less.
        If the pet is too hungry, it will sleep more.
        Args:
            None
        """
        print(f"{self.name} is sleeping... 😴")
        self.energy = min(10, self.energy + 5)

    def play(self):
        """Play with the pet to increase happiness and reduce energy.
        If the pet is too tired, it will not play.
        If the pet is too happy, it will play less.
        Args:
            None
        """
        if self.energy <= 0:
            print(f"{self.name} is too tired to play... 💤")
            return
        print(f"{self.name} is playing! 🎾")
        self.energy = max(0, self.energy - 2)
        self.happiness = min(10, self.happiness + 2)
        self.hunger = min(10, self.hunger + 1)

    def train(self, trick):
        """Train the pet to learn a new trick.
        If the pet is too tired, it will not learn.
        If the pet is too happy, it will learn faster.
        Args:
            trick (str): The trick to be learned.
        """
        print(f"{self.name} is learning a new trick: {trick} 🤓")
        self.tricks.append(trick)
        self.happiness = min(10, self.happiness + 1)
        self.energy = max(0, self.energy - 1)

    def show_tricks(self):
        """Display the tricks the pet has learned.
        If the pet has not learned any tricks, display a message.
        Args:
            None
        """
        if self.tricks:
            print(f"{self.name} knows the following tricks: {', '.join(self.tricks)} 🎉")
        else:
            print(f"{self.name} doesn't know any tricks yet.")
            
    def get_status(self):
        """
        Display the current status of the pet.
        This includes hunger, energy, happiness, and learned tricks.
        Args:
            None
        """
        print(f"\n{self.name}'s current status:")
        print(f"Hunger: {self.hunger}/10")
        print(f"Energy: {self.energy}/10")
        print(f"Happiness: {self.happiness}/10")
        print(f"Tricks: {self.tricks}\n")
