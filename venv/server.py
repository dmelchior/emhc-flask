from flask import Flask, render_template, url_for, request, redirect
import csv

app = Flask(__name__)

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
        company = data['company']
        payment = data['payment']
        materials = data['materials']
        yards = data['yards']
        optional = data['optional']
        driver = data['driver']
        csv_writer = csv.writer(database2, delimiter=',',
                            quotechar='"', quoting=csv.QUOTE_MINIMAL)
        
        csv_writer.writerow([company,payment,materials,yards,optional,driver])

@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect('/thankyou.html')
        except:
            return "didn't save to database"
    else:   
        return 'Something went wrong. Try again.'