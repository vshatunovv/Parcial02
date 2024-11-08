from flask import Flask, render_template
import math

app = Flask(__name__)

@app.route('/<int:num>')
def factorial(num):
    try:
        result = math.factorial(num)
        return render_template('factorial.html', number=num, result=result)
    except ValueError:
        return "Error de valor"

if __name__ == '__main__':
    app.run(debug=True)
