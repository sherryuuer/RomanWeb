from flask import Flask, render_template, request, redirect
import csv


app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/<string:page_name>")
def pages(page_name):
    return render_template(page_name)


def write_data_to_txt(data):
    with open('database.txt', mode='a') as database:
        email = data['email']
        subject = data['subject']
        message = data['message']
        database.write(f'{email},{subject},{message}')


def write_data_to_csv(data):
    with open('database.csv', mode='a', newline='') as database:
        email = data['email']
        subject = data['subject']
        message = data['message']
        csv_writer = csv.writer(database, delimiter=',',
                                quotechar='"', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_data_to_csv(data)
            # Got the data!
            return redirect('thankyou.html')
        except Exception:
            return 'Saving data failed'
    else:
        return 'Something goes wrong'


if __name__ == "__main__":
    app.run(debug=True)
