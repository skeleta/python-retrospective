SIGNS = ("Козирог", "Водолей", "Риби", "Овен", "Телец", "Близнаци",
         "Рак", "Лъв", "Дева", "Везни", "Скорпион", "Стрелец")

RANGES = {1: 19, 2: 18, 3: 20, 4: 20, 5: 20, 6: 20,
          7: 21, 8: 22, 9: 22, 10: 22, 11: 21, 12: 21}


def what_is_my_sign(day, month):
    return SIGNS[month - 12 - (day <= RANGES[month])]
