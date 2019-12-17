from flask import Flask, redirect, request, url_for, render_template
from  fuzzy_brightness import main

app = Flask(__name__)

@app.route("/",methods=['POST','GET'])
@app.route("/home",methods=['POST','GET'])
def home():
    # Return to the same page but with different brightness and electricity usage from html input
    if request.method == 'POST':
        # Perform the whole fuzzy process 
        brightness = main(request.form['KWHValue'])
        return render_template('lamp.html',
        brightness_value =  '%.2f' % brightness,
        KWHValue = request.form['KWHValue'])
    # Default configuration
    return render_template('lamp.html',
    brightness_value =  55.00,
    KWHValue = 500)
        

if __name__ == "__main__":
    app.run()
