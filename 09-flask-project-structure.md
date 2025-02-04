# Flask project structure

## A simple Flask project looks like this below

- It has three main parts: frontend, backend, booting code(also in backend actually)
- The file structure is strict, like you'd better put your `.css` files in `/static/css/` directory, don't be lazy by just putting it under the root directory.

![flask diagram](./90-markdown_media/Screenshot%20from%202025-02-04%2014-49-51.png)

## Explaining the booting code

```python
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
```

> #### ** What is `__name__`?**
>
> In Python, `__name__` is a built-in variable that holds the name of the module that is currently being executed. When a Python script is run directly, `__name__` is set to `"__main__"`.
