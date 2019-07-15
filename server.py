from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route("/")
def index():

    return render_template("index.html")
@app.route('/result', methods=['POST'])
def create_user():
    print("Got Post Info")
    print(f"{request.form}")
    name_from_form = request.form['name']
    comment_from_form = request.form['comment']
    location_from_form = request.form['location']
    language_from_form = request.form['language']
    return render_template("info.html", name_on_template=name_from_form, comment_on_template=comment_from_form,location_on_template =location_from_form,language_on_template = language_from_form  )
app.run(debug=True)