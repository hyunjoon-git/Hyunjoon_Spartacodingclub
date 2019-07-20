from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

orders = []
order_no = 1

@app.route('/')
def home():
    return 'This is Home!'


@app.route('/mypage')
def mypage():
    return render_template('index.html')

@app.route('/post', methods=['POST'])
def post():
    global orders
    global order_no
    name_receive = request.form['name_give']
    volume_receive = request.form['volume_give']
    address_receive = request.form['address_give']
    phonenumber_receive = request.form['phonenumber_give']

    order = {'name': name_receive, 'volume': volume_receive, 'address': address_receive, 'phone': phonenumber_receive, 'no' : order_no}

    order_no = order_no + 1

    orders.append(order)

    return jsonify({'result': 'success'})

@app.route('/post', methods=['GET'])
def view():
    return jsonify({'result': 'success', 'orders': orders})

@app.route('/delete', methods=['post'])
def delete():
   global orders
   no_receive = request.form['no_give']

   for order in orders:
       if str(order['no']) == no_receive:
           orders.remove(order)
           return jsonify({'result':'success'})

if __name__ == '__main__':
    app.run('127.0.0.1', port=5000, debug=True)