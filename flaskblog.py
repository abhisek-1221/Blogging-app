from flask import Flask, render_template, url_for,flash,redirect
from forms import RegistrationForm, LoginForm
app = Flask(__name__)

app.config['SECRET_KEY'] = 'a81038b1383be9a25dd8b9dbc888cc8c'

posts = [
    {
        'author': 'Abhisek Sahoo',
        'title': 'Blog Plost 1',
        'content': 'Hyperparameter tuning',
        'date_posted': 'April 29,2023'
    },
    {
        'author': 'Vaansh',
        'title': 'Blog Plost 2',
        'content': 'Intro to Cloud',
        'date_posted': 'May 14,2023'
    }
]
@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)

@app.route("/about")
def about():
    return render_template('about.html', title='About')

@app.route("/register", methods=['GET','POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

@app.route("/login")
def login():
    form = LoginForm()
    return render_template('login.html', title='Login', form=form)

if __name__ == '__main__':
    app.run(debug=True,host='127.0.0.1', port=5001)