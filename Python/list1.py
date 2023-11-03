foods = ["pizza", "salad", "hamburger", "steak", "apple", "orange"]

def display_list(label, foods):
    print(label)
    for food in foods:
        print(food)

display_list("foods in original order:", foods)

foods.sort()
display_list("foods in ascending alphabetical order:", foods)

foods.sort(reverse=True)
display_list("foods in descending alphabetical order:", foods)


foods2 = sorted(foods)
display_list("foods2 in ascending alphabetical order", foods2)

display_list("foods still in descending alphabetical order", foods)


foods.reverse()

display_list("foods in ascending alphabetical order:", foods)

foods.append("carrots")
foods.append("milk")

display_list("sorted foods with carrots and milk appended to the end:", foods)

foods.sort()

display_list("foods in ascending alphabetical order:", foods)

pizza_index = foods.index("pizza")

print(f"Pizza is at {pizza_index}")

foods.insert(pizza_index, "fries")

pizza_index = foods.index("pizza")

print(f"Pizza is now at {pizza_index}")

