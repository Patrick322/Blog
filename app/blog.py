from flask import flask, render_template
app = Flask(__name__)

posts = [
    {
        'author': 'jemmy',
        'title': 'Blog ppost 1'
        'content': 'First post content',
        'date_posted': 'May 1,2020'
    },
    {
        'author': 'Steph'
        'title': 'Blog post 2'
        'content': 'Second post',
        'date_posted': 'April 20,2019'
    }
]
@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html',posts=posts)


@app.route("/about")
def about():
    return render_template('_about.html_')
     
   
if __name__ == '__main__': 
    app.run(debug=True)