from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    txt = "Hello World!"
    return render_template('hello.html', text=txt)

if __name__ == '__main__':
    app.run(debug=True)