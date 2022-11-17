from flask import Flask, request, render_template

app = Flask(__name__)
app.config.from_pyfile("config.py")
# app.config.from_object(Config)

@app.route('/')
def page_index():
    title = app.config.get("PROJECT_NAME")
    description = app.config.get("PROJECT_DESCRIPTION")
    return f"<h1>{ title }</h1><p>{ description }</p>"

@app.route('/path')
def page_index():
    path = app.config.get("PATH")
    print(path)

app.run()