from flask import Flask, render_template

app = Flask(__name__)

projects = [{
  'id': 1,
  'title': "Калькулятор метрических величин",
  'description': 'Программа для перевода одной физической феличины в другую',
  'image': 'screen_1.png',
  'techs': 'Python, tkinter, customtkinter'
}, {
  'id': 2,
  'title': 'Таймер',
  'description': 'Обратный отсчет времени',
  'image': 'screen_2.png',
}, {
  'id': 3,
  'title': 'Домашняя библиотека',
  'description': 'Каталог книг с базой данных',
  'image': 'screen_3.png',
  'techs': 'Python, tkinter, customtkinter, sqlite',
}]


@app.route("/")
def index():
  # return "<p>Привет, это Flask</p>"
  return render_template('index.html', projects=projects)


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
