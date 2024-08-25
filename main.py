import random
import os
from datetime import datetime

# Expanded list of ideas categorized by type
ideas = {
    "general": [
        "Make a game", "Deploy a web app", "Write a short story", "Travel to a new country",
        "Start a blog", "Volunteer at a local charity", "Read a book", "Watch a movie", 
        "Spend time with family and friends", "Go on a hike", "Start a garden", 
        "Learn about a new topic", "Organize a community event", "Try a new hobby", "Take a class online",
        "Explore local museums", "Plan a weekend getaway", "Try a new restaurant", "Visit a historical site"
    ],
    "coding": [
        "Build a mobile app", "Contribute to an open-source project", "Create a Python script to automate a task",
        "Learn a new programming language", "Develop a website using a new framework", 
        "Build a chatbot", "Work on a machine learning project", "Explore cloud computing tools",
        "Create a video game", "Develop a personal finance tracker"
    ],
    "music": [
        "Compose a new song", "Learn to play a new instrument", "Record a cover of your favorite song",
        "Write lyrics for a song", "Experiment with music production software", 
        "Attend a local concert", "Join a local band or choir", "Explore different music genres",
        "Create a music playlist for different moods", "Learn about music theory"
    ],
    "hobbies": [
        "Start a painting project", "Learn knitting or crocheting", "Take up gardening", 
        "Try cooking a new recipe", "Explore photography", "Take up a new sport", 
        "Join a book club", "Learn pottery or sculpture", "Try woodworking", "Start a model train collection"
    ],
    "wellness": [
        "Practice mindfulness meditation", "Start a daily yoga routine", "Take a nature walk", 
        "Learn a new relaxation technique", "Attend a wellness workshop", 
        "Explore different types of exercise", "Try a new healthy recipe", "Schedule a digital detox day",
        "Join a fitness class", "Practice deep breathing exercises"
    ],
    "personal_development": [
        "Take a public speaking course", "Read a self-help book", "Write a personal journal", 
        "Set personal goals for the year", "Learn about time management", "Attend a personal development seminar",
        "Try a new productivity technique", "Take a course on emotional intelligence", "Explore career coaching", "Learn about financial planning"
    ],
    "travel": [
        "Plan a road trip across your country", "Visit a famous landmark", "Explore a new city", 
        "Try backpacking in a foreign country", "Take a scenic train ride", "Attend a cultural festival",
        "Go on a wildlife safari", "Plan a beach vacation", "Try a new adventure sport", "Explore local food markets"
    ],
    "creative_writing": [
        "Write a novel", "Start a poetry collection", "Create a screenplay", "Write a script for a short film", 
        "Develop a new blog series", "Experiment with different writing styles", "Join a writing group", 
        "Create a personal memoir", "Write and illustrate a children's book", "Try writing flash fiction"
    ],
    "technology": [
        "Build a DIY tech project", "Explore new tech gadgets", "Learn about blockchain technology", 
        "Experiment with virtual reality", "Create a personal tech blog", "Develop a mobile game",
        "Learn about artificial intelligence", "Build a home automation system", "Try out new programming tools", "Attend a tech conference"
    ],
    "art": [
        "Learn digital art techniques", "Create a new sculpture", "Take a graphic design course", 
        "Explore abstract painting", "Create an art installation", "Try mixed media art", 
        "Attend an art workshop", "Explore art history", "Create a custom mural", "Join an art community"
    ]
}

def generate_idea(category="general"):
    if category in ideas:
        return random.choice(ideas[category])
    else:
        return "Invalid category. Please select a valid category."

def save_idea_to_file(idea, filename="ideas.txt"):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(filename, "a") as file:
        file.write(f"{timestamp} - {idea}\n")

def print_home_screen():
    print("\nIdea Generator")
    print("Choose an option:")
    print("1. Get a new idea")
    print("2. Save idea to file")
    print("3. Show all saved ideas")
    print("4. Clear saved ideas")
    print("5. Exit")

def print_category_menu():
    print("\nSelect a category for the idea:")
    print("1. General")
    print("2. Coding")
    print("3. Music")
    print("4. Hobbies")
    print("5. Wellness")
    print("6. Personal Development")
    print("7. Travel")
    print("8. Creative Writing")
    print("9. Technology")
    print("10. Art")

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

   
# Now run the program
if __name__ == "__main__":
    main()
