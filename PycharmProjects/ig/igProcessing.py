import cv2

img = cv2.imread(r"C:\Users\malic\Downloads\igPic.png")

color = [101, 52, 152] # 'cause purple!

# border widths; I set them all to 150
top, bottom, left, right = [0, 0, 60, 10]

img_with_border = cv2.copyMakeBorder(img, top, bottom, left, right, cv2.BORDER_REPLICATE)
cv2.namedWindow('image', cv2.WINDOW_NORMAL)
cv2.imshow('image',img_with_border)
cv2.waitKey(0)
cv2.destroyAllWindows()


x=4
LST = [1,2,3,4]
LST = list(range(4*len(LST))
hash(5)



print(LST)