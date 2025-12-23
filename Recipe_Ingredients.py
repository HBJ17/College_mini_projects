# Recipe Management System

def add_recipe():
    name = input("Enter recipe name: ").strip()
    ingredients = input("Enter ingredients (comma separated): ").strip()

    with open("recipes.txt", "a") as r:
        r.write(name + "\n")

    with open("details.txt", "a") as d:
        d.write(name + ":" + ingredients + "\n")

    print("Recipe added successfully!\n")


def view_recipes():
    try:
        with open("recipes.txt", "r") as r:
            recipes = r.readlines()
            if not recipes:
                print("No recipes found.\n")
            else:
                print("Recipes:")
                for recipe in recipes:
                    print("-", recipe.strip())
                print()
    except FileNotFoundError:
        print("No recipe file found.\n")


def search_recipe():
    name = input("Enter recipe name to search: ").strip()
    try:
        with open("details.txt", "r") as d:
            for line in d:
                recipe, ingredients = line.strip().split(":")
                if recipe == name:
                    print("Ingredients:", ingredients, "\n")
                    return
            print("Recipe not found.\n")
    except FileNotFoundError:
        print("Details file not found.\n")


def delete_recipe():
    name = input("Enter recipe name to delete: ").strip()

    try:
        with open("recipes.txt", "r") as r:
            recipes = r.readlines()

        with open("details.txt", "r") as d:
            details = d.readlines()

        with open("recipes.txt", "w") as r:
            for recipe in recipes:
                if recipe.strip() != name:
                    r.write(recipe)

        with open("details.txt", "w") as d:
            for line in details:
                if not line.startswith(name + ":"):
                    d.write(line)

        print("Recipe deleted successfully!\n")
    except FileNotFoundError:
        print("Files not found.\n")


def update_ingredients():
    name = input("Enter recipe name to update: ").strip()
    new_ingredients = input("Enter new ingredients: ").strip()

    try:
        with open("details.txt", "r") as d:
            lines = d.readlines()

        with open("details.txt", "w") as d:
            found = False
            for line in lines:
                recipe, ingredients = line.strip().split(":")
                if recipe == name:
                    d.write(name + ":" + new_ingredients + "\n")
                    found = True
                else:
                    d.write(line)

        if found:
            print("Ingredients updated successfully!\n")
        else:
            print("Recipe not found.\n")

    except FileNotFoundError:
        print("Details file not found.\n")


while True:
    print("1.Add Recipe  2.View Recipes  3.Search Recipe")
    print("4.Delete Recipe  5.Update Ingredients  6.Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        add_recipe()
    elif choice == "2":
        view_recipes()
    elif choice == "3":
        search_recipe()
    elif choice == "4":
        delete_recipe()
    elif choice == "5":
        update_ingredients()
    elif choice == "6":
        print("Thank you!")
        break
    else:
        print("Invalid choice\n")
