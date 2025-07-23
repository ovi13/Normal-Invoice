from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/invoice', methods=['POST'])
def invoice():
    customer = request.form['customer']
    item = request.form['item']
    price = float(request.form['price'])
    quantity = int(request.form['quantity'])
    total = price * quantity
    return render_template('invoice.html', customer=customer, item=item, price=price, quantity=quantity, total=total)

if __name__ == '__main__':
    app.run(debug=True, port=5001)

