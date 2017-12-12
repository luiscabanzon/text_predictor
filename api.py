import json
import io

'''
path = ''
with io.open(path +'1_1_predictor.json', 'r', encoding='utf-8') as f:
    _1_1 = json.load(f)
with io.open(path +'1_2_predictor.json', 'r', encoding='utf-8') as f:
    _1_2 = json.load(f)
with io.open(path + '2_2_predictor.json', 'r', encoding='utf-8') as f:
    _2_2 = json.load(f)
with io.open(path + '2_1_predictor.json', 'r', encoding='utf-8') as f:
    _2_1 = json.load(f)
with io.open(path + '3_1_predictor.json', 'r', encoding='utf-8') as f:
    _3_1 = json.load(f)
with io.open(path + '3_2_predictor.json', 'r', encoding='utf-8') as f:
    _3_2 = json.load(f)
'''

import zlib
# with open('3_2_predictor.cjson', 'rb') as f:
#     _3_2 = json.loads(zlib.decompress(f.read()).decode('utf-8'))
with open('2_2_predictor.cjson', 'rb') as f:
    _2_2 = json.loads(zlib.decompress(f.read()).decode('utf-8'))
with open('1_2_predictor.cjson', 'rb') as f:
    _1_2 = json.loads(zlib.decompress(f.read()).decode('utf-8'))
# with open('3_1_predictor.cjson', 'rb') as f:
#     _3_1 = json.loads(zlib.decompress(f.read()).decode('utf-8'))
with open('2_1_predictor.cjson', 'rb') as f:
    _2_1 = json.loads(zlib.decompress(f.read()).decode('utf-8'))
with open('1_1_predictor.cjson', 'rb') as f:
    _1_1 = json.loads(zlib.decompress(f.read()).decode('utf-8'))
_3_2 = _3_1 = {}

def predict(key):
    key_1 = key_2 = key_3 = None
    keys = key.split('-')
    key_1 = keys[-1]
    next_1 = []
    if len(keys) > 1:
        key_2 = '-'.join(keys[-2:])
    if len(keys) > 2:
        key_3 = '-'.join(keys[-3:])
    
    if key_3 in _3_1:
        next_1 += [x[0] for x in _3_1[key_3]]
    if len(next_1) < 5:
        if key_2 in _2_1:
            next_1 += [x[0] for x in _2_1[key_2]]
    if len(next_1) < 5:
        if key_1 in _1_1:
            next_1 += [x[0] for x in _1_1[key_1]]
    
    next_2 =[]
    if key_3 in _3_2:
        next_2 += [x[0] for x in _3_2[key_3]]
    if len(next_2) < 5:
        if key_2 in _2_2:
            next_2 += [x[0] for x in _2_2[key_2]]
    if len(next_2) < 5:
        if key_1 in _1_2:
            next_2 += [x[0] for x in _1_2[key_1]]
    
    return next_1[:5], next_2[:5]

from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return jsonify(1)

@app.route('/predict/<text>')
def get_prediction(text):
    return jsonify(predict(text))

if __name__ == '__main__':
    app.run(debug=True)
