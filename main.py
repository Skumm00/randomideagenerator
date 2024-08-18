#libraries used
import random
import sys 

def generate_idea():
  #generate a random idea
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
    "Practice or learn a instrument",
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
    "Learn about economics",
    "Take a deep breath",
    "Go play a sport",
    "Go take a nap!",
    "Meditate for 1 minute",
    "relearn old things",
    "Learn about psychology"
  ]

  return random.choice(ideas)

def save_idea_to_file(idea, filename="ideas.txt"):

    # Save the generated idea to a file
    with open(filename, "a") as file:
        file.write(f"{idea}\n")

def main():
    if len(sys.argv) > 1 and sys.argv[1] == "--save":
      
        idea = generate_idea()
        save_idea_to_file(idea)
        print(f"Idea saved to file: {idea}")
    elif len(sys.argv) > 1 and sys.argv[1] == "--list":
        try:
            with open("ideas.txt", "r") as file:
                print("Saved ideas:")
                print(file.read())
        except FileNotFoundError:
            print("No ideas saved yet.")
    else:
        print(generate_idea())

if __name__ == "__main__":
    main()
