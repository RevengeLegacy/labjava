import os
import sys
import math
import random
import platform
from datetime import datetime

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Простой многофункциональный скрипт — "любой код"
# Содержит: мини-калькулятор, заметки, случайная цитата и информация о системе.


NOTES_FILE = "notes.txt"
QUOTES = [
    "Ученье — свет, а неученье — тьма.",
    "Лучше делать и сожалеть, чем не делать и жалеть.",
    "Код, который читают люди, важнее кода, который выполняют машины.",
    "Маленькие шаги каждый день ведут к большим результатам.",
]

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def show_menu():
    print("=== Простой инструмент ===")
    print("1) Калькулятор (выражение)")
    print("2) Добавить заметку")
    print("3) Просмотреть заметки")
    print("4) Случайная цитата")
    print("5) Информация о системе")
    print("0) Выйти")
    print()

def calc():
    expr = input("Введите арифметическое выражение (напр. 2+3*4): ").strip()
    if not expr:
        print("Пустое выражение.")
        return
    try:
        # Безопаснее: разрешаем только цифры и базовые операторы/скобки/точку/пробел
        allowed = "0123456789+-*/(). %eE"
        if any(ch not in allowed for ch in expr):
            raise ValueError("Недопустимые символы в выражении.")
        result = eval(expr, {"__builtins__": None}, {"math": math})
        print("Результат:", result)
    except Exception as e:
        print("Ошибка вычисления:", e)

def add_note():
    note = input("Текст заметки: ").strip()
    if not note:
        print("Заметка пуста, отмена.")
        return
    timestamp = datetime.now().isoformat(sep=' ', timespec='seconds')
    line = f"{timestamp} — {note}\n"
    with open(NOTES_FILE, "a", encoding="utf-8") as f:
        f.write(line)
    print("Заметка сохранена.")

def view_notes():
    if not os.path.exists(NOTES_FILE):
        print("Файл заметок не найден.")
        return
    print("=== Заметки ===")
    with open(NOTES_FILE, "r", encoding="utf-8") as f:
        for i, line in enumerate(f, 1):
            print(f"{i}: {line.rstrip()}")
    print("=== Конец заметок ===")

def random_quote():
    print(random.choice(QUOTES))

def sys_info():
    print("Платформа:", platform.system(), platform.release())
    print("Python:", platform.python_version())
    print("Текущая директория:", os.getcwd())
    try:
        print("Пользователь:", os.getlogin())
    except Exception:
        # os.getlogin может падать в некоторых окружениях
        print("Пользователь: (не определён)")

def main():
    while True:
        show_menu()
        choice = input("Выберите опцию: ").strip()
        if choice == "1":
            calc()
        elif choice == "2":
            add_note()
        elif choice == "3":
            view_notes()
        elif choice == "4":
            random_quote()
        elif choice == "5":
            sys_info()
        elif choice == "0":
            print("Выход.")
            break
        else:
            print("Неизвестная опция.")
        input("\nНажмите Enter, чтобы продолжить...")
        clear_screen()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nПрервано пользователем.")