# Excel to SQLite Synchronization Tool 🔄
# Инструмент синхронизации Excel с SQLite 🔄

## Overview 📋
## Обзор 📋
This tool provides seamless synchronization between Excel workbooks and SQLite databases, specifically designed for managing metallurgical casting data. It handles complex data structures including casting information, sector details, and multiple participants.

Этот инструмент обеспечивает бесперебойную синхронизацию между файлами Excel и базами данных SQLite, специально разработан для управления металлургическими данными о плавках. Он обрабатывает сложные структуры данных, включая информацию о плавках, детали секторов и нескольких участников процесса.

## Features ⭐
## Возможности ⭐
- **Reliable Data Transfer**: Accurately transfers data from Excel to SQLite
- **Smart Data Type Handling**: Properly manages dates, times, numbers, and text
- **Error Resilient**: Continues processing despite individual record errors
- **Data Integrity**: Maintains referential integrity through foreign key relationships
- **Idempotent Operations**: Safely handles multiple runs without data duplication

- **Надежная передача данных**: Точно переносит данные из Excel в SQLite
- **Умная обработка типов данных**: Правильно управляет датами, временем, числами и текстом
- **Устойчивость к ошибкам**: Продолжает обработку несмотря на ошибки в отдельных записях
- **Целостность данных**: Поддерживает ссылочную целостность через внешние ключи
- **Идемпотентные операции**: Безопасно обрабатывает многократные запуски без дублирования данных

## Database Structure 🗄️
## Структура базы данных 🗄️

### Tables
### Таблицы

#### Plavki (Main Castings Table)
#### Плавки (Основная таблица)
- `id`: Unique identifier (TEXT)
- `uchet_number`: Accounting number
- `date`: Casting date
- `plavka_number`: Casting number
- `cluster_number`: Cluster number
- `senior_shift`: Senior shift supervisor
- `participant1-4`: Shift participants
- `casting_name`: Name of casting
- `experiment_type`: Type of experiment
- `comment`: Additional notes

- `id`: Уникальный идентификатор (ТЕКСТ)
- `uchet_number`: Учетный номер
- `date`: Дата плавки
- `plavka_number`: Номер плавки
- `cluster_number`: Номер кластера
- `senior_shift`: Старший смены
- `participant1-4`: Участники смены
- `casting_name`: Наименование отливки
- `experiment_type`: Тип эксперимента
- `comment`: Дополнительные заметки

#### Sectors
#### Сектора
- `id`: Auto-incrementing identifier
- `plavka_id`: Reference to main casting
- `sector_name`: Sector identifier (A, B, C, D)
- `sector_number`: Sector number
- `heating_time`: Ladle heating time
- `movement_time`: Movement time
- `pouring_time`: Pouring time
- `temperature`: Pouring temperature

- `id`: Автоинкрементный идентификатор
- `plavka_id`: Ссылка на основную плавку
- `sector_name`: Идентификатор сектора (A, B, C, D)
- `sector_number`: Номер сектора
- `heating_time`: Время прогрева ковша
- `movement_time`: Время перемещения
- `pouring_time`: Время заливки
- `temperature`: Температура заливки

## Requirements 📦
## Требования 📦
- Python 3.x
- pandas
- openpyxl

Install dependencies:
Установка зависимостей:
```bash
pip install -r requirements.txt
```

## Usage 🚀
## Использование 🚀

### 1. Database Setup
### 1. Настройка базы данных
Initialize the database structure:
Инициализация структуры базы данных:
```bash
python create_db.py
```

### 2. Data Synchronization
### 2. Синхронизация данных
Run the synchronization script:
Запуск скрипта синхронизации:
```bash
python sync_script.py
```

## File Structure 📁
## Структура файлов 📁
```
.
├── create_db.py      # Database initialization / Инициализация базы данных
├── sync_script.py    # Synchronization logic / Логика синхронизации
├── requirements.txt  # Python dependencies / Зависимости Python
├── plavka.xlsx      # Source Excel file / Исходный файл Excel
└── plavka.db        # SQLite database / База данных SQLite
```

## Error Handling 🛠️
## Обработка ошибок 🛠️
- The tool logs errors for individual records
- Continues processing despite individual failures
- Maintains data consistency

- Инструмент логирует ошибки для отдельных записей
- Продолжает обработку несмотря на отдельные сбои
- Поддерживает согласованность данных

## Best Practices 💡
## Лучшие практики 💡
1. Keep regular backups of your Excel file
2. Run synchronization regularly to maintain data consistency
3. Monitor error logs for potential data issues
4. Validate source data before synchronization

1. Регулярно делайте резервные копии файла Excel
2. Регулярно запускайте синхронизацию для поддержания согласованности данных
3. Отслеживайте журналы ошибок для выявления потенциальных проблем
4. Проверяйте исходные данные перед синхронизацией

## Contributing 🤝
## Участие в разработке 🤝
Feel free to submit issues and enhancement requests!

Не стесняйтесь отправлять сообщения об ошибках и предложения по улучшению!

## License 📄
## Лицензия 📄
This project is licensed under the MIT License - see the LICENSE file for details.

Этот проект лицензирован под MIT License - подробности см. в файле LICENSE.

---
Made with ❤️ for metallurgical data management

Сделано с ❤️ для управления металлургическими данными