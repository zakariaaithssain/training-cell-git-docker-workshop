# 🛒 Workshop Marketplace

A collaborative FastAPI project for learning Git branching, merging, and Docker containerization.

## 🚀 Quick Start (Local)
### Run the App
```bash
# Install dependencies
uv sync

# Run the app
uvicorn website.main:app --reload
```

Visit: http://localhost:8000

### Notes
- The app automatically mounts `/static` and `/templates` directories
- Database is initialized automatically on first run with seed data
- Hot-reload is enabled with `--reload` flag

## 🐳 Docker

### Build & Run

```bash
# Build the image
docker build -t workshop-marketplace .

# Run the container
docker run -p 8000:8000 workshop-marketplace
```

### How It Works
- Uses Python 3.13-slim as base image
- Dependencies are managed with `uv` (see `pyproject.toml`)
- `PYTHONPATH` is set to `/app/src` to properly resolve the `website` module
- Virtual environment is activated in the container PATH

## 📁 Project Structure

```
fastapi-workshop/
├── app/
│   ├── src/
│   │   └── website/
│   │       ├── __init__.py
│   │       ├── main.py              # ⚠️ DO NOT EDIT
│   │       ├── core/
│   │       │   ├── __init__.py
│   │       │   ├── config.py        # ⚠️ DO NOT EDIT
│   │       │   ├── database.py      # ⚠️ DO NOT EDIT
│   │       │   ├── models.py        # ⚠️ DO NOT EDIT
│   │       │   └── init_db.py       # ⚠️ DO NOT EDIT
│   │       ├── shops/
│   │       │   ├── __init__.py
│   │       │   ├── group_1.py       # ✅ Group 1 edits this
│   │       │   ├── group_2.py       # ✅ Group 2 edits this
│   │       │   └── group_3.py       # ✅ Group 3 edits this
│   │       │ 
│   │       │ 
│   │       ├── static/              # 🎨 Assets (CSS, JS, Images) # ⚠️ DO NOT EDIT
│   │       └── templates/           # 📄 HTML Templates           # ⚠️ DO NOT EDIT
│   ├── Dockerfile     # ⚠️ DO NOT EDIT
│   ├── pyproject.toml # ⚠️ DO NOT EDIT
│   └── README.md      # ⚠️ DO NOT EDIT
```

## 📝 Workshop Rules

1. **You may only edit your group's file** inside `src/website/shops/`.
2. **Never touch the other files**
3. Work on your own branch.
4. Never work or push in `main`.
4. The instructor will merge all branches into `main`.

## 🔗 API Endpoints

| Endpoint | Description |
|----------|-------------|
| `GET /` | Welcome message |
| `GET /docs` | Swagger UI (FastAPI Documentation) |
| `GET /1/products` | Group 1's products |
| `GET /2/products` | Group 2's products |
| `GET /3/products` | Group 3's products |
