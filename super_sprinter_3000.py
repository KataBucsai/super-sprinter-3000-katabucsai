from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    with open("story_list.csv", "r") as file:
        lines = file.readlines()
    table = [element.replace("\n", "").split(";") for element in lines]

    return render_template("list.html", table=table)


if __name__ == '__main__':
    app.run(debug=True)