from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')

def index():
    return render_template('whats_name.html')


@app.route('/process', methods=['POST'])
def create_user():
    
   print request.form['name']

#    return render_template('success.html')
   # redirects back to the '/' route
   return redirect('/')

app.run(debug=True)
