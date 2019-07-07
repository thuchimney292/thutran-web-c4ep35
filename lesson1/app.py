# flask, django, pyramid (o ung dung cho lam)

from flask import Flask
app =Flask(__name__)
#function binding
@app.route('/')
def home(): 
    return "Home page"

@app.route('/hello')
def hello():
    return "Hello Everyone"

@app.route('/hello/<name>')
def hello_(name):
    age = 19
    return "Hello {0}, he is {1} years old!".format(name,age)

@app.route('/hello/<name>/<age>')
def hello_name_age(name,age):
    return "Hello {0}, he is {1} years old!".format(name,age)
if __name__ == "__main__": # có tác dụng khi triển khai đường link thật
    app.run(debug=True)
