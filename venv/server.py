from flask import Flask, render_template, url_for, request, redirect
from flask_mail import Mail
import csv

app = Flask(__name__)
mail = Mail(app)

if __name__ == "__main__":
    app.run(host='0.0.0.0')

# if __name__ == "__main__":
#     # Only for debugging while developing
#     app.run(host='ericmelchiorhauling.com', debug=True, port=80)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)

def write_to_csv(data):
    with open('database.csv', mode='a', newline="") as database2:
        # date = data['date']
        time = data['time']
        company = data['company']
        payment = data['payment']
        material = data['material']
        yards = data['yards'] + " yards"
        optional = data['optional']
        driver = data['driver']
        driverEmail = data['driver-email']
        sig = data['sig']
        csv_writer = csv.writer(database2, delimiter=',',
                            quotechar='"', quoting=csv.QUOTE_MINIMAL)
        
        csv_writer.writerow([time, company, payment, material, yards, optional, driver, driverEmail, sig])

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            # for csv file
            data = request.form.to_dict()
            write_to_csv(data)
            # for email
            time = request.form.get("time")
            company = request.form.get("company")
            payment = request.form.get("payment")
            material = request.form.get("material")
            yards = request.form.get("yards")
            optional = request.form.get("optional")
            driver = request.form.get("driver")
            driverEmail = request.form.get("driver-email")
            sig = request.form.get("sig")
            # send email
            msg = Message("this is a test", subject="A new ticket from " + company)
            msg.recipients("daniel.melchior@gmail.com")
            msg.add_recipients(driverEmail)
            conn.send(msg)
            return render_template('/email.html', **locals())
        except:
            return "didn't save to database"
    else:   
        return 'Something went wrong. Try again.'