from transformers import pipeline

# создаём модель распознавания речи
transcriber = pipeline("automatic-speech-recognition", model="openai/whisper-small")

# ввод пути к аудиофайлу
audio_file = input("Введите путь к аудиофайлу (.wav или .mp3): ")

# распознаём текст
result = transcriber(audio_file)

print("Распознанный текст:", result["text"])
