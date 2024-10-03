class animal:
    def __init__(self, name, genus, year_of_birth):
        self.name = name
        self.genus = genus
        self.year_of_birth = year_of_birth
def file_animals(animals, filename):
    with open(filename, 'w') as file:
        for animal in animals:
            file.write(f"{animal.name} - {animal.genus}\n")
animals = [
    animal("King", "lion", 2010),
    animal("Sharik", "dog", 2015),
    animal("Gringo", "hog", 2011),
    animal("Tom", "cat", 2018),
    animal("Jerry", "mouse", 2022)
]
filename = "animal_name_genus.txt"
file_animals(animals, filename)