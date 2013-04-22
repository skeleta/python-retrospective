def what_is_my_sign(day, month):
    if month == 12 and day in range(22, 31+1) or month == 1 and day in range(1, 19+1):
        return "Козирог"
    elif month == 1 and day in range(20, 31+1) or month == 2 and day in range(1, 18+1):
        return "Водолей"
    elif month == 2 and day in range(19, 29+1) or month == 3 and day in range(1, 20+1):
        return "Риби"
    elif month == 3 and day in range(21, 31+1) or month == 4 and day in range(1, 20+1):
        return "Овен"
    elif month == 4 and day in range(21, 30+1) or month == 5 and day in range(1, 20+1):
        return "Телец"
    elif month == 5 and day in range(21, 31+1) or month == 6 and day in range(1, 20+1):
        return "Близнаци"
    elif month == 6 and day in range(21, 30+1) or month == 7 and day in range(1, 21+1):
        return "Рак"
    elif month == 7 and day in range(22, 31+1) or month == 8 and day in range(1, 22+1):
        return "Лъв"
    elif month == 8 and day in range(23, 31+1) or month == 9 and day in range(1, 22+1):
        return "Дева"
    elif month == 9 and day in range(23, 30+1) or month == 10 and day in range(1, 22+1):
        return "Везни"
    elif month == 10 and day in range(23, 31+1) or month == 11 and day in range(1, 21+1):
        return "Скорпион"
    elif month == 11 and day in range(22, 30+1) or month == 12 and day in range(1, 21+1):
        return "Стрелец"
