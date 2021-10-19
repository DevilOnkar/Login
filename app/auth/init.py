from flask import Flask, request, render_template, redirect, url_for
from Model import model
from form import LoginForm
app=Flask(__name__, template_folder='../template',static_folder='../Static')


@app.route('/register1')
def register1():
    return render_template('register1.html')

@app.route('/login1')
def login1():
    return render_template('login1.html')

@app.route('/forget1')
def forget1():
    return render_template('forget1.html')
 
@app.route('/login', methods=['GET', 'POST'])
def login():
    result=request.form
    username=result['username']
    password=result['password']
    lf=LoginForm(username,password)
    result=model.loginCheck(lf.user,lf.passw)
    if result == 'success':
        return render_template('profile1.html')
    elif result == 'fail':
        return render_template('forget1.html')
    
if __name__ == '__main__':
    app.run(debug=True)
