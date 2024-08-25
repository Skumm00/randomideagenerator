#libraries used
import random
import os
from datetime import datetime

# List of different types of users
personalizeuser = {
    1: "Beginner Learner",
    2: "Intermediate Learner",
    3: "Advanced Learner",
    4: "Expert Learner",
    5: "Hard Worker",
    6: "Pro Learner"
}

# Expanded list of ideas categorized by type and difficulty
ideas = {
    "general": {
        "Beginner Learner": [
            "Read a book", "Go on a hike", "Watch a movie", "Start a garden", 
            "Explore local museums", "Try a new hobby"
        ],
        "Intermediate Learner": [
            "Travel to a new country", "Start a blog", "Volunteer at a local charity", 
            "Organize a community event", "Plan a weekend getaway", "Explore local food markets"
        ],
        "Advanced Learner": [
            "Deploy a web app", "Write a short story", "Learn about a new topic", 
            "Attend a cultural festival", "Explore local historical sites"
        ],
        "Expert Learner": [
            "Make a game", "Create a new app", "Develop a complex project", 
            "Participate in a local competition", "Write a comprehensive guide"
        ],
        "Hard Worker": [
            "Work on a challenging project", "Take an intensive course", "Start a business", 
            "Lead a community initiative", "Undertake a major home renovation"
        ],
        "Pro Learner": [
            "Start a non-profit organization", "Mentor others in your field", "Write a book", 
            "Speak at an international conference", "Lead a research project"
        ]
    },
    
    "coding": {
        "Beginner Learner": [
            "Build a simple website", "Create a basic script", "Learn HTML/CSS", 
            "Build a basic calculator", "Try a beginner's coding challenge"
        ],
        "Intermediate Learner": [
            "Develop a small web app", "Learn JavaScript frameworks", "Build a chatbot", 
    
            "Create a personal portfolio site", "Contribute to an open-source project"
        ],
        "Advanced Learner": [
            "Create a complex app", "Work on a machine learning model", "Build a video game", 
            "Develop a web API", "Explore cloud services"
        ],
        "Expert Learner": [
            "Build a scalable system", "Work with big data", "Create a custom CMS", 
            "Develop a sophisticated AI tool", "Lead a software development team"
        ],
        
        "Hard Worker": [
            "Optimize an existing system", "Develop an advanced tech product", "Start a tech blog", 
            "Build an innovative tool", "Explore cutting-edge technologies"
        ],
        "Pro Learner": [
            "Create a groundbreaking app", "Lead a major tech initiative", "Consult on high-profile projects", 
            "Develop proprietary algorithms", "Speak at a major tech conference"
        ]
    },
    "music": {
        "Beginner Learner": [
            "Learn basic chords on a guitar", "Start a simple music playlist", "Explore different music genres", 
            "Attend a beginner's music class", "Record a basic cover song"
        ],
        
        "Intermediate Learner": [
            "Compose a simple melody", "Experiment with music production software", "Join a local band", 
            "Attend a music workshop", "Record and mix a demo"
        ],
        "Advanced Learner": [
            "Write and produce a full song", "Learn advanced music theory", "Create a music video", 
            "Perform at a local event", "Collaborate with other musicians"
        ],
        "Expert Learner": [
            "Compose a symphony", "Record an album", "Create a new genre of music", 
            "Work with a renowned producer", "Start a music education program"
        ],
        "Hard Worker": [
            "Organize a large music event", "Create an innovative music project", "Teach advanced music classes", 
            "Lead a music-focused non-profit", "Develop a music-related app"
        ],
        "Pro Learner": [
            "Conduct a major music symphony", "Collaborate on a global music project", "Speak at an international music conference", 
            "Start a music mentorship program", "Lead a major music initiative"
        ]
    },
    #More catagories
}

#generate idea function
def generate_idea(category="general", user_type="Beginner Learner"):
    if category in ideas and user_type in ideas[category]:
        return random.choice(ideas[category][user_type])
    else:
        return "Invalid category or user type. Please select valid options."

#save to file function
def save_idea_to_file(idea, filename="ideas.txt"):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open(filename, "a") as file:
        file.write(f"{timestamp} - {idea}\n")
        
#print home screen function.
def print_home_screen():
    print("\nIdea Generator")
    print("Choose an option:")
    print("1. Get a new idea")
    print("2. Save idea to file")
    print("3. Show all saved ideas")
    print("4. Clear saved ideas")
    print("5. Exit")
    
#print catagory function
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

def print_user_type_menu():
    print("\nSelect your user type:")
    for key, value in personalizeuser.items():
        print(f"{key}. {value}")
        
#save the ideas
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
    
#print the saved ideas
def clear_saved_ideas(filename="ideas.txt"):
    if os.path.exists(filename):
        open(filename, 'w').close()
        print("All saved ideas have been cleared.")
    else:
        print("Error. File not found.")
        
def secretmessage():
    #show the secret messages
    print("Wow, you shouldnt be reading this but you are, so here is a secret little game and if you pass it, I will give you a super secret idea.")
    userres = input("What is the name of the person who made all of these projects?")
    #now give a answer depending on the message.
    if userres.lower() == "skumm00" or "skand":
        userres = ""
        #now give the second question
        userres = input("Great! Now answer this, what climbs up a hill on 4 legs and comes back on 2?")
        if userres.lower() == "nothing":
            print("Good Job, you won! Here is the secret idea: Start working on your dream")
        else:
            print("You were so close but you LOST!")
    else:
        print("Wrong! Terminating all programs")
def main():
    while True:
        #show all the choices as well as print the home screen
        print_home_screen()
        choice = input("Enter your choice (1-5): ")
        #generate a new idea
        if choice == '1':
            print_category_menu()
            category_choice = input("Select category (1-10): ")
            categories = {
                "1": "general", "2": "coding", "3": "music", "4": "hobbies", "5": "wellness",
                "6": "personal_development", "7": "travel", "8": "creative_writing", "9": "technology", "10": "art"
            }
            category = categories.get(category_choice, "general")
            #print the user menu
            print_user_type_menu()
            user_type_choice = int(input("Select your user type (1-6): "))
            user_type = personalizeuser.get(user_type_choice, "Beginner Learner")

            idea = generate_idea(category, user_type)
            print(f"Generated Idea: {idea}")
        #save to file
        elif choice == '2':
            print_category_menu()
            category_choice = input("Select category (1-10): ")
            categories = {
                "1": "general", "2": "coding", "3": "music", "4": "hobbies", "5": "wellness",
                "6": "personal_development", "7": "travel", "8": "creative_writing", "9": "technology", "10": "art"
            }
            category = categories.get(category_choice, "general")

            print_user_type_menu()
            user_type_choice = int(input("Select your user type (1-6): "))
            user_type = personalizeuser.get(user_type_choice, "Beginner Learner")

            #generate ideas to file
            idea = generate_idea(category, user_type)
            save_idea_to_file(idea)
            print(f"Idea saved to file: {idea}")
        #show the list of saved ideas
        elif choice == '3':
            list_saved_ideas()
        #show the different choices
        elif choice == '4':
            clear_saved_ideas()
        #5 choices the user can choose
        elif choice == '5':
            print("Exiting the program.")
            secretmessage()
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

# Now run the program
if __name__ == "__main__":
    main()
