from flask import Flask, request, jsonify
from flask_cors import CORS
from services.app_service import list_apps, get_app_by_id
from utils.errors import ApiError

app = Flask(__name__, static_folder='static')
CORS(app)

@app.get("/health")
def health():
    return jsonify({"ok": True})

@app.get('/apps')
def apps():
    try:
        search = request.args.get('search')
        items = list_apps(search)
       
        # add iconUrl for clients
        data = []
        for item in items:
            obj = dict(item)
            if 'icon' in obj:
                obj['iconUrl'] = f"/images/{obj['icon']}"
            data.append(obj)

        return jsonify({'data': data, 'count': len(data)})
    except Exception as e:
        resp = ApiError.error_response(e)
        return jsonify(resp), resp['status']
    
@app.get("/apps/<app_id>")
def app_by_id(app_id):
    try:
        app = get_app_by_id(app_id)
        if 'icon' in app:
            app['iconUrl'] = f"/images/{app['icon']}"
        return jsonify({'data': app})
    except Exception as e:
        resp = ApiError.error_response(e)
        return jsonify(resp), resp['status']
    

# static images are served from /static/icons
@app.get("/images/<path:filename>")
def images(filename):
    return app.send_static_file(f"images/{filename}")

def main():
    app.run(port=5000, debug=True)

if __name__ == "__main__":
    main()
