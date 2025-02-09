import readImg

def counting_stars(scan_mas):
    count = 0
    for i in scan_mas:
        if i == '1':
           count += 1 
    return count

def scanner(mas):
    x1, x2 = 0, 1
    y1, y2 = 0, 1
    count_N, count_M = 0, 0

    while True:
        scan_mas = mas[y1][x1] + mas[y1][x2] + mas[y2][x1] + mas[y2][x2]
        count = counting_stars(scan_mas)
        x1 += 1 
        x2 += 1
        if count == 1:
           count_N += 1 
        if count == 3:
           count_M += 1
        if x2 == len(mas[-1]):
            x1, x2 = 0, 1
            y1 += 1
            y2 += 1
            if y2 == len(mas):
                break 
    return (count_N - count_M) / 4

