import cv2
from PIL import Image
from transformers import pipeline

# создаём детектор объектов
detector = pipeline("object-detection")

# вводим путь к видео
video_path = input("Введите путь к видеофайлу (.mp4, .avi): ")

# открываем видео
cap = cv2.VideoCapture(video_path)
ret, frame = cap.read()
cap.release()

if not ret:
    print("Не удалось прочитать кадр из видео")
else:
    # конвертируем кадр в PIL Image
    frame_pil = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))

    # детекция объектов
    result = detector(frame_pil)

    # выводим первые 5 объектов
    print("Найденные объекты (топ-5):")
    for obj in result[:5]:
        print(obj)
