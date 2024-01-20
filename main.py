import cv2

# открываем видеозаписи и читаем к ним аннотации
camera1 = cv2.VideoCapture("data/1.avi")
with open("data/1.txt", "r") as file:
    lines = file.readlines()
    annotation1 = (line.strip() for line in lines)
camera2 = cv2.VideoCapture("data/2.avi")
with open("data/2.txt", "r") as file:
    lines = file.readlines()
    annotation2 = (line.strip() for line in lines)
camera3 = cv2.VideoCapture("data/3.avi")
with open("data/3.txt", "r") as file:
    lines = file.readlines()
    annotation3 = (line.strip() for line in lines)
camera4 = cv2.VideoCapture("data/4.avi")
with open("data/4.txt", "r") as file:
    lines = file.readlines()
    annotation4 = (line.strip() for line in lines)

# получаем общее кол-во кадров в самом маленьком видео из 4-х
frame_count = min(camera1.get(cv2.CAP_PROP_FRAME_COUNT),
                  camera2.get(cv2.CAP_PROP_FRAME_COUNT),
                  camera3.get(cv2.CAP_PROP_FRAME_COUNT),
                  camera4.get(cv2.CAP_PROP_FRAME_COUNT))
screen_annotation1 = float(annotation1.__next__())
screen_annotation2 = float(annotation2.__next__())
screen_annotation3 = float(annotation3.__next__())
screen_annotation4 = float(annotation4.__next__())

# создаём видеозаписыватели для записи видео из получившихся кадров
frameSize, fps = (1280, 720), 5
out1 = cv2.VideoWriter('new_videos/1.avi',
                       cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'),
                       fps, frameSize)
out2 = cv2.VideoWriter('new_videos/2.avi',
                       cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'),
                       fps, frameSize)
out3 = cv2.VideoWriter('new_videos/3.avi',
                       cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'),
                       fps, frameSize)
out4 = cv2.VideoWriter('new_videos/4.avi',
                       cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'),
                       fps, frameSize)

counter = 0
while counter < frame_count:
    # 4-я камера будет ведущей, т.к. она имеет наибольшее первое
    # значение аннотации
    _, camera4_image = camera4.read()
    cv2.imwrite(f"screens/camera4/{screen_annotation4} - {counter}.jpg",
                camera4_image)
    out4.write(camera4_image)
    while screen_annotation1 < screen_annotation4:
        screen_annotation1 = float(annotation1.__next__())
        _, camera1_image = camera1.read()
    cv2.imwrite(f"screens/camera1/{screen_annotation1} - {counter}.jpg",
                camera1_image)
    out1.write(camera1_image)
    while screen_annotation2 < screen_annotation4:
        screen_annotation2 = float(annotation2.__next__())
        _, camera2_image = camera2.read()
    cv2.imwrite(f"screens/camera2/{screen_annotation2} - {counter}.jpg",
                camera2_image)
    out2.write(camera2_image)
    while screen_annotation3 < screen_annotation4:
        screen_annotation3 = float(annotation3.__next__())
        _, camera3_image = camera3.read()
    cv2.imwrite(f"screens/camera3/{screen_annotation3} - {counter}.jpg",
                camera3_image)
    out3.write(camera3_image)
    counter += 1
    screen_annotation4 = float(annotation4.__next__())

camera1.release()
camera2.release()
camera3.release()
camera4.release()
out1.release()
out2.release()
out3.release()
out4.release()
cv2.destroyAllWindows()
