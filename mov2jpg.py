import cv2

vidcap = cv2.VideoCapture(IMG_0179.mov)

success,image = vidcap.read()
count = 0
while success: 
    print("%03d" % count)
    cv2.imwrite("IMG_0179_frame%03d.jpg" % count, image)     # save frame as JPEG file  
    success,image = vidcap.read()
    print('Read a new frame: ', success)
    count += 1

print(f'totally {count} frames.')
