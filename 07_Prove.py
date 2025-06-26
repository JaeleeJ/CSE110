# 07 Prove: Assignment Milestone
# Jaelee

from PIL import Image
image_original = Image.open("penguin.jpg")


width,  height = image_original.size
print(width, height)

pixels_original = image_original.load()
r, g, b = pixels_original[100, 200]
print(r, g, b)

pixels_original[100, 200] = (255, 255, 255)
pixels_original[50, 90] = (255, 0, 255)
pixels_original[150, 60] = (255, 0, 0)
pixels_original[80, 100] = (0, 0 , 255)
pixels_original[200, 175] = (0, 255, 0)

image_original.show()
image_original.save("the_file_goes_here.jpg")

