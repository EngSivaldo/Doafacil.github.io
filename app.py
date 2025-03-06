from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# Lista para armazenar as doações
doacoes = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/fazerDoacao', methods=['GET', 'POST'])
def fazer_doacao():
    if request.method == 'POST':
        donation_type = request.form['donation-type']
        donation_amount = request.form['donation-amount']
        payment_method = request.form['payment-method']
        donor_name = request.form['donor-name']

        # Adiciona a doação à lista
        doacoes.append({
            'donor_name': donor_name,
            'donation_type': donation_type,
            'donation_amount': donation_amount,
            'payment_method': payment_method
        })

        return redirect('/historicoDoacoes')
    return render_template('fazerDoacao.html')

@app.route('/historicoDoacoes')
def historico_doacoes():
    return render_template('historicoDoacoes.html', doacoes=doacoes)

if __name__ == '__main__':
    app.run(debug=True)