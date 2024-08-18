# libraries used
import random
import sys

def generate_idea():
  
    # Generate a random idea
    ideas = [
        "Make a game",
        "Deploy a web app",
        "Write a short story",
        "Learn a new programming language",
      
        "Build a robot",
        "Create a painting",
        "Compose a song",
        "Start a blog",
        "Volunteer at a local charity",
        "Travel to a new country",
        "Learn a new skill",
        "Take a cooking class",
        "Start a business",
      
        "Write a book",
        "Practice or learn an instrument",
        "Take a dance class",
        "Learn a new language",
        "Go on a hike",
        "Read a book",
        "Watch a movie",
      
        "Spend time with family and friends",
        "Learn a new hobby",
        "Take a yoga class",
        "Meditate",
        "Go for a run",
        "Start a garden",
      
        "Learn about a new topic",
        "Take a photography class",
        "Learn about history",
        "Learn about science",
        "Learn about art",
        "Learn about music",
        "Learn about literature",
      
        "Learn about philosophy",
        "Learn about religion",
        "Learn about politics",
        "Learn about economics",
      
        "Take a deep breath",
        "Go play a sport",
        "Go take a nap!",
        "Meditate for 1 minute",
        "Relearn old things",
        "Learn about psychology"
    ]
    return random.choice(ideas)

def save_idea_to_file(idea, filename="ideas.txt"):
    # Save the generated idea to a file
    with open(filename, "a") as file:
        file.write(f"{idea}\n")

def print_home_screen():
  
    print("Idea Generator")
    print("Choose an option:")
    print("1. Get a new idea")
    print("2. Save to file")
    print("3. Show all Saved Ideas")
    print("4. Exit")

def list_saved_ideas(filename="ideas.txt"):
    try:
        with open(filename, "r") as file:
            print("Saved ideas:")
            print(file.read())
    except FileNotFoundError:
        print("Error. Noting here... Its empty")

def main():
    while True:
        print_home_screen()
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            print(f"Generated Idea: {generate_idea()}")
        elif choice == '2':
            idea = generate_idea()
            save_idea_to_file(idea)
            print(f"Idea saved to file: {idea}")
        elif choice == '3':
            list_saved_ideas()
        elif choice == '4':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
