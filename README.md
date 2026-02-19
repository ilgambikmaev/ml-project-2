# ML Project — 4 типа задач

## Задача 1: Текст
- Модель: distilbert-base-uncased-finetuned-sst-2-english
- Задача: анализ тональности
- Пример вывода:
  Текст: "I love programming"
  Результат: [{'label': 'POSITIVE', 'score': 0.9998}]

## Задача 2: Аудио
- Модель: Wav2Vec2 (HuggingFace)
- Задача: распознавание речи

## Задача 3: Изображения
- Модель: google/vit-base-patch16-224
- Задача: классификация изображения
- Пример вывода:
  [{'label': 'tabby cat', 'score': 0.95}]

## Задача 4: Видео
- Модель: facebook/detr-resnet-50
- Задача: детекция объектов на первом кадре видео
- Пример вывода:
  {'score': 0.9537, 'label': 'bowl', 'box': {'xmin': 125, 'ymin': 20, 'xmax': 352, 'ymax': 250}}

## Как запускать
1. Активировать виртуальное окружение:
venv\Scripts\activate
2. Установить библиотеки:
pip install -r requirements.txt
3. Запускать скрипты:
python text.py
python audio.py
python image.py
python video.py