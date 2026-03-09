import sqlite3
import os

# Подключаемся к базе
db_path = 'instance/database.db'
conn = sqlite3.connect(db_path)
cur = conn.cursor()

# Проверяем, есть ли колонка photo
cur.execute("PRAGMA table_info(resumes)")
columns = cur.fetchall()
column_names = [col[1] for col in columns]

print("📋 Существующие колонки:", column_names)

if 'photo' not in column_names:
    try:
        # Добавляем колонку photo
        cur.execute('ALTER TABLE resumes ADD COLUMN photo TEXT')
        print("✅ Колонка 'photo' добавлена")
    except Exception as e:
        print(f"❌ Ошибка: {e}")
else:
    print("✅ Колонка 'photo' уже существует")

conn.commit()
conn.close()