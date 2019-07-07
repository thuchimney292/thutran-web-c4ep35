from flask import Flask, render_template,redirect
app= Flask(__name__)
all_foods=[
        {
        'title' : "Bánh xèo",
        'des':'Good',
        'link':"https://thucthan.com/media/2018/06/banh-xeo/banh-xeo.jpg",
        '_type':"food"
        },
        {
        'title' : "Gà",
        'des':'Good',
        'link':"http://alohaa.vn/img_data/images/hap-dan-voi-mon-ga-ran-nhieu-vi-tai-aloha/hap-dan-voi-mon-ga-ran-nhieu-vi-tai-aloha-001.JPG",
        '_type':"food"
        },
        {
        'title' : "Thịt kho tàu",
        'des':'Good',
        'link':"https://thucthan.com/media/thit-kho-tau/thit-kho-tau.jpg",
        '_type':"food"
        },
        {
        'title' : "Coca",
        'des':'Good',
        'link':"https://www.hangngoainhap.com.vn/images/201712/goods_img/2061_P_1514107213177.jpg",
        '_type':"drink"
        }
]
@app.route('/foods')
def all_food():
    return render_template("all_foods.html",FOOD=all_foods)
@app.route('/foods/detail/<int:index>')
@app.route("/foods/delete/<int:index>")
def delete_food(index):
    del all_foods[index]
    return redirect('/foods')
def food_detail(index):
    food=all_foods[index]
    return render_template("Food_detail.html", FOOD_DETAIL=food) #str(all_foods[index])

if __name__ =="__main__":
    app.run(debug=True)