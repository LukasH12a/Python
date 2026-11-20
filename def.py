# def policz_srednia(*args):
#     return sum(args) / len(args)

# print(policz_srednia(2,3,5)); print(policz_srednia(3,5,4,2))

# def wypisz_informacje(**kwargs):
#     for klucz in kwargs:
#         print(kwargs[klucz])

# a = {
#     "name": "Karo",
#     "age": 14,
#     "description": "The best gf in the world <3"
# }

# wypisz_informacje(name = "Karo",age = 14,description= "The best gf in the world <3")

def policz_wyplate(podstawa, policz_premie):
    return podstawa + policz_premie(podstawa)

def zwroc_zero(podstawa):
    return 0

def policz_premie_managera(podstawa):
    return lambda podstawa : podstawa * 0.5

print(policz_wyplate(1000, zwroc_zero))
print(policz_wyplate(1800, lambda podstawa : podstawa * 0.5))
print(policz_wyplate(3000, lambda x: x*0.25))