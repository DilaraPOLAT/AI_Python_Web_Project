from flask import Flask, render_template, request, Response, redirect, url_for, session
import cv2
import numpy as np
import sqlite3
from werkzeug.security import check_password_hash, generate_password_hash
from collections import Counter
app = Flask(__name__)
app.secret_key = 'my_secret_key'  


camera = cv2.VideoCapture(0)


def get_db_connection():
    conn = sqlite3.connect("database.db")
    conn.row_factory = sqlite3.Row
    return conn

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')


def euclidean_distance(x1, x2):
    return np.sqrt(np.sum((x1 - x2) ** 2))

class KNN:
    def __init__(self, k=3):
        self.k = k

    def fit(self, X, y):

        self.X_train = X
        self.y_train = y

    def predict(self, X):

        return np.array([self._predict(x) for x in X])

    def _predict(self, x):

        distances = [euclidean_distance(x, x_train) for x_train in self.X_train]
        k_indices = np.argsort(distances)[:self.k]
        k_nearest_labels = [self.y_train[i] for i in k_indices]
        most_common = Counter(k_nearest_labels).most_common(1)
        return most_common[0][0]

def train_knn_model():
    conn = get_db_connection()
    users = conn.execute('SELECT age, salary, category FROM users').fetchall()
    conn.close()

    X = np.array([[user['age'], user['salary']] for user in users])
    y = np.array([user['category'] for user in users])

    test_size = int(0.3 * len(X))  # %30 test verisi
    indices = np.arange(len(X))
    np.random.shuffle(indices)  # Veriyi karıştır
    train_indices = indices[:-test_size]
    test_indices = indices[-test_size:]

    X_train, X_test = X[train_indices], X[test_indices]
    y_train, y_test = y[train_indices], y[test_indices]

    knn = KNN(k=3)
    knn.fit(X_train, y_train)

    predictions = knn.predict(X_test)
    accuracy = np.mean(predictions == y_test)
    print(f"Model Doğruluğu: {accuracy:.2f}")

    return knn


@app.route('/')
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        username = request.form['username']
        password = request.form['password']
        age = int(request.form['age'])
        salary = float(request.form['salary'])

        conn = get_db_connection()
        user = conn.execute('SELECT * FROM users WHERE username = ?', (username,)).fetchone()

        if user:
            print(check_password_hash(user['password'], password))
            print(password, user['password'])
                  
            if (user['password']== password):
                session['username'] = user['username']
                session['score'] = user['score']
                session['category']="Kayıtlı Kullanıcı Kategoriniz: "+user['category']
                conn.close()
                return redirect(url_for('index'))
            else:
                print("ere")
                conn.close()
                return 'Hatalı şifre. Lütfen tekrar deneyin.'
        else:
            knn_model = train_knn_model()
            predicted_category = knn_model.predict([[age, salary]])[0]
            session['category']="Yeni Kayıt K-NN ALGORİTMASI Tahmin edilen kategoriniz: "+ predicted_category

            conn.execute("""
            INSERT INTO users (username, password, age, salary, category, score)
            VALUES (?, ?, ?, ?, ?, ?)
            """, (username, password, age, salary, predicted_category, 0))
            session['username'] = username
            session['score'] = 0
            conn.commit()
            conn.close()

            return redirect(url_for('index'))

    return render_template('login.html')


def detect_head():
    while True:
        ret, frame = camera.read()
        if not ret:
            print("Kamera görüntüsü alınamadı!")
            break

        height, width, _ = frame.shape
        center_x = width // 2


        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)


        faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(50, 50))

        for (x, y, w, h) in faces:

            head_center_x = x + w // 2


            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.circle(frame, (head_center_x, y + h // 2), 5, (0, 0, 255), -1)

            if head_center_x < center_x - 50:
                cv2.putText(frame, "Sola git", (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
            elif head_center_x > center_x + 50:
                cv2.putText(frame, "Saga git", (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
            else:
                cv2.putText(frame, "Ortadasiniz", (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)


        cv2.line(frame, (center_x, 0), (center_x, height), (255, 0, 0), 2)

        _, buffer = cv2.imencode('.jpg', frame)
        frame_bytes = buffer.tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')



@app.route('/index', methods=["GET", "POST"])
def index():
    return render_template('index.html')


@app.route('/video_feed')
def video_feed():
    return Response(detect_head(), mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route('/exam', methods=["GET", "POST"])
def exam():
    if request.method == "POST":
        answers = request.form
        score = 0
        total_questions = len(answers)

        conn = get_db_connection()
        cursor = conn.cursor()

        username = session.get('username')  
        print(username)
        cursor.execute("SELECT score FROM users WHERE username = ?", (username,))

        current_score = cursor.fetchone()
        if current_score:
            print(f"Mevcut puan: {current_score['score']}")
        else:
            print("Kullanıcı bulunamadı.")
        
        for question_id, user_answer in answers.items():
            cursor.execute("SELECT correct_option FROM questions WHERE id = ?", (question_id,))
            result = cursor.fetchone()
            if result and user_answer == result["correct_option"]:
                score += 1
        conn.close()


        if current_score is not None and score > current_score["score"]:
            print("-------------------------------------------")
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("UPDATE users SET score = ? WHERE username = ?", (score, username))
            session['score'] = score
            conn.commit()
            conn.close()

        return redirect(url_for("result", score=score, total_questions=total_questions))

    conn = get_db_connection()

    questions = conn.execute("SELECT * FROM questions ORDER BY RANDOM() LIMIT 5").fetchall()
    conn.close()

    return render_template("exam.html", questions=questions)



@app.route("/result")
def result():
    score = request.args.get("score")
    total_questions = request.args.get("total_questions")
    return render_template("result.html", score=score, total_questions=total_questions)

if __name__ == '__main__':
    app.run(debug=True, threaded=True)
