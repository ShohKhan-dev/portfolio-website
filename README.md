# My Personal Portfolio
![image](front-page.png)

![python](https://img.shields.io/badge/-python-grey?style=for-the-badge&logo=python&logoColor=white&labelColor=306998)
![django](https://img.shields.io/badge/-django-grey?style=for-the-badge&logo=django&logoColor=white&labelColor=092e20)
![linux](https://img.shields.io/badge/linux-grey?style=for-the-badge&logo=linux&logoColor=white&labelColor=072c61)
![Git](https://img.shields.io/badge/git-%23F05033.svg?style=for-the-badge&logo=git&logoColor=white)
![HTML](https://img.shields.io/badge/-html/css-grey?style=for-the-badge&&logoColor=white&labelColor=306998)
![django](https://img.shields.io/badge/-JavaScript-grey?style=for-the-badge&logoColor=white&labelColor=092e20)
![vercel](https://img.shields.io/badge/vercel-grey?style=for-the-badge&logo=vercel&logoColor=white&labelColor=072c61)

### Language: python 3.9 +

### Frameworks : Django 4+

### Deployment: vercel, Bash

### Database : Sqlite



# About
My perconal portfolio website that I store my academic and portfolio information. Blogs, My CV, Projects

![image](projects-page.png)


# Project Setup



# Architecture

```
.
└── app
    └── portfolio
        ├──  migrations
        ├──  __init__.py
        ├──  admin.py
        ├──  apps.py
        ├──  models.py
        ├──  api.py
        ├──  tests.py
        ├──  urls.py
        ├──  views.py
    └──  config
        ├──  __init__.py
        ├──  asgi.py
        ├──  urls.py
        ├──  settings.py
        ├──  wsgi.py
        
    ├── .gitignore
    ├── .gitlab-ci.yml
    ├──  manage.py
    ├──  requirements.txt
```

### models.py

```python
from core.base_model import BaseModel
from django.db import models


class MyModel(BaseModel):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name
```

### views.py

## urls.py

```python
from django.urls import path

'from .views import MyView'

urlpatterns = [
    path("article/", views.article, name="article"),
]
```

### main.urls.py

```python
from django.urls import path, include

urlpatterns = [
    path('/api/v1/{app_name}/', include('{app_name.urls}'))
]
```
