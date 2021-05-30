
from flask import Flask, render_template

app=Flask(__name__)
# home page
@app.route("/")
def home():
        return render_template("index.html")

# home page

@app.route('/contact',methods = ['POST', 'GET'])
def login():
   if request.method == 'POST':
      user = request.form['nm']
      return redirect(url_for('success'))
   else:
      user = request.args.get('nm')
      return redirect(url_for('success'))

if __name__=="__main__":
	app.run()