from flask import Flask, request, jsonify
import os, datetime
app = Flask(__name__)
UPLOAD = '/tmp/uploads'
os.makedirs(UPLOAD, exist_ok=True)

@app.route('/upload', methods=['POST'])
def upload():
    f = request.files.get('file') or request.files.get('dosya')
    if not f: return {'error':'no file'}, 400
    name = datetime.datetime.utcnow().strftime('%Y%m%d_%H%M%S') + '_' + f.filename
    f.save(os.path.join(UPLOAD, name))
    return {'status':'ok','file':name}, 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
