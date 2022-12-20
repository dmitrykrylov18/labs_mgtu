from flask import Flask
import main

app = Flask('fibonacci')


@app.route('/')
def start():
    return "use /n where n - int"

@app.route('/<int:n>')
def fib(n):
    return str(list(main.fibonacci(n)))

@app.errorhandler(404)
def page_not_found(e):
    return "use /n where n - int"

if __name__=="__main__":
    app.run(debug=True)