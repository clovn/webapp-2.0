from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/submit_form', methods=['POST'])
def submit_form():
    num = request.form.get('num')
    date = request.form.get('date')
    reason = request.form.get('reason')

    # здесь можно добавить код для сохранения данных в базу данных или отправки их на email
    # ...

    return render_template('submit.html', num=num, date=date, reason=reason)

if __name__ == '__main__':
    app.run(debug=True)
