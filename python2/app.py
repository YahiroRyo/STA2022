from flask import Flask, render_template,request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/sample1')
def sample1_index():
    return render_template('sample1_index.html')

@app.route('/sample1/result', methods=['POST'])
def sample1_reuslt():
    number = int(request.form['number'])
    message = '偶数です' if number % 2 == 0 else '奇数です'
    return render_template('sample1_result.html', message = message)

@app.route('/sample2')
def sample2_index():
    return render_template('sample2_index.html')

@app.route('/sample2/result', methods=['POST'])
def sample2_reuslt():
    number = int(request.form['number'])
    message = '素数ではありません' if number == 1 or True in [number % i == 0 for i in range(2, number)] else '素数です'
    return render_template('sample2_result.html', message = message)
