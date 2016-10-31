# imports
from flask import Flask, request, jsonify

# create app
app = Flask(__name__)
app.config.from_object(__name__)

prs = [
    {'code': 'A','price1': 30.5, 'price2': 90.0, 'price2cnt': 3},
    {'code': 'B','price1': 101.3,'price2': 101.3,'price2cnt': 1},
    {'code': 'C','price1': 1.0,  'price2': 5.0,  'price2cnt': 6},
    {'code': 'D','price1': 500.0,'price2': 500.0,'price2cnt': 1},
    {'code': 'F','price1': 17.0, 'price2': 135.0,'price2cnt': 9}
]

#curl -H "Content-Type: application/json" -X POST -d "{"""r""":"""ACB"""}" http://localhost:5000
#or
#curl http://localhost:5000/api?q=ABCD
   
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return jsonify({'products': prs})
    elif request.method == 'POST':
        sum = 0
        for p in prs:
            sum+= int(request.json.get('r').count(p.get('code'))/p.get('price2cnt')) * p.get('price2') + request.json.get('r').count(p.get('code'))%p.get('price2cnt') * p.get('price1')            
        return jsonify(sum)
    
@app.route('/api', methods=['GET'])
def api():
    q = request.args.get('q')
    sum = 0
    for p in prs:
        sum+= int(request.args.get('q').count(p.get('code'))/p.get('price2cnt')) * p.get('price2') + request.args.get('q').count(p.get('code'))%p.get('price2cnt') * p.get('price1')            
    return jsonify(sum)
    
if __name__ == '__main__':
    app.run()