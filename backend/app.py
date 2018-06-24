from flask import Flask
app = Flask(__name__)

@app.route("/")
def main():
    return "Welcome!"

@app.route("/coucou")
def couocu():
    return([i for i in range(120)])

if __name__ == '__main__':
    app.run()