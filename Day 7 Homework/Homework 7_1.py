for year in range(8, 2027):
    if year % 4 != 0:
        continue

    if year % 100 == 0:
        if year % 400 != 0:
            continue

    print(year)


    