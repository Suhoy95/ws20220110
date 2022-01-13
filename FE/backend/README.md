# Hello, world!

```bash
mkdir backend && cd backend && \
  echo -e "venv\n__pycache__\n.idea/\ndb.sqlite3\n.DS_Store" > .gitignore && \
  echo "# Hello, world!" > README.md && \
  python -m venv venv && . venv/Scripts/activate && \
  pip install django && \
  django-admin startproject mysite . && python manage.py startapp blog && \
  pip freeze > requirements.txt && \
  git add . && git commit -m "Django-project has been created"
```

```json
{
    "name": "Мега-рогалик",
    "map": [
        {
            "img-source": "url-картинки",
            "name": "Название карты"
        }
    ]
}
```