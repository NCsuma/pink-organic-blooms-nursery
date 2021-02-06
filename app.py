from flask import Flask, render_template,url_for

app = Flask(__name__,static_folder='abc')

@app.route('/')
def index():
    messages = ["Hi,welcome","you have a price","your updates are"]
    #return "Hello, world!"
    return render_template('index.html',messages = messages)

@app.route('/contact')
def contact():

    #return "Hello, world!"
    return render_template('contact.html')

if __name__ == "__main__":
    app.run(debug=True)
