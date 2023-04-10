from flask import Flask, render_template
from database import engine
from sqlalchemy import text

app = Flask(__name__)

# projects = [{
#   'id': 1,
#   'title': "Калькулятор метрических величин",
#   'desc_text': 'Программа для перевода одной физической феличины в другую',
#   'img_link': 'screen_1.png',
#   'keywords': 'Python, tkinter, customtkinter'
# }, {
#   'id': 2,
#   'title': 'Таймер',
#   'desc_text': 'Обратный отсчет времени',
#   'img_link': 'screen_2.png',
# }, {
#   'id': 3,
#   'title': 'Домашняя библиотека',
#   'desc_text': 'Каталог книг с базой данных',
#   'img_link': 'screen_3.png',
#   'keywords': 'Python, tkinter, customtkinter, sqlite',
# }]


def load_projects_from_bd():
  with engine.connect() as conn:
    result = conn.execute(text("select * from projects"))
  
    result_dicts = []
  
    for row in result.all():
      result_dicts.append(row._mapping)
  
  
    return result_dicts



@app.route("/")
def index():
  # return "<p>Привет, это Flask</p>"
  return render_template('index.html', projects=load_projects_from_bd())


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
