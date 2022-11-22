# ЗАДАЧА 6
# Есть словарь песен
my_favorite_songs = {
     "Waste a Moment": 3.03,
     "New Salvation": 4.02, 
     "Staying\' Alive": 3.40,
     "Out of Touch": 3.03,
     "A Sorta Fairytale": 5.28,
     "Easy": 4.15,
     "Beautiful Day": 4.04,
     "Nowhere to Run": 2.58,
     "In This World": 4.02
}

# Для того, чтобы использовать random.choice необходимо преобразовать словарь в список
# Преобразуем словарь my_favorite_songs в список
my_favorite_songs_list = [[key, value] for key, value in my_favorite_songs.items()]

import random

# print("Три случайные песни -", random.choices(my_favorite_songs_list, k = 3))

# Три случайные песни выпали случайным образом:
# "A Sorta Fairytale: 5.28, 
# "New Salvation: 4.02", 
# "Beautiful Day: 4.04"

sorta_song = my_favorite_songs_list[4][1]
new_song = my_favorite_songs_list[1][1]
beautiful_song = my_favorite_songs_list[6][1]
three_songs = sorta_song + new_song + beautiful_song
print("Три песни звучат -", three_songs,"минут")

# Распечатайте общее время звучания трех случайных песен
# Вывод: Три песни звучат ХХХ минут.


