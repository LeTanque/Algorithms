#!/usr/bin/python
import math


def recipe_batches(recipe, ingredients):
    checklist = []
    batches_possible = 100000       # This is ghetto
    # Check if necessary ingredient names are present
    for r in recipe.keys():
        if r not in ingredients.keys():
            return 0

    # The necessary ingredients are present. Let's calculate
    # how many batches can be made.
    for s in recipe:
        if recipe.get(s) <= ingredients.get(s):
            # print("Recipe can be made", s, ":", recipe[s], ingredients[s])
            batches_with_curr_ing = ingredients.get(s) // recipe.get(s)
            if batches_with_curr_ing < batches_possible:
                batches_possible = batches_with_curr_ing
            # print('batches_with_curr_ing: \n\n', batches_with_curr_ing, "\n")
        else:
            # print("Recipe fails on -> ", s, recipe[s], ingredients[s])
            return 0

    return batches_possible





if __name__ == '__main__':
    # Change the entries of these dictionaries to test
    # your implementation with different inputs
    recipe = {'milk': 100, 'butter': 50, 'flour': 10}
    ingredients = {'milk': 198, 'butter': 52, 'flour': 10}
    print("{batches} batches can be made from the available ingredients: {ingredients}.".format(
        batches=recipe_batches(recipe, ingredients), ingredients=ingredients))
