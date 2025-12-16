import json
from pathlib import Path
from typing import Optional
from utils.errors import ApiError

DATA_PATH = Path(__file__).parent.parent / "data" / "apps.json"

# Load sample data once at startup
# In production, use a database
with open(DATA_PATH, "r") as f:
    data = json.load(f)
    APPS = data.get("apps", [])

def list_apps(search: Optional[str] = None):
    if not search:
        return APPS
    
    q = search.strip().lower()
    if not q:
        return APPS
    
    return [
            app for app in APPS
            if q in app.get("name", "").lower()
            or q in app.get("tagline", "").lower()
    ]

def get_app_by_id(app_id: str):
    for app in APPS:
        if str(app["id"]) == str(app_id):
            return app
    raise ApiError("APP_NOT_FOUND", "App not found", 404)
