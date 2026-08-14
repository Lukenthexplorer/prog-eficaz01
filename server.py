from flask import Flask, render_template, request, redirect
from utils import load_data, create_data

app = Flask(__name__)
app.static_folder = 'static'

@app.route('/')
def home():
  info = load_data()
  return render_template('index.html', info=info)

@app.route('/submit', methods=["GET", "POST"])
def submit_note():
  title = request.form.get("title")
  details = request.form.get("details")

  create_data(title, details)
  return redirect("/")

if __name__ == "__main__":
  app.run(debug=True)