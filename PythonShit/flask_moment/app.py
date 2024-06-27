from flask import Flask, render_template, jsonify
import numpy as np

app = Flask(__name__)
x = np.arange(0, 10, 0.1)
a = 1

@app.route('/')
def index():
    return render_template('index.html')


# Генерация новых данных (10 точек) и преобразование в Python-friendly формат
@app.route('/update', methods=['GET'])
def update_data():
    global x, a
    y = np.sin(x + a)
    a += 0.1

    # Преобразование чисел в формат Python-friendly для сериализации в JSON
    data = {'x': x.tolist(), 'y': y.tolist()}
    return jsonify(data)


if __name__ == '__main__':
    app.run(debug=True)