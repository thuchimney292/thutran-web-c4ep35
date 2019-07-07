from flask import Flask
app = Flask(__name__)

@app.route('/bmi/<int:weight>/<int:height>')
def BMI(weight,height):
    bmi=weight/(height/100)**2
    if bmi<16:
        return(str(bmi)+' Severly underweight')
    if 16<=bmi<18.5:
        return(str(bmi)+' Underweight')
    if 18.5<= bmi <25:
        return(str(bmi)+' Normal')
    if 25<= bmi <30:
        return(str(bmi)+" Overweight")
    if bmi>=30:
        return(str(bmi)+' Obese')
if __name__=='__main__':
    app.run(debug=True)