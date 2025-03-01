percentage_maznini = int(input())
percentage_protein = int(input())
percentage_vuglehidrati = int(input())
calorii = int(input())
percentage_water = int(input())

grams_maznini = (percentage_maznini * calorii/ 100) / 9
# print(grams_maznini)
grams_protein = (percentage_protein * calorii / 100) / 4
# print(grams_protein)
grams_vuglehidrati = (percentage_vuglehidrati * calorii /100) / 4
# print(grams_vuglehidrati)

grams_food = grams_protein + grams_vuglehidrati + grams_maznini
# print(grams_food)
calorii_per_gram = calorii / grams_food
# print(calorii_per_gram)

# print(percentage_water)
calorii_per_gram_natur = calorii_per_gram * (100 - percentage_water) / 100
# print(calorii_per_gram_natur)
print(f"{calorii_per_gram_natur:.4f}")