import pandas as pd
import sqlite3
from datetime import datetime
import os

def connect_to_db():
    """Create a connection to SQLite database"""
    conn = sqlite3.connect('plavka.db')
    conn.execute('PRAGMA foreign_keys = ON')
    return conn

def read_excel_data():
    """Read data from Excel file"""
    return pd.read_excel('plavka.xlsx')

def convert_time(time_value):
    """Convert time values to string format"""
    if pd.isna(time_value):
        return None
    if isinstance(time_value, str):
        return time_value
    try:
        if isinstance(time_value, datetime):
            return time_value.strftime('%H:%M:%S')
        return str(time_value)
    except:
        return None

def convert_date(date_value):
    """Convert date values to string format YYYY-MM-DD"""
    if pd.isna(date_value):
        return None
    try:
        if isinstance(date_value, str):
            return date_value
        if isinstance(date_value, datetime):
            return date_value.strftime('%Y-%m-%d')
        return str(date_value)
    except:
        return None

def convert_float(value):
    """Convert float values, handling NaN"""
    if pd.isna(value):
        return None
    try:
        return float(value)
    except:
        return None

def convert_id(id_value):
    """Convert ID values to string, handling NaN"""
    if pd.isna(id_value):
        return None
    return str(id_value).strip()

def sync_data():
    # Connect to database
    conn = connect_to_db()
    cursor = conn.cursor()
    
    # Read Excel data
    df = read_excel_data()
    
    # Process each row in the Excel file
    for _, row in df.iterrows():
        try:
            # Convert ID to string format
            plavka_id = convert_id(row['ID'])
            if not plavka_id:
                print(f"Skipping row with empty ID")
                continue
                
            # Insert into plavki table
            cursor.execute("""
                INSERT OR REPLACE INTO plavki (
                    id, uchet_number, date, plavka_number, cluster_number,
                    senior_shift, participant1, participant2, participant3, participant4,
                    casting_name, experiment_type, comment
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                plavka_id,
                str(row['Учетный_номер']) if pd.notna(row['Учетный_номер']) else None,
                convert_date(row['Плавка_дата']),
                str(row['Номер_плавки']) if pd.notna(row['Номер_плавки']) else None,
                str(row['Номер_кластера']) if pd.notna(row['Номер_кластера']) else None,
                str(row['Старший_смены_плавки']) if pd.notna(row['Старший_смены_плавки']) else None,
                str(row['Первый_участник_смены_плавки']) if pd.notna(row['Первый_участник_смены_плавки']) else None,
                str(row['Второй_участник_смены_плавки']) if pd.notna(row['Второй_участник_смены_плавки']) else None,
                str(row['Третий_участник_смены_плавки']) if pd.notna(row['Третий_участник_смены_плавки']) else None,
                str(row['Четвертый_участник_смены_плавки']) if pd.notna(row['Четвертый_участник_смены_плавки']) else None,
                str(row['Наименование_отливки']) if pd.notna(row['Наименование_отливки']) else None,
                str(row['Тип_эксперемента']) if pd.notna(row['Тип_эксперемента']) else None,
                str(row['Комментарий']) if pd.notna(row['Комментарий']) else None
            ))
            
            # Process sectors A, B, C, D
            sectors = ['A', 'B', 'C', 'D']
            for sector in sectors:
                sector_number = row[f'Сектор_{sector}_опоки']
                if pd.notna(sector_number):  # Check if sector exists
                    cursor.execute("""
                        INSERT OR REPLACE INTO sectors (
                            plavka_id, sector_name, sector_number,
                            heating_time, movement_time, pouring_time, temperature
                        ) VALUES (?, ?, ?, ?, ?, ?, ?)
                    """, (
                        plavka_id,
                        sector,
                        int(sector_number) if pd.notna(sector_number) else None,
                        convert_time(row[f'Плавка_время_прогрева_ковша_{sector}']),
                        convert_time(row[f'Плавка_время_перемещения_{sector}']),
                        convert_time(row[f'Плавка_время_заливки_{sector}']),
                        convert_float(row[f'Плавка_температура_заливки_{sector}'])
                    ))
        except Exception as e:
            print(f"Error processing row with ID {row['ID']}: {str(e)}")
            continue
    
    # Commit changes and close connection
    conn.commit()
    conn.close()

if __name__ == "__main__":
    try:
        sync_data()
        print("Synchronization completed successfully!")
    except Exception as e:
        print(f"An error occurred: {str(e)}")
