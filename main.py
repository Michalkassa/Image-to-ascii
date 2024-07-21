from PIL import Image
import numpy as np
print(Image.__version__)
print(np.__version__)
compression = 0.3

image = Image.open(r"./input/image.jpg")
w,h = image.size
new_image = image.resize((int(w * compression), int(h * compression)))
new_image.save('./input/myimage_compressed.jpg')
a = np.asarray(new_image)

characters = [
    "## " ,
    "XX " ,
    "%% " ,
    "&& " ,
    "** " ,
    "++ " ,
    "// " ,
    "(( " ,
    "'' " ,
]
w,h = new_image.size

constriction = min(w,h)
output = []

for i, row in enumerate(a):
    r = []
    for col in row:
        s = col.sum()
        if s == 0 :
            r.append(characters[0])
        if s in range(0,100):
            r.append(characters[1])
        if s in range(100,200) :
            r.append(characters[2])
        if s in range(200,300) :
            r.append(characters[3])
        if s in range(300,400) :
            r.append(characters[4])
        if s in range(400,500) :
            r.append(characters[5])
        if s in range(500,600) :
            r.append(characters[6])
        if s in range(600,700) :
            r.append(characters[7])
        if s in range(700,800) :
            r.append(characters[8])
    print(f"{(i/h) * 100}%")
    output.append(r)


out = open("./output/output.txt", "w")
for row in output:
    out.write("".join(row)+"\n")