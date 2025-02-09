from PIL import Image

def convert_image(filePath):
    img = Image.open(filePath).convert('L')
    # print(img)
    w, h = img.size
    pixels = img.load()
    # print(pixels[0,0])
    

    matrixPixels = []
    for y in range(h):
        row = []
        for x in range(w):
            row.append("1" if pixels[x,y] > 128 else "0")
        row.insert(0, "0")
        row.append("0")
        matrixPixels.append(row)
    
    matrixPixels.insert(0, ["0"] * (w + 2)) 
    matrixPixels.append(["0"] * (w + 2))
    
    return matrixPixels

convert_image("sky.png")

