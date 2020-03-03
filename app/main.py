from flask import Flask, render_template, url_for, request, redirect
from flask_mail import Mail, Message
import csv
from binascii import a2b_base64
app = Flask(__name__)

mail_settings ={
    "MAIL_SERVER":'smtp.gmail.com',
    "MAIL_PORT":465,
    "MAIL_USE_TLS":False,
    "MAIL_USE_SSL":True,
    "MAIL_USERNAME":'ericmelchiorhauling@gmail.com',
    "MAIL_PASSWORD": 'Thisism@1l'
}

app.config.update(mail_settings)
mail = Mail(app)

if __name__ == "__main__":
    app.run(host='ericmelchiorhauling.com',debug=True, port=80)

# if __name__ == "__main__":
#     # Only for debugging while developing
#     app.run(host='ericmelchiorhauling.com', debug=True, port=80)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/spreadsheet')
def spreadsheet():
    return render_template('spreadsheet.html')

@app.route('/ticket')
def ticket():
    return render_template('ticket.html')

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
            ##time = request.form.get("time")
            ##company = request.form.get("company")
            ##payment = request.form.get("payment")
            ##material = request.form.get("material")
            ##yards = request.form.get("yards")
            ##optional = request.form.get("optional")
            ##driver = request.form.get("driver")
            ##driverEmail = request.form.get("driver-email")
            ##sig = request.form.get("sig")

            # convert signature from base64 data-url to an image
            ##data = sig[22:]
            ##binary_data = a2b_base64(data)
            ##fd = open('signature.png', 'wb')
            ##fd.write(binary_data)
            ##fd.close()

            ##msg = Message("A new ticket has been created!", sender=("Eric Melchior Hauling Company", "ericmelchiorhauling@gmail.com"), recipients=["daniel.melchior@gmail.com"])
            
            ##msg.html=render_template('/email.html', **locals())
            # uncomment if you want to send signature as attachment
            # with app.open_resource("signature.png") as fp:
            #     msg.attach("signature.png", "image/png", fp.read())

            # attach signature embedded in email
            with app.open_resource("signature.png") as fp:
                msg.attach("signature.png", "image/png", fp.read(), "inline", headers=[['Content-ID','<signature>'],])
            
            mail.send(msg)
         
            return render_template('/thankyou.html', **locals())
        except:
            return "didn't save to database"
    else:   
        return 'Something went wrong. Try again.'
