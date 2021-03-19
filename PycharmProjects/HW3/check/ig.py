import cv2

img = cv2.imread(r"C:\Users\malic\Downloads\igPic.png")

color = [101, 52, 152] # 'cause purple!

# border widths; I set them all to 150
top, bottom, left, right = [150]*4

img_with_border = cv2.copyMakeBorder(img, top, bottom, left, right, cv2.BORDER_CONSTANT, value=color)