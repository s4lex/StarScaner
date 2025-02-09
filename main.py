from scanner import scanner
from readImg import convert_image

filepath = "sky.png"

matrixPixels = convert_image(filepath)

countStars = scanner(matrixPixels)

print(f'Количество звезд на изображении {filepath}: {countStars}')