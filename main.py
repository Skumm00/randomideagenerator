#libraries used
import random

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
    "Learn about psychology"
  ]

  return random.choice(ideas)

if __name__ == "__main__":
  print(generate_idea())