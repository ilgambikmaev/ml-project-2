from transformers import pipeline

# создаём классификатор тональности
classifier = pipeline("sentiment-analysis")

# ввод текста пользователем
text = input("Введите текст: ")

# получаем результат
result = classifier(text)

print("Результат:", result)
