# 08 Prove: Assignment
# Jaelee Hutchinson

from PIL import Image
# open and load images
image_penguin = Image.open("penguin.jpg")
image_snow = Image.open("snowscape.jpg")
image_new = Image.new("RGB", image_snow.size)
pixels_penguin = image_penguin.load()
pixels_snow = image_snow.load()
pixels_new = image_new.load()

width,  height = image_snow.size
color = pixels_penguin[1, 1]

# set colors
for x in range(0, width):
    for y in range(0, height):
        (r,g,b) = pixels_penguin[x, y]
        if r <= 200 and g >= 100 and b <= 50:
            pixels_penguin[x, y] = pixels_snow[x, y]
        elif r <= 150 and g >= 150 and b <= 100:
            pixels_penguin[x, y] = pixels_snow[x, y]

        pixels_new[x, y] = pixels_penguin[x, y]

# save and show new image
image_new.save("the_file_goes_here.jpg")
image_new.show()
