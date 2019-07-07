from flask import Flask, render_template
app = Flask(__name__)

@app.route('/bmi/<int:weight>/<int:height>')
def BMI(weight, height):
    bmi = weight / (height/100)**2
    return render_template('bmi.html',BMI=bmi)

if __name__ == "__main__":
    app.run(debug=True)