#libraries
import random
import sys
import os

def generate_idea():
    ideas = [
        "Make a game", "Deploy a web app", "Write a short story", "Learn a new programming language",
        "Build a robot", "Create a painting", "Compose a song", "Start a blog", "Volunteer at a local charity",
        "Travel to a new country", "Learn a new skill", "Take a cooking class", "Start a business",
        "Write a book", "Practice or learn an instrument", "Take a dance class", "Learn a new language",
        "Go on a hike", "Read a book", "Watch a movie", "Spend time with family and friends", "Learn a new hobby",
        "Take a yoga class", "Meditate", "Go for a run", "Start a garden", "Learn about a new topic",
        "Take a photography class", "Learn about history", "Learn about science", "Learn about art",
        "Learn about music", "Learn about literature", "Learn about philosophy", "Learn about religion",
        "Learn about politics", "Learn about economics", "Take a deep breath", "Go play a sport",
        "Go take a nap!", "Meditate for 1 minute", "Relearn old things", "Learn about psychology"
    ]
    return random.choice(ideas)

def save_idea_to_file(idea, filename="ideas.txt"):
    with open(filename, "a") as file:
        file.write(f"{idea}\n")

def print_home_screen():
    print("\nIdea Generator")
    print("Choose an option:")
    print("1. Get a new idea")
    
    print("2. Save idea to file")
    print("3. Show all saved ideas")
    print("4. Clear saved ideas")
    print("5. Exit")

def list_saved_ideas(filename="ideas.txt"):
    if os.path.exists(filename):
        with open(filename, "r") as file:
            ideas = file.readlines()
            if ideas:
                print("Saved ideas:")
                for i, idea in enumerate(ideas, start=1):
                    print(f"{i}. {idea.strip()}")
            else:
                print("No saved ideas.")
    else:
        print("Error. File not found.")

def clear_saved_ideas(filename="ideas.txt"):
    if os.path.exists(filename):
        open(filename, 'w').close()
        print("All saved ideas have been cleared.")
    else:
        print("Error. File not found.")

def main():
    while True:
        print_home_screen()
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            print(f"Generated Idea: {generate_idea()}")
        
        elif choice == '2':
            idea = generate_idea()
            save_idea_to_file(idea)
            print(f"Idea saved to file: {idea}")
            
        elif choice == '3':
            list_saved_ideas()
            
        elif choice == '4':
            clear_saved_ideas()
            
        elif choice == '5':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

#now run the program
if __name__ == "__main__":
    main()
