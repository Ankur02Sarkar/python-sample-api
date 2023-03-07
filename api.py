from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def echo():
    param = request.args.get('text')
    print(param)
    return f"Echo: {param}"

if __name__ == '__main__':
    app.run()
