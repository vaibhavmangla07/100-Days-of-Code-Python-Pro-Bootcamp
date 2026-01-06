from flask import Flask, render_template, redirect, url_for
from flask_bootstrap import Bootstrap5
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired, URL
import csv
import os

# -------------------- APP SETUP --------------------

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap5(app)

# -------------------- FILE PATH FIX (IMPORTANT) --------------------

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
CSV_FILE_PATH = os.path.join(BASE_DIR, "cafe-data.csv")

# -------------------- FORM --------------------

class CafeForm(FlaskForm):
    cafe = StringField('Cafe name', validators=[DataRequired()])
    location = StringField(
        "Cafe Location on Google Maps (URL)",
        validators=[DataRequired(), URL()]
    )
    open = StringField("Opening Time e.g. 8AM", validators=[DataRequired()])
    close = StringField("Closing Time e.g. 5:30PM", validators=[DataRequired()])
    coffee_rating = SelectField(
        "Coffee Rating",
        choices=["☕️", "☕☕", "☕☕☕", "☕☕☕☕", "☕☕☕☕☕"],
        validators=[DataRequired()]
    )
    wifi_rating = SelectField(
        "Wifi Strength Rating",
        choices=["✘", "💪", "💪💪", "💪💪💪", "💪💪💪💪", "💪💪💪💪💪"],
        validators=[DataRequired()]
    )
    power_rating = SelectField(
        "Power Socket Availability",
        choices=["✘", "🔌", "🔌🔌", "🔌🔌🔌", "🔌🔌🔌🔌", "🔌🔌🔌🔌🔌"],
        validators=[DataRequired()]
    )
    submit = SubmitField('Submit')

# -------------------- ROUTES --------------------

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/add", methods=["GET", "POST"])
def add_cafe():
    form = CafeForm()
    if form.validate_on_submit():
        with open(CSV_FILE_PATH, mode="a", newline="", encoding="utf-8") as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow([
                form.cafe.data,
                form.location.data,
                form.open.data,
                form.close.data,
                form.coffee_rating.data,
                form.wifi_rating.data,
                form.power_rating.data
            ])
        return redirect(url_for("cafes"))

    return render_template("add.html", form=form)


@app.route("/cafes")
def cafes():
    with open(CSV_FILE_PATH, newline="", encoding="utf-8") as csv_file:
        csv_data = csv.reader(csv_file)
        list_of_rows = list(csv_data)

    return render_template("cafes.html", cafes=list_of_rows)

# -------------------- RUN --------------------

if __name__ == "__main__":
    app.run(debug=True, port=5002)
