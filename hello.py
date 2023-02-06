from flask import Flask, escape, request

app = Flask(__name__)

@app.route("/")
def hello() -> str:
    name = request.args.get("name")
    style_name = f'<p style="color:red; text-align:center">{name}</p>!'
    return f'Hello, {escape(style_name)}'

if __name__ == '__main__':
    app.run(debug=True)
