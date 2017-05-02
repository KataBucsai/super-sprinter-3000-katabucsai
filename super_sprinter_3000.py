from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    with open("story_list.csv", "r") as file:
        lines = file.readlines()
    table = [element.replace("\n", "").split(";") for element in lines]

    return render_template("list.html", table=table)


@app.route('/story', methods=["GET", "POST"])
def story():
    with open("story_list.csv", "r") as file:
        lines = file.readlines()
    table = [element.replace("\n", "").split(";") for element in lines]
    new_story = []
    render_template("story.html", new_story=new_story)
    table.append(new_story)
    with open("story_list.csv", "w") as file:
        for record in table:
            row = ';'.join(record)
            file.write(row + "\n")
    return render_template("list.html", table=table)

if __name__ == '__main__':
    app.run(debug=True)