from flask import Flask, request, json, Response

app = Flask(__name__)

def api_set_gps():
 if request.headers['Content-Type'] == 'text/plain':
  return "Sent Text: " + request.data
 elif request.headers['Content-Type'] == 'application/json':
  return "Sent JSON: " + json.dumps(request.json)

def api_get_gps():
 data = {'X' : 'X_Coord', 'Y' : 'Y_Coord'}
 js = json.dumps(data)
 resp = Response(js, status=200, mimetype='application/json')
 return resp
  
@app.route('/gps/', methods = ['POST', 'GET'])
def api_handler():
 if request.method == 'GET':
  return api_get_gps()
 elif request.method == 'POST':
  return api_set_gps()

if __name__ == '__main__':
 #app.run(host='10.221.85.10', port = 5000, debug=True)
 app.run(debug=True)
