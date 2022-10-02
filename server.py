from flask import Flask, render_template, request, redirect
import csv


app = Flask(__name__)
print(__name__)

# decorator
# @app.route("/index.html")
# def my_home():
#     return render_template('./index.html')
#
# @app.route("/works.html")
# def works():
#     return render_template('./works.html')
#
# @app.route("/about.html")
# def about():
#     return render_template('./about.html')
#
# @app.route("/contact.html")
# def contact():
#     return render_template('./contact.html')
#
# @app.route("/components.html")
# def components():
#     return render_template('./components.html')
#
#
# @app.route('/submit_form', methods=['GET', 'POST'])
# def submit_form():
#     return 'form submitted hoorayy'


# Everything after page /home{wil be displayed}
# @app.route("/<username>/<int:post_id>")
# def users(username=None, post_id=None):
#     return render_template('./index.html', name=username, posts=post_id)

# Home Page
@app.route("/")
def my_home():
    return render_template('index.html')

# Changing Routes Dinamically!!
@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template(page_name)



def write_to_file(data):
    # write in database mode=a = append
    with open('database.txt', mode='a') as database:
        email = data['email']
        subject = data['subject']
        message = data['message']
        file = database.write(f'😎\nEmail: {email}\nSubject: {subject}\nMessage: {message}')
        database.write(f'😎\nEmail: {email}\nSubject: {subject}\nMessage: {message}')


def write_to_csv(data):
    # write in database mode=a = append
    with open('database.csv', newline='', mode='a', encoding='utf-8') as database2:
        email = data['email']
        subject = data['subject']
        message = data['message']
        # where do we want write
        # delimiter ...ect.. option how to write the in the file
        csv_writer = csv.writer(database2, delimiter=",", quotechar='|', quoting=csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    if request.method == 'POST':
        try:
            data = request.form.to_dict()
            write_to_file(data)
            # write_to_csv(data)
            return redirect('./thankYou.html')
        except:
            return 'did not save to database'
    else:
        return 'something went wrong. Try again!'