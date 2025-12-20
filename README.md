# django template

## Structure
```commandline
template
|
⊢ app
  |
  ⊢ migrations
      ⨽ __init__.py
  |
  ⊢ __init__.py
  ⊢ admin.py
  ⊢ apps.py
  ⊢ models.py
  ⊢ tests.py
  ⨽ views.py
|

|
⊢ media
|

|
⊢ project
  ⊢ __init__.py
  ⊢ asgi.py
  ⊢ settings.py
  ⊢ urls.py
  ⨽ wsgi.py
|

|
⊢ static
  ⊢ css
  |
     ⨽ styles.css
  |
  ⊢ img
  ⊢ js
  |
     ⨽ script.js
  |
|

|
⊢ templates
  ⨽ index.html
|
⊢ manange.py
⊢ README.md
⨽ requirements.txt 
```


1. set the venv enviroment
2. download dependencies  
```pip install -r requirements.txt```  
if doesn't work try this:  
```uv pip install -r requirements.txt```