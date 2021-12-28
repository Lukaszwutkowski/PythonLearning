import pandas
from logo import logo

data = pandas.read_csv("../data/recipes.csv")
print(data)
#data.dropna(subset=["Category", "Title", "Quantity", "Unit of Measure", "Ingredient", "Directions"], inplace=True)
new_data = data.to_json("../data/recipe.json")

print(new_data)

def read_category():
    data.dropna(subset=["Category", "Title", "Quantity" , "Unit of Measure", "Ingredient", "Directions"], inplace=True)
    category_list = data.Category.to_list()
    return category_list

def read_cakes_cat():
    data.dropna(subset=["Title"], inplace=True)
    title_list = data.Title.to_list()
    cakes_list = title_list[0:37]
    return cakes_list

def chosen_recipe():
    pass


def start_menu():
    new_list = read_category()
    n = 0
    for cat in new_list:
        n = n + 1
        print(f"{n}.{cat}")

def cakes_menu():
    new_list = read_cakes_cat()
    n = 0
    for cat in new_list:
        n = n + 1
        print(f"{n}.{cat}")

def run():
    print(logo)
    print("Welcome!\nPlease choose an Category in Recipes Book by pressing a number.")
    start_menu()
    chosen_number = input("Please chose a number: ")
    if chosen_number == "1":
        print(cakes_menu())
    else:
        print("NNN")


#run()

#print(cakes_menu())
