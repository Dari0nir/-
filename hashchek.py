import hashlib
import os
import time
from datetime import datetime

# Доступные алгоритмы хэширования
ДОСТУПНЫЕ_АЛГОРИТМЫ = {
    '1': 'md5',
    '2': 'sha1',
    '3': 'sha256',
    '4': 'sha512',
    '5': 'blake2b',
    '6': 'blake2s'
}

def вычислить_хэш_текста(текст, алгоритм='sha256'):
    """Хэширует текст выбранным алгоритмом."""
    try:
        hasher = hashlib.new(алгоритм)
        hasher.update(текст.encode())
        return hasher.hexdigest()
    except Exception as e:
        return f"❌ Ошибка: {str(e)}"

def вычислить_хэш_файла(путь_к_файлу, алгоритм='sha256'):
    """Хэширует файл выбранным алгоритмом."""
    if not os.path.exists(путь_к_файлу):
        return "❌ Файл не найден. Он в другом замке?"
    
    try:
        hasher = hashlib.new(алгоритм)
        with open(путь_к_файлу, 'rb') as файл:
            while chunk := файл.read(8192):
                hasher.update(chunk)
        return hasher.hexdigest()
    except Exception as e:
        return f"❌ Ошибка: {str(e)}"

def главное_меню():
    """Основное меню программы."""
    while True:
        print("\n⚔️  Выбери действие:")
        print("1. Хэшировать текст")
        print("2. Хэшировать файл")
        print("3. Показать доступные алгоритмы")
        print("4. Выйти")
        
        выбор = input("> ")
        
        if выбор == "1":
            текст = input("Введи текст: ")
            алгоритм = выбрать_алгоритм()
            if алгоритм:
                start_time = time.time()
                хэш = вычислить_хэш_текста(текст, алгоритм)
                elapsed = time.time() - start_time
                print(f"\n🔐 {алгоритм.upper()} хэш: {хэш}")
                print(f"⏱  Время выполнения: {elapsed:.4f} сек.")
        
        elif выбор == "2":
            путь = input("Введи путь к файлу: ")
            алгоритм = выбрать_алгоритм()
            if алгоритм:
                start_time = time.time()
                хэш = вычислить_хэш_файла(путь, алгоритм)
                elapsed = time.time() - start_time
                print(f"\n📜 {алгоритм.upper()} хэш файла: {хэш}")
                print(f"⏱  Время выполнения: {elapsed:.4f} сек.")
        
        elif выбор == "3":
            показать_алгоритмы()
        
        elif выбор == "4":
            print("🌌 Программа завершена. Тень растворяется в ночи...")
            break
        
        else:
            print("💢 Неверный выбор! Попробуй снова.")

def выбрать_алгоритм():
    """Выбор алгоритма хэширования."""
    показать_алгоритмы()
    выбор = input("Выбери номер алгоритма: ")
    if выбор in ДОСТУПНЫЕ_АЛГОРИТМЫ:
        return ДОСТУПНЫЕ_АЛГОРИТМЫ[выбор]
    else:
        print("💢 Неверный выбор алгоритма!")
        return None

def показать_алгоритмы():
    """Показывает доступные алгоритмы."""
    print("\n🔮 Доступные алгоритмы:")
    for num, name in ДОСТУПНЫЕ_АЛГОРИТМЫ.items():
        print(f"{num}. {name.upper()}")

if __name__ == "__main__":
    print("🎌 Добро пожаловать в Усовершенствованное Хэш-Додзё")
    print(f"📅 Сегодня: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    главное_меню()