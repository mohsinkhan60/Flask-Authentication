from flask import Flask, render_template, session, redirect, url_for


app = Flask(__name__)

@app.route('/')
def home():
    if "username" in session:
        return redirect(url_for('dashboard'))
    return render_template('index.html')

if __name__ == "__main__":
      app.run(debug=True)