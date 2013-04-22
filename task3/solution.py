class Person:
    family = {}

    def __init__(self, name, birth_year,
                 gender, father=None, mother=None):
        self.name = name
        self.birth_year = birth_year
        self.gender = gender
        self.father = father
        self.mother = mother
        Person.family.update({self: [father, mother, self.gender]})

    def get_sisters(self):
        sisters = []
        for key, value in Person.family.items():
            if value[2] == 'F':
                if key is not self:
                    if self.father is None:
                        if self.mother is value[1] and value[1] is not None:
                            sisters.append(key)
                    else:
                        if self.father is value[0]:
                            sisters.append(key)
                        if self.mother is value[1] and value[1] is not None:
                            if key not in sisters:
                                sisters.append(key)
        return sisters

    def get_brothers(self):
        brothers = []
        for key, value in Person.family.items():
            if value[2] == 'M':
                if key is not self:
                    if self.father is None:
                        if self.mother is value[1] and value[1] is not None:
                            brothers.append(key)
                    else:
                        if self.father is value[0]:
                            brothers.append(key)
                        if self.mother is value[1] and value[1] is not None:
                            if key not in brothers:
                                brothers.append(key)
        return brothers

    def children(self, gender=None):
        children = []
        if gender is None:
            for key, value in Person.family.items():
                if self is value[0] or self is value[1]:
                    children.append(key)
        else:
            for key, value in Person.family.items():
                if self is value[0] or self is value[1]:
                    if gender == value[2]:
                        children.append(key)
        return children

    def is_direct_successor(self, other):
        for key, value in Person.family.items():
            if (value[0] or value[1]) is self:
                if key is other:
                    return True
        return False
