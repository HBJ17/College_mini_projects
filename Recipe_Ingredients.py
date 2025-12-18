def add_recipe():
    name = input("Enter recipe name: ")
    ingredients = input("Enter ingredients: ")

    with open("recipes.txt", "a") as f:
        f.write(name + "\n")

    with open("details.txt", "a") as f:
        f.write(name + ":" + ingredients + "\n")

def view_recipes():
    with open("recipes.txt", "r") as f:
        print(f.read())

def search_recipe():
    name = input("Enter recipe name to search: ")
    with open("details.txt", "r") as f:
        for line in f:
            if line.startswith(name + ":"):
                print("Ingredients:", line.split(":")[1])

def delete_recipe():
    name = input("Enter recipe name to delete: ")

    with open("recipes.txt", "r") as f:
        lines = f.readlines()
    with open("recipes.txt", "w") as f:
        for line in lines:
            if line.strip() != name:
                f.write(line)

    with open("details.txt", "r") as f:
        lines = f.readlines()
    with open("details.txt", "w") as f:
        for line in lines:
            if not line.startswith(name + ":"):
                f.write(line)

def update_recipe():
    name = input("Enter recipe name: ")
    new_ing = input("Enter new ingredients: ")

    with open("details.txt", "r") as f:
        lines = f.readlines()
    with open("details.txt", "w") as f:
        for line in lines:
            if line.startswith(name + ":"):
                f.write(name + ":" + new_ing + "\n")
            else:
                f.write(line)
while True:
    print("\nRecipe Ingredients System")
    print("1. Add Recipe")
    print("2. View Recipes")
    print("3. Search Recipe")
    print("4. Delete Recipe")
    print("5. Update Recipe")
    print("6. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == "1":
        add_recipe()
    elif choice == "2":
        view_recipes()
    elif choice == "3":
        search_recipe()
    elif choice == "4":
        delete_recipe()
    elif choice == "5":
        update_recipe()
    elif choice == "6":
        break
    else:
        print("Invalid choice. Please try again.")
        