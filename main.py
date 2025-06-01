import json
import os

json_filename = "data.json"
notes = []

def load_json_file():
    if os.path.exists(json_filename):
        with open(json_filename, "r") as f:
            data = json.load(f)  
            for i in range(len(data)):
                notes.append(data[str(i)])  
    else:
        with open(json_filename, "w") as f:
            json.dump({}, f)  

# above this line is important code please do not touch

print("Welcome to QuickNotes 📓")

# by making a infinite loop everytime the user is done with one thing they will immidiately get back up here
while True:
    print("\n1. View notes    \
           \n2. Add a new note\
           \n3. Delete a note \
           \n4. Exit")
    
    choice = None
    while True:
        user_input = input("Your choice (1-4): ")
        if user_input.isdigit():
            choice = int(user_input)
            break
        else:
            print("Please enter a number between (1-4)")

    def show_notes():
        if len(notes):
            for i in range(len(notes)):
                print(f"{i + 1}. \"{notes[i]["title"]}\"")
        else:
            print("You have zero notes saved")

    def add_to_json():
        open(json_filename, "w").close() # this clears out the entire JSON file
        with open(json_filename, "w") as f:
            f.write("{\n")
            for i in range(len(notes)):
                
                if i >= 1:
                    f.write(f'  ,"{i}": {json.dumps(notes[i])}\n')
                else:
                    f.write(f'  "{i}": {json.dumps(notes[i])}\n')
            f.write("\n}")

    def add_note(note):
        new_dict = {"title": note}
        notes.append(new_dict)
        add_to_json()

    match choice:
        case 1:
            show_notes()
        case 2:
            user_note = input("Enter your note: ")
            add_note(user_note)
            show_notes()
        case 3:
            if len(notes):
                show_notes() 
                # to make the list start from 1 I have to remove one to make the indexing correct
                user_deletion_index = int(input(f"Which of these notes to delete (1-{len(notes)})?")) - 1
                print(notes[user_deletion_index])
                del notes[user_deletion_index]
                add_to_json()
                show_notes()
            else:
                print("Brody you have nothing to delete you gotta make to destroy first")
        case 4:
            quit()