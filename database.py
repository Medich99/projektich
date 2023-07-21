from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Sequence(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=True, nullable=False)
    sequence = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f"<Sequence {self.name}>"

def add_example_sequences():
    example_sequences = [
        {"name": "proba", "sequence": "ATAGGCTTCG"},
        {"name": "dysferlin", "sequence": "GTCCAAGAGCGAGATCTGGGCTACGCCGGGCGCCCGGAGCCCTAGTCCAGCCCCCGGCCATCGCGGCCGCCGCCCAGCCAGGTGCAAAATGCCGTGTCATTGGGAGACTCCGCAGCCGGAGCATTAGATTACAGCTCGACGGAGCTCGGGAAGGGCGGCGGGGGTGGAAGATGAGCAGAAGCCCCTGTTCTCGGAACGCCGGCTGACAAG"},
        {"name": "sekvenca 3", "sequence": "TATATATA"},
        {"name": "retarded penis [Homo sapiens(human)]", "sequence": "GTAGTATATATAAAAATAACAGTCGGGCGGGGAGCTCGGCGGCGGC"},
        {"name": "major histocompatibility complex, class I, B", "sequence": "AGAGTCTCCTCAGACGCCGAGATGCTGGTCATGGCGCCCCGAACCGTCCTCCTGCTGCTCTCGGCGGCCCTGGCCCTGACCGAGACCTGGGCCGGTGAGTGCGGGTCGGGAGGGAAATGGCCTCTGCCGGGAGGAGCGAGGGGACCGCAGGCGGGGGCGCAGGACCTGAGGAGCCGCGCCGGGAGGAGGGTCGGGCGGGTCTCAGCCCCTCCTCACCCCCAGGCTCCCACTCCATGAGGTATTTCTACACCTCCGTGTCCCGGCCCGGCCGCGGGGAGCCCCGCTTCATCTCAGTGGGCTACGTGGACGACACCCAGTTCGTGAGGTTCGACAGCGACGCCGCGAGTCCGAGAGAGGAGCCGCGGGCGCCGTGGATAGAGCAGGAGGGGCCGGAGTATTGGGACCGGAACACACAGATCTACAAGGCCCAGGCACAGACTGACCGAGAGAGCCTGCGGAACCTGCGCGGCTACTACAACCAGAGCGAGGCCGGTGAGTGACCCCGGCCCGGGGCGCAGGTCACGACTCCCCATCCCCCACGTACGGCCCGGGTCGCCCCG"},


        # Add more example sequences as needed
    ]

    for seq_data in example_sequences:
        sequence = Sequence(name=seq_data["name"], sequence=seq_data["sequence"])
        db.session.add(sequence)

    db.session.commit()

def create_app():
    # Initialize the Flask application
    app = Flask(__name__)

    # Set the SQLAlchemy database URI (replace 'sqlite:///sequences.db' with your desired database URI)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///sequences.db'

    # Initialize the database with the app
    db.init_app(app)

    # Return the initialized app
    return app

if __name__ == '__main__':
    # Create the Flask app within the application context
    app = create_app()
    with app.app_context():
        # Create all the database tables
        db.create_all()

        # Add example sequences to the database
        add_example_sequences()
