attendees = int(input("Enter number of attendees: "))
venue = "large hall" if attendees > 100 else "conference room"
print(venue)

# Based on the corrected code from Task 1, further enhance the program to recommend additional facilities like "audio system" or "projector" based on the number of attendees.
system = "audio system" if attendees <= 100 else "projector"
print(system)

# Ask the user if they want "vegetarian" food. Recommend "Veggie Delight Caterers" if yes, otherwise recommend "Gourmet Meals Caterers".
food = input("Want vegetarian food? (yes/no) ")
choice = "Veggie Delight Caterers" if food == "yes" else "Gourmet Meals Caterers"
print(choice)