class Person:
    MALE = 'M'
    FEMALE = 'F'

    def __init__(self, name, birth_year,
                 gender, father=None, mother=None):
        self.name = name
        self.birth_year = birth_year
        self.gender = gender
        self.father = father
        self.mother = mother
        self.kids = []

        if self.father:
            self.father.kids.append(self)

        if self.mother:
            self.mother.kids.append(self)

    def children(self, gender=None):
        if gender:
            children = []
            for person in self.kids:
                if person.gender == gender:
                    children.append(person)
            return children
        else:
            return self.kids

    def get_sisters(self):
        return self.__get_siblings(self.FEMALE)

    def get_brothers(self):
        return self.__get_siblings(self.MALE)

    def is_direct_successor(self, other_person):
        return other_person in self.children()

    def __get_siblings(self, gender):
        all_siblings = list(self.mother.children() + self.father.children())
        return list(set(sibling for sibling in all_siblings
                    if sibling.gender == gender and sibling is not self))
