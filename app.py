from flask import Flask, render_template

app = Flask(__name__)

schemes = [
    {
        "name": "PM Kisan Yojana",
        "eligibility": "Small and marginal farmers",
        "deadline": "31 December 2026",
        "documents": "Aadhaar, Bank Passbook, Land Records"
    },
    {
        "name": "Ayushman Bharat",
        "eligibility": "Low income families",
        "deadline": "Open Throughout Year",
        "documents": "Aadhaar Card, Ration Card"
    },
    {
        "name": "PM Awas Yojana",
        "eligibility": "Economically weaker sections",
        "deadline": "15 March 2026",
        "documents": "Income Certificate, Aadhaar, Bank Details"
    }
]

@app.route('/')
def home():
    return render_template('index.html', schemes=schemes)

if __name__ == '__main__':
    app.run(debug=True)