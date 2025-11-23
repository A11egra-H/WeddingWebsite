from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html', page_title='Home')

@app.route('/schedule')
def schedule():
    return render_template('schedule.html', page_title='Schedule')

@app.route('/faqs')
def faqs():
    return render_template('faqs.html', page_title='FAQs')

@app.route('/story')
def story():
    return render_template('story.html', page_title='Story')

@app.route('/rsvp')
def rsvp():
    return render_template('rsvp.html', page_title='RSVP')

if __name__ == '__main__':
    app.run(debug=True)
