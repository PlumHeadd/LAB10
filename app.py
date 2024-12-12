from flask import Flask, request, render_template

app = Flask(__name__)


tasks = []


def add_task(task):
    if task not in tasks:  
        tasks.append(task)


def get_tasks():
    return tasks

@app.route("/", methods=["GET"])
def index():
    return render_template("index2.html", tasks=get_tasks())

@app.route("/add-task", methods=["POST"])
def add_task_route():
    task = request.form.get("task")
    if task:  
        add_task(task)
    return render_template("index2.html", tasks=get_tasks())

if __name__ == "__main__":
    app.run(debug=True)
