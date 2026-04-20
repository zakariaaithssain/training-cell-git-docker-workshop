# 🛒 Workshop Marketplace

A collaborative FastAPI project for learning Git branching, merging, and Docker containerization.

## 🚀 Quick Start (Local)

```bash
uv sync

#run the app
uvicorn website.main:app --reload
```

Visit: http://localhost:8000/docs

## 🐳 Docker

```bash
# Build the image
docker build -t workshop-marketplace .

# Run the container
docker run -p 8000:8000 workshop-marketplace
```

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
│   │       │   └── models.py        # ⚠️ DO NOT EDIT
│   │       └── shops/
│   │           ├── __init__.py
│   │           ├── group_1.py   # ✅ Group 1 edits this
│   │           ├── group_2.py    # ✅ Group 2 edits this
│   │           └── group_3.py   # ✅ Group 3 edits this
│   ├── Dockerfile
│   ├── pyproject.toml
│   └── README.md
```

## 📝 Workshop Rules

1. **You may only edit your group's file** inside `src/website/shops/`.
2. **Never touch `src/website/main.py` or `src/website/core/`.**
3. Work on your own branch, push it, then tell the instructor.
4. The instructor will merge all branches into `main`.

## 🔗 API Endpoints

| Endpoint | Description |
|----------|-------------|
| `GET /` | Welcome message |
| `GET /1/products` | Group 1's products |
| `GET /2/products` | Group 2's products |
| `GET /3/products` | Group 3's products |
