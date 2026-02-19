from transformers import pipeline

# создаём классификатор изображений
classifier = pipeline("image-classification")

# путь к изображению
image_path = input("Введите путь к изображению: ")

# получаем результат
result = classifier(image_path)

print("Топ-5 предсказаний:")
for item in result[:5]:
    print(item)
