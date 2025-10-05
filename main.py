from flask import Flask, render_template,request, redirect



app = Flask(__name__)

#Halaman Konten Berjalan
@app.route('/')
def index():
    return render_template('index.html')


#Keterampilan Dinamis
@app.route('/', methods=['POST'])
def process_form():
    button_python = request.form.get('button_python')
    button_db = request.form.get('button_db')
    button_html = request.form.get('button_html')
    button_discord = request.form.get('button_discord')
    email = request.form.get('email')
    text = request.form.get('text')
    
    if email and text:
        with open('messages.txt', 'a') as f:
                  f.write("Email:" + email + "/n")
                  f.write("Message:" + text + "/n")

    return render_template('index.html', button_python=button_python, button_db=button_db, button_html=button_html, button_discord=button_discord)


if __name__ == "__main__":
    app.run(debug=True)
