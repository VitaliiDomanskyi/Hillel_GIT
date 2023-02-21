import os


if not os.path.exists("film_storage"):
    os.mkdir("film_storage")

for i in range(65, 91):
    letter = chr(i)
    if not os.path.exists(f"film_storage/{letter}"):
        os.mkdir(f"film_storage/{letter}")