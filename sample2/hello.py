from flask import Flask, render_template,request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', message="名前を入力してください。")

@app.route('/result', methods=["GET"])
def result_get():
    # GET送信の処理
    field = request.args.get("field","")
    return render_template('result.html', message = "名前は{}です。".format(field))

@app.route('/result', methods=["POST"])
def result_post():
    # POST送信の処理
    field = request.form["field"]
    return render_template('result.html', message = "My name is {}.".format(field))

if __name__ == '__main__':
    app.run()