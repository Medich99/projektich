from flask import Flask, render_template, request 
from database import db, Sequence, count_sequence_characters

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

def calculate_percentage_similarity(seq1, seq2):
    len_seq1 = len(seq1)
    len_seq2 = len(seq2)

    if len_seq1 == 0 or len_seq2 == 0:
        return 0.0

    num_common = sum(c1 == c2 for c1, c2 in zip(seq1, seq2))
    similarity_percentage = (num_common / max(len_seq1, len_seq2)) * 100

    return similarity_percentage

def calculate_similarity(seq1, seq2):

    return calculate_percentage_similarity(seq1, seq2)

@app.route('/analyze', methods=['GET', 'POST'])
def analyze_sequences():
    if request.method == 'POST':
        # To get the sequences entered by the user in the form
        sequence1 = request.form['sequence1']
        sequence2 = request.form['sequence2']

        # This is done to perform sequence analysis and calculate similarity percentage
        similarity_percentage = calculate_percentage_similarity(sequence1, sequence2)

        # These lines count characters in both sequences
        sequence1_character_counts = count_sequence_characters(sequence1)
        sequence2_character_counts = count_sequence_characters(sequence2)

        # Render the results template with the calculated similarity and character counts
        return render_template('results.html', sequence1=sequence1, sequence2=sequence2, similarity_percentage=similarity_percentage, sequence1_character_counts=sequence1_character_counts, sequence2_character_counts=sequence2_character_counts)

    # Render the analysis page if it's a GET request
    return render_template('analysis.html')

if __name__ == '__main__':
    app.run(debug=True)
