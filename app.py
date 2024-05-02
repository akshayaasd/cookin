from flask import Flask, render_template, request

app = Flask(__name__)

# Define Indian recipes
indian_recipes = {
    "Curry": {
        "Paneer Gravy": {
            "ingredients": ["paneer", "onion", "tomato", "ginger", "garlic", "spices"],
            "steps": [
                "Dice the paneer into cubes.",
                "Sauté chopped onion, ginger, and garlic in a pan until golden brown.",
                "Add chopped tomatoes and cook until soft.",
                "Blend the mixture into a smooth paste.",
                "Return the paste to the pan, add spices and cook until fragrant.",
                "Gently add the paneer cubes and simmer until the gravy thickens.",
                "Garnish with fresh coriander leaves and serve hot."
            ],
            "timings": [10, 15, 10, 10, 5, 10, 5]  # Timings in minutes for each step
        },
        "Soya Bean Gravy": {
            "ingredients": ["soya chunks", "onion", "tomato", "ginger", "garlic", "spices"],
            "steps": [
                "Soak soya chunks in hot water for 15-20 minutes and squeeze out excess water.",
                "Sauté chopped onion, ginger, and garlic until golden brown.",
                "Add chopped tomatoes and cook until soft.",
                "Blend the mixture into a smooth paste.",
                "Return the paste to the pan, add spices and cook until fragrant.",
                "Add soaked soya chunks and simmer until the gravy thickens.",
                "Garnish with coriander leaves and serve hot."
            ],
            "timings": [20, 15, 10, 10, 5, 15, 5]  # Timings in minutes for each step
        },
        "Chicken Gravy": {
            "ingredients": ["chicken", "onion", "tomato", "ginger", "garlic", "spices"],
            "steps": [
                "Marinate chicken with yogurt, ginger-garlic paste, and spices for 1 hour.",
                "Sauté chopped onion, ginger, and garlic until golden brown.",
                "Add chopped tomatoes and cook until soft.",
                "Blend the mixture into a smooth paste.",
                "Return the paste to the pan, add marinated chicken and cook until tender.",
                "Simmer until the gravy thickens.",
                "Garnish with coriander leaves and serve hot."
            ],
            "timings": [60, 15, 10, 10, 30, 20, 5]  # Timings in minutes for each step
        },
    },
    "Rice": {
        "Vegetable Biryani": {
            "ingredients": ["rice", "mixed vegetables", "yogurt", "spices"],
            "steps": [
                "Cook rice until partially done.",
                "Sauté vegetables and spices in a pan.",
                "Layer partially cooked rice and vegetables, and cook until done."
            ],
            "timings": [15, 15, 30]  # Timings in minutes for each step
        },
        "Chicken Biryani": {
            "ingredients": ["rice", "chicken", "yogurt", "spices"],
            "steps": [
                "Marinate chicken in yogurt and spices for 1 hour.",
                "Cook rice until partially done.",
                "Layer marinated chicken and partially cooked rice, and cook until done."
            ],
            "timings": [60, 15, 45]  # Timings in minutes for each step
        },
        "Pulao": {
            "ingredients": ["rice", "vegetables", "spices"],
            "steps": [
                "Sauté vegetables and spices in a pan.",
                "Cook rice with sautéed vegetables until done."
            ],
            "timings": [15, 25]  # Timings in minutes for each step
        }
    },
    "Side Dish": {
        "Soya Chunks Fry": {
            "ingredients": ["soya chunks", "onion", "tomato", "ginger", "garlic", "spices"],
            "steps": [
                "Boil soya chunks until soft.",
                "Sauté onion, tomato, ginger, and garlic in a pan.",
                "Add boiled soya chunks and spices, cook until flavors blend."
            ],
            "timings": [20, 15, 15]  # Timings in minutes for each step
        },
        "Low-Oil Chicken Tikka": {
            "ingredients": ["chicken", "yogurt", "spices"],
            "steps": [
                "Marinate chicken in yogurt and spices for 30 minutes.",
                "Grill or bake chicken until cooked through."
            ],
            "timings": [30, 20]  # Timings in minutes for each step
        }
    }
}

# Function to generate recipe with steps and timings
def generate_recipe_with_steps_and_timings(meal_type, dish_name):
    if meal_type in indian_recipes:
        recipes = indian_recipes[meal_type]
        if dish_name in recipes:
            recipe_details = recipes[dish_name]
            return dish_name, recipe_details
        else:
            return "Sorry, I don't have that dish in the {} category.".format(meal_type), {}
    else:
        return "Sorry, I don't have recipes for that meal type in Indian cuisine.", {}


# Route for index page
@app.route('/')
def index():
    return render_template('index.html')


# Route for generating recipe
@app.route('/generate_recipe', methods=['POST'])
def generate_recipe():
    meal_type = request.form['meal_type']
    dish_name = request.form['dish_name']
    recipe_details = indian_recipes[meal_type][dish_name]
    steps_with_timings = zip(recipe_details["steps"], recipe_details["timings"])
    return render_template('recipe.html', dish_name=dish_name, steps_with_timings=steps_with_timings, recipe_details=recipe_details)


if __name__ == '__main__':
    app.run(debug=True)
