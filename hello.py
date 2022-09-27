from flask import Flask, escape, request

app = Flask(__name__)


@app.route('/')
def hello():
    # http://127.0.0.1:5000/?name=Tom
    name = request.args.get("name")
    style_name = '<p style="color:red; text-align:center";>{}</p>!'.format(name)
    return 'Hello, ' + escape(style_name)


if __name__ == '__main__':
    app.run(debug=True)
