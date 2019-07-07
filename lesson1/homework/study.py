from flask import Flask,render_template,redirect
app=Flask(__name__)

me={
    'Name':'Thư',
    'School':'MTA',
    'Hobby':'Reading book',
    'Animal':'MyTom'
}
@app.route('/about-me')
def about_me():
    return render_template("about_me.html",ME=me)
@app.route('/school')
def school():
    return redirect('http://techkids.vn')
if __name__=="__main__":
    app.run(debug=True)