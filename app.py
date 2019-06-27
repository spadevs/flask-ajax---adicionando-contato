from flask import Flask, render_template, request

app = Flask(__name__)

contacts = []

@app.route('/contato/adicionar', methods=['GET', 'POST'])
def add_contact():
    if request.method == 'POST':
        contact_name = request.form['contact_name']

        contacts.append(contact_name)
        return contact_name

    return render_template('contato.html', contacts=contacts)


app.run(debug=True)