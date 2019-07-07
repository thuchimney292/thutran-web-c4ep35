from flask import Flask
app=Flask(__name__)

@app.route('/add/<int:n1>/<int:n2>')
def sum2number(n1,n2):
    _sum =str(n1+n2)
    return _sum

if __name__ == "__main__":
    app.run(debug=True)