# ЗАДАЧА № 2

# Создайте список "города" с именами любых городов
# Количестов элементов в списке "города" не меньше 3!
from pprint import pprint

сities = [
       "Рим", 
       "Барселона",
       "Прага", 
       "Москва",
       "Париж"
       
]

# Создайте список списков населения перечисленных городов
 
population_of_cities = [
       ["Рим", 2758454],
       ["Барселона", 1636732],
       ["Прага", 1275406],
       ["Москва", 12455682],
       ["Париж", 2148327]
]


# Выведите на консоль население второго города в формате                                                                                                          
# Население Москвы - ХХ человек

print("Население второго города -", population_of_cities[1:2], "человек")

# Выведите на консоль общий размер населения перечисленных городов
# Итого размер населения -ХХ человек

all_size = population_of_cities[0][1] + population_of_cities[1][1] + population_of_cities[2][1] + \
           population_of_cities[3][1] + population_of_cities[4][1]
print("Итого размер населения -", all_size, "человек")
                                                   