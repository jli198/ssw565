import requests

API_URL = "https://jsonplaceholder.typicode.com/posts"

def add_note():
    note = input("Enter your note: ")
    data = {"title": note, "body": note, "userId": 1}
    response = requests.post(API_URL, json=data)
    if response.status_code == 201:
        print("Note added to the cloud.")
    else:
        print("Failed to add note.")

def view_notes():
    
    #Please use the  requests.get(API_URS) to finish the view_notes function
    return

def menu():
    while True:
        print("\nMenu:")
        print("1. Add Note")
        print("2. View Notes")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            add_note()
        elif choice == '2':
            view_notes()
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    menu()
