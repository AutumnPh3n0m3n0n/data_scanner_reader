from flask import Flask, render_template, url_for, flash, redirect
from formLogInPage import RegistrationForm, LoginForm
#flash_configuration is referencing from the other file

app = Flask(__name__)
app.config['SECRET_KEY'] = '44aa55bb66cc77dd'

posts = [
    {
        'author': 'Dan Smith',
        'title': 'First Blog Post',
        'content': 'First post content',
        'date_posted': '11 March, 2023'
    },
    {
        'author': 'Jane Doe',
        'title': 'Second Blog Post',
        'content': 'Second post content',
        'date_posted': '11 March, 2023'
    },
    {
        'author': 'John Gray',
        'title': 'Third Blog Post',
        'content': 'Third post content',
        'date_posted': '11 March, 2023'
    },
    {
        'author': 'Michael Lee',
        'title': 'Fourth Blog Post',
        'content': 'Fourth post content',
        'date_posted': '11 March, 2023'
    },
    {
        'author': 'Anna Miller',
        'title': 'Fifth Blog Post',
        'content': 'Fifth post content',
        'date_posted': '11 March, 2023'
    },
    {
        'author': 'Phil Phillips',
        'title': 'Sixth Blog Post',
        'content': 'Sixth post content',
        'date_posted': '11 March, 2023'
    }
]


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title='About')


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template('login.html', title='Login', form=form)


if __name__ == '__main__':
    app.run(debug=True)