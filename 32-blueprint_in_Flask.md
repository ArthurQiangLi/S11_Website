# Blueprint

Used for: Organizing and modularize big application into small and resuable components.

```py
in app/routes.py

main = Blueprint('main', __name__) # creat a blueprint instance, to defaine routes and register them into Flask app later

@main.route('/')   # This decorator here claims route `@main.route()` belongs to blueprint `main`
def index():
    return render_template('index.html')
```

```py
in __init__.py
from app.routes import main # from app/routes.py

def create_app():
    app = Flask(__name__)
    app.register_blueprint(main)    # Register the 'main' blueprint with the Flask app
    return app

```

## 1. One example of 3-people team

You have tasks for 3 people each:

1. in main.py, worker1 defines routes in this file
2. in auth.py worker2 defines routes in this file
3. in file_mgmt.py Worker3 defines routes in this file

```py
from app.routes.main import main # from work1's file improt the 'main' blueprint.
from app.routes.auth import auth
from app.routes.file_mgmt import file_mgmt

def create_app():
    app = Flask(__name__)

    # Register all blueprints from 3 workers.
    app.register_blueprint(main)
    app.register_blueprint(auth, url_prefix='/auth')
    app.register_blueprint(file_mgmt, url_prefix='/files')

    return app

```

## 2. Comparing the booting code using Blueprint or not

```python
from flask import Flask, render_template, Blueprint

bp_main = Blueprint('main', __name__)

@bp_main.route('/')
def index():
    return render_template('main.html')

if __name__ == '__main__':
    app = Flask(__name__)
    app.register_blueprint(bp_main)
    app.run(debug=True, host='0.0.0.0', port=5000)
```

Alternatively, if you don't use Blueprint.

```python
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
```
