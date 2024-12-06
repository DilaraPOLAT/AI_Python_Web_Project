from flask import Flask, render_template, request, Response, redirect, url_for, session
import cv2
import numpy as np
import sqlite3
from werkzeug.security import check_password_hash, generate_password_hash


def get_db_connection():
    conn = sqlite3.connect("database.db")
    conn.row_factory = sqlite3.Row
    return conn
def add_user(username, password, age, salary, category, score):
    conn = get_db_connection()
    conn.execute("""
    INSERT INTO users (username, password, age, salary, category, score)
    VALUES (?, ?, ?, ?, ?, ?)
    """, (username, password, age, salary, category, score))
    conn.commit()
    conn.close()
# Örnek kullanıcı ekleme
"""add_user('user1', '01', 25, 50000, 'Müdür', 0)
add_user('user2', '012', 30, 70000, 'Yönetici', 1)
add_user('user3', '0123', 22, 40000, 'Uzman',2)
add_user('user4', '012', 35, 80000, 'Yönetici', 1)
add_user('user5', '0123', 27, 20000, 'Uzman',2)"""
conn = get_db_connection()
cursor = conn.cursor()
cursor.execute("SELECT score, password FROM users WHERE username = ?", ('Dilara',))
current_score = cursor.fetchone()
print(current_score)

cursor.execute("SELECT username,password, score FROM users")
users = cursor.fetchall()


print("Kayıtlar:")
for user in users:
    print(f"Kullanıcı Adı: {user['username']}, Puan: {user['score']},{user['password']} ")


conn.close()
