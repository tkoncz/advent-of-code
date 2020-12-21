with open("inputs/day_21_allergen_assessment_input.txt", "r") as input:
    lines = input.read().rstrip().split('\n')

# part 1
ingredients_list = []
all_allergens = set()
for l in lines:
    ingredients = l.split(' (contains ')[0].split(' ')
    allergens   = l.split(' (contains ')[1].replace(')', '').split(', ')
    ingredients_list.append({
        'ingredients': ingredients,
        'allergens': allergens
    })
    all_allergens = set(list(all_allergens) + allergens)

all_allergens = list(all_allergens)

allergens_w_ingredients = {}
for allergen in all_allergens:
    ingredients_w_allergen = []
    for row in ingredients_list:
        ingredients = row['ingredients']
        allergens   = row['allergens']

        if allergen in allergens:
            ingredients_w_allergen.append(ingredients)

    allergens_w_ingredients[allergen] = ingredients_w_allergen


common_ingredients_for_allergens = {}
for allergen, ingredients in allergens_w_ingredients.items():

    for i in range(0, len(ingredients)):
        if i == 0:
            common_ingredients = set(ingredients[0])
        else:
            common_ingredients = common_ingredients & set(ingredients[i])

    unique_ingredients = list(common_ingredients)
    common_ingredients_for_allergens[allergen] = unique_ingredients

all_ingredients = [ingredients['ingredients'] for ingredients in ingredients_list]
unique_ingredients = []
for ingredients in all_ingredients:
    unique_ingredients = list(set(unique_ingredients + ingredients))

unsafe_ingredients = []
for ingredients in common_ingredients_for_allergens.values():
    unsafe_ingredients = list(set(unsafe_ingredients + ingredients))

# ----
safe_ingredients = set(unique_ingredients) - set(unsafe_ingredients)

answer = 0
for safe_ingredient in safe_ingredients:
    for ingredients in ingredients_list:
        if safe_ingredient in ingredients['ingredients']:
            answer += 1

print(answer)
# 2078

# part 2

# TODO! solved manually

# lmcqt,kcddk,npxrdnd,cfb,ldkt,fqpt,jtfmtpd,tsch
