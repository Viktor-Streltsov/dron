import cv2

img_file = "./berds.jpg"
img = cv2.imread(img_file, cv2.IMREAD_GRAYSCALE)


title = "IMG"
x, y = 100, 100

while True:
    cv2.imshow(title, img)
    cv2.moveWindow(title, x, y)
    key = cv2.waitKey(0) & 0xFF
    print(key, chr(key))

    if key == ord("a"):
        x -= 10
    elif key == ord("s"):
        y += 10
    elif key == ord("w"):
        y -= 10
    elif key == ord("d"):
        x += 10
    elif key == ord("q") or key == 27:
        break

cv2.destroyAllWindows()