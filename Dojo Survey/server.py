from flask import Flask, render_template, session, redirect,request

app = Flask(__name__)

app.secret_key="Something"

@app.route('/')
def mainpag():
    return render_template("index.html")


@app.route('/process',methods=['POST'])
def process():
    session['name'] = request.form['name']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    session['comments'] = request.form['comments']
    return redirect('/success')

@app.route('/success')
def info():
    return render_template('submitted.html')
    
if __name__=="__main__":
    app.run(debug=True)

# http://127.0.0.1:5000/