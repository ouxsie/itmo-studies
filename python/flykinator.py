# This is my final for the first-year Intro to Python I class. The idea is to adjust binary search algorytm for the purposes of some kind of an IDE chat-bot like Akinator. 
# I made it about planes, therefore, it is named Flykinator. I took this class online without much support from the professor. 100/100, 5A for the class. And I'm sorry, this one's fully in Russian.

a = [0, 'Ан-2М', 2, 'Harbin Y-12', 4, 'Ил-18ГрМ', 6, 'Ан-22 Антей', 8, 'Як-40ДТС', 10, 'Ан-72', 12, 'Ил-96-400Т', 14, 'Ан-124 Руслан', 16,
     'Cessna 408', 18, 'CASA CN-235', 20, 'Lockheed L-1049D', 22, 'Hughes H-4 Hercules', 24, 'Embraer E-190F', 26, 'Grumman EA-6B', 28,
     'McDonnell Douglas MD-11F', 30, 'Lockheed C-5 Galaxy', 32, 'Ил-114', 34, 'Ан-2', 36, 'Ту-114', 38, 'Ту-116', 40, 'Ту-104', 42, 'Як-40 ВИП', 44,
     'COMAC C929', 46, 'Ил-96-300ПУ', 48, 'Bombardier Dash Q-400', 50, 'Beechcraft King Air 350', 52, 'Lockheed Constellation', 54,
     'Piaggio P180 Avanti', 56, 'Airbus A220', 58, 'Embraer Phenom 300', 60, 'Boeing 787', 62, 'Dassault Falcon 8X']

mid = len(a) // 2
low = 0
high = len(a)

# функции для сокращения области поиска, чтоб постоянно не прописывать их в коде
def negative():
    global high, low, mid
    eq_high = high
    eq_low = low
    eq_mid = mid
    eq_high = eq_mid
    eq_mid = (eq_low + eq_high) // 2
    if eq_high > eq_low:
        high = eq_high
        low = eq_low
        mid = eq_mid
    else:
        eq_high = high
        eq_low = low
        eq_mid = mid



def positive():
    global high, low, mid
    eq_high = high
    eq_low = low
    eq_mid = mid
    eq_low = eq_mid
    eq_mid = (eq_low + eq_high) // 2
    if eq_high > eq_low:
        high = eq_high
        low = eq_low
        mid = eq_mid
    else:
        eq_high = high
        eq_low = low
        eq_mid = mid


# Ввиду специфики проекта, почти все вопросы будут одинаковыми для двух веток,
# так что ниже они будут написаны в качестве переменных, просто чтобы не хахламлять код.
origin = 'Самолёт создан в западных странах (ЕС, США, Канада, Бразилия)?'
engines = 'У самолёта реактивные двигатели?'
fl_duration = 'Самолёт рассчитан на длинные полёты? Больше 3 часов'

# вопросы для определения самолёта
print('Здравствуйте! Двавйте поиграем во Флайкинатор.')
print('Я буду задавать вопросы, вы будете на них отвечать, а я буду выдавать интересный (не боевой!) самолёт.')
print(
    'К сожалению, для такого бинарного проекта создатель достаточно ограничен в выборе самолётов, будьте к этому готовы.')
print(
    'Если вы напишете 1 - то это ответ "да", 0 - то "нет". Начнём!')
print('Самолёт пассажиирский?')

flag = True

while flag:

    value = int(input())

    # если самолёт грузовой - идём по "левой ветке"
    if value == 0:
        negative()
        print(origin)

        value = int(input())

        if value == 0 or value == 1:
            if value == 0:
                negative()
            elif value == 1:
                positive()
            print(engines)

            value = int(input())

            if value == 0 or value == 1:
                if value == 0:
                    negative()
                elif value == 1:
                    positive()
                print(fl_duration)

                value = int(input())

                if value == 0 or value == 1:
                    if value == 0:
                        negative()
                    elif value == 1:
                        positive()
                    print('Самолёт используется в основном в вооружённых силах?')

                    value = int(input())

                    if value == 0 or value == 1:
                        if value == 0:
                            negative()
                        elif value == 1:
                            positive()
                        flag = False
                        break

    # если самолёт пассажирский - идём по "правой ветке"
    elif value == 1:
        positive()
        print(origin)

        value = int(input())

        if value == 0 or value == 1:
            if value == 0:
                negative()
            elif value == 1:
                positive()
            print(engines)

            value = int(input())

            if value == 0 or value == 1:
                if value == 0:
                    negative()
                elif value == 1:
                    positive()
                print(fl_duration)

                value = int(input())

                if value == 0 or value == 1:
                    if value == 0:
                        negative()
                    elif value == 1:
                        positive()
                    print('В основном самолёт используется в частных авиаперевозках? (Бизнес-джет)')

                    value = int(input())

                    if value == 0 or value == 1:
                        if value == 0:
                            negative()
                        elif value == 1:
                            positive()
                            flag = False
                            break

print('Поздравляю! В этом массиве вы нашли', a[mid])
