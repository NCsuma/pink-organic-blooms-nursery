from flask import Flask, render_template,url_for
from FlowerItem import FlowerItem

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/flowers')
def show_flower_images():
    item1 = FlowerItem(1,"Cosmos","images/flower1.jpg")
    item2 = FlowerItem(2,"Gardenblue flower", "images/flower2.jpg")
    item3 = FlowerItem(3,"Red Anemone", "images/flower3.jpg")
    item4 = FlowerItem(4,"Marigold", "images/flower4.jpg")
    item5 = FlowerItem(5,"Sun Flower", "images/flower5.jpg")
    item6 = FlowerItem(6,"Orchid", "images/flower7.jpg")
    flowersgroup1 = [item1,item2,item3]
    flowersgroup2 = [item4,item5,item6]
    return render_template('flowers.html',flowersgroup1 = flowersgroup1 ,flowersgroup2 = flowersgroup2)

@app.route('/contact')
def contact():

    #return "Hello, world!"
    return render_template('contact.html')

if __name__ == "__main__":
    app.run(debug=True)
