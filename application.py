from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def index_page():
    """Show an index page."""

    return "<html><body>This is the homepage.</body></html>"

    # Alternately, we could make this a Jinja template in `templates/`
    # and return that result of rendering this, like:
    #
    # return render_template("index.html")


@app.route("/application-form")
def app_form():
    """Show the application for a job."""

    return render_template("application-form.html")


@app.route("/application", methods=["POST"])
def get_app_info():
    first_name = request.form.get("firstname")
    last_name = request.form.get("lastname")
    salary = request.form.get("salary")
    job = request.form.get("job")

    return "Thank you {} {}, for applying for the position of {} with a minimum salary of {}".format(first_name, last_name, job, salary)

if __name__ == "__main__":
    app.run(debug=True)
