# ЗАДАЧА №4
# Приведем плейлист песен в виде списка списков
# Cписок my_favorite_songs содержит список названий и длительности треков
import random

my_favorite_songs = [
    ["Waste a moment", 3.03],
    ["New Salvation", 4.02],
    ["Staying\' Alive", 3.40],
    ["Out of touch", 3.03],
    ["A Sorta Fairytale", 5.28],
    ["Easy", 4.15],
    ["Beautiful day", 4.04],
    ["Nowhere to Run", 2.58],
    ["In This World", 4.02]

]

# print("Три случайные песни -", random.choices(my_favorite_songs, k=3))
# "Easy", 4.15
# "Waste a moment", 3.03
# "Staying\' Alive", 3.40 

easy_song = my_favorite_songs[5][1]
waste_song = my_favorite_songs[0][1]
staying_song = my_favorite_songs[2][1]
summa_songs = easy_song + waste_song + staying_song
print("Три песни звучат -", summa_songs, "минут")

# Выведите общее время звучания трех случайных песен в формате
# Три песни звучат ХХХ минут
# Для того, чтобы задавать случайные значения, используйте модуль random
# import random

