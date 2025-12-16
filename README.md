# App List API (Flask)

## Run
source venv/bin/activate
pip install flask flask-cors
python app.py

## Endpoints
GET /health
GET /apps?search=<text>
GET /apps/<id>
GET /images/<filename>

## Notes
- Loads JSON into memory for simplicity.
- Search is case-insensitive (name/category/description).
- Errors return: { "error": { "code": "...", "message": "..." } }
- With more time: pagination, DB storage, indexing, caching, validation, tests.