import sqlite3
import os

# Подключаемся к базе
conn = sqlite3.connect('instance/database.db')
cur = conn.cursor()

# Добавляем колонку user_id в таблицу resumes
try:
    cur.execute('ALTER TABLE resumes ADD COLUMN user_id INTEGER')
    print("✅ Колонка user_id добавлена")
except:
    print("❌ Колонка уже существует")

# Проверяем структуру таблицы
cur.execute("PRAGMA table_info(resumes)")
columns = cur.fetchall()
print("\n📋 Структура таблицы resumes:")
for col in columns:
    print(f"  {col[1]} - {col[2]}")

conn.commit()
conn.close()