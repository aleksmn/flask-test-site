from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
  # return "<p>Привет, это Flask</p>"
  return render_template('index.html')
  


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
  