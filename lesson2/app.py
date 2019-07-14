from flask import Flask, render_template,redirect, request, url_for
app = Flask(__name__)
from mongoDB import get_all_food,insert_food,delete_food_by_id, find_food_by_id
# foods =[
#     {'name':'com rang','price':'100'},
#     {'name':'ga','price':'150'}
# ]
@app.route('/',methods=['GET'])
def index():
    return render_template('index.html',data=get_all_food())

@app.route('/delete/<food_id>')
def delete_food(food_id):
    delete_food_by_id(food_id)
    return redirect(url_for('index'))
    
@app.route('/',methods=["POST"])
def post_food():
    food_name=request.form.get('name')
    food_price=request.form.get('price')
    insert_food(food_name,food_price)
    #foods.append({'name':food_name,'price':food_price})
    # return redirect(url_for('index'))
    return render_template('index.html', data = get_all_food())
@app.route('/edit/<food_id>')
def get_edit(food_id):
    food=find_food_by_id(food_id)
    return render_template("edit.html",food=food)

if __name__ == '__main__':
  app.run(host='127.0.0.1', port=8000, debug=True)
 