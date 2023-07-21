from flask import Flask, render_template, request 
from database import db, Sequence

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sequences.db'

db.init_app(app)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        search_term = request.form['search_term']
        sequences = Sequence.query.filter(Sequence.name.like(f'%{search_term}%')).all()
        if not sequences:
            no_match_message = f"No sequences found for '{search_term}'."
            return render_template('index.html', sequences=sequences, no_match_message=no_match_message)

        return render_template('index.html', sequences=sequences)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
