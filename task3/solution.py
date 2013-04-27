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

    def is_direct_successor(self, other):
        for key, value in Person.family.items():
            if (value[0] or value[1]) is self:
                if key is other:
                    return True
        return False
