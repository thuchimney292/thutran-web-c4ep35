from flask import Flask,render_template
app=Flask(__name__)
users = {
    'huy': {
			'name' : 'Nguyen Quang Huy',
			'age': 29
       },
    'tuananh' : {
			'name' : 'Huynh Tuan Anh',
			'age' : 22
       }
}
@app.route('/user/<username>')
def check_user(username):
    if username in users:
        user = users[username]
        return render_template('user.html', USER = user)
    else:
        return 'User not found'
if __name__ == '__main__':
    app.run(debug=True)