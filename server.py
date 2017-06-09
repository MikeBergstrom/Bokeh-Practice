from bokeh.plotting import figure, output_file, show
from bokeh.embed import components
from flask import Flask, render_template, request, redirect, flash

app= Flask(__name__)
app.secret_key="sosecret"


plot = figure()
plot.circle([2,2,5,6,7], [3,4,1,2,3])
script, div = components(plot)
script
print div

@app.route('/')
def index():
    return render_template("index.html", script=script, div=div)
app.run(debug=True)