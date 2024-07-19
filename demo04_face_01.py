import os
import face_recognition
import cv2

boss_names = ['Boss']


# 读取到数据库中得人名喝面部特征
face_databases_dir = 'face_databases'

user_names = []  # 存用户姓名
user_face_encodings = []  # 存用户面部特征向量

# 得到face_databases_dir 文件夹下面所有得文件名
files = os.listdir(face_databases_dir)
num = 0
# 循环读取文件名进一步得处理
for image_shot_name in files:
    # 截取文件名得，前面那部分作为用户名存入user_names列表中
    user_name, _ = os.path.splitext(image_shot_name)
    user_names.append(user_name)

    # 读取图片文件中得面部特征信息存入user_faces_encodings 列表中
    image_file_name = os.path.join(face_databases_dir, image_shot_name)
    image_file = face_recognition.load_image_file(image_file_name)

    face_encodings = face_recognition.face_encodings(image_file)
    if face_encodings:
        user_face_encodings.append(face_encodings[0])

        # print(user_face_encodings)

# 打开摄像头 获取摄像头对象
video_capture = cv2.VideoCapture(0)  # 代表的是第一个摄像头

# 循环不停的去获取摄像头拍摄的画面，并做进一步出来
while True:
    # 还需要进一步做处理
    # 获取摄像头拍摄到的画面
    ret, frame = video_capture.read()
    # 从拍摄到画面中提取出人的脸部所在区域（可能有多个）
    face_locations = face_recognition.face_locations(frame)
    # 从所有脸部信息提取脸部特征（可能会有多个）
    face_encodings = face_recognition.face_encodings(frame, face_locations)

    # 定义属于存储拍摄到得用户得姓名得列表
    names = []

    # 遍历拍摄到特征信息 与 库里数据做比对
    for face_encoding in face_encodings:
        matchs = face_recognition.compare_faces(user_face_encodings, face_encoding)

        # user_names=[] 姓名
        name = 'Unknown'

        for index, is_match in enumerate(matchs):
            if is_match:
                name = user_names[index]
                break
        names.append(name)

    # zip
    # zip (['第一个人得位置', '第二个人得位置'],['第一个人得姓名', '第二个人得姓名'])
    # 循环遍历人的脸部所在区域。并画框
    for (top, right, bottom, left), name in zip(face_locations, names):
        color = (0, 255, 0)
        if name in boss_names:
            color = (0, 0, 255)
        # 在人像所在区域画框
        # RGB
        cv2.rectangle(frame, (left, top), (right, bottom), color, 2)
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(frame, name, (left, top - 10), font, 1, color, 2)


    # 通过opencv 把画面展示出来
    cv2.imshow('Video', frame)
    # 退出机制 输入q 退出
    if cv2.waitKey(1) & 0xFF == ord('q'):
        # 退出
        break

video_capture.release()
cv2.destroyAllWindows()
