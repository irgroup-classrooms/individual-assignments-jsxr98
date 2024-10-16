# This program calculates how much coffee you need to survive the semester! ☕️

def coffee_needed(assignments, exams):
    # Coffee is life! We assume 2 cups per assignment and 5 cups per exam.
    cups = (assignments * 2) + (exams * 5)
    return cups

assignments = 8
exams = 3

# Get the result with a cheeky comment
cups_of_coffee = coffee_needed(assignments, exams)
print(f"To survive this semester, you need approximately {cups_of_coffee} cups of coffee! 🚀☕")

# Fun message if you're over-caffeinated
if cups_of_coffee > 30:
    print("Warning: You might transform into a caffeinated coding machine! 💻🤖")
