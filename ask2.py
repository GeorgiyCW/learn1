def discounted(цена, скидка, max_скидка=20): 
    try:
        цена = abs(float(цена))
        скидка = abs(float(скидка))
        max_скидка = abs(float(max_скидка))
    except ValueError:
        return 'ОШИБКА'
    if max_скидка > 99:
        return 'Слишком большая'
    elif скидка >= max_скидка:
        return цена
    else:
        return цена - (цена * скидка / 100)


print(discounted(100, 'Zero'))
