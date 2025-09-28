shopping_list = []

def display_menu():
    print("\n1. Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def add_item():
    item = input("Enter the item to add: ").strip().lower()
    if not item:
        print("Item name cannot be empty.")
        return
    if item in shopping_list:
        print(f"'{item}' is already in your shopping list.")
    else:
        shopping_list.append(item)
        print(f"'{item}' has been added to your shopping list.")

def remove_item():
    item = input("Enter the item to remove: ").strip().lower()
    if not item:
        print("Item name cannot be empty.")
        return
    if item in shopping_list:
        shopping_list.remove(item)
        print(f"'{item}' has been removed from your shopping list.")
    else:
        print(f"'{item}' not found in your shopping list.")

def view_list():
    if shopping_list:
        print("\nYour Shopping List:")
        for index, item in enumerate(shopping_list, start=1):
            print(f"{index}. {item}")
    else:
        print("Your shopping list is currently empty.")

def main():
    while True:
        display_menu()
        choice = input("Enter your choice (number): ").strip()

        try:
            choice_num = int(choice)
        except ValueError:
            print("Invalid choice. Please enter a number between 1 and 4.")
            continue

        if choice_num == 1:
            add_item()
        elif choice_num == 2:
            remove_item()
        elif choice_num == 3:
            view_list()
        elif choice_num == 4:
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
