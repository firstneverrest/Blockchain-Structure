# Blockchain Structure

## Tools

![image](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=darkgreen)
![image](https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white)

## Web Server

Flask is a micro web framework written in Python. It does not require particular tools or libraries like other framework. Therefore, just a few line of code can create website.

### Installation

1. check pip

```
pip list
```

2. install flask via pip

```
pip install Flask
```

### Write Flask server

```py
# web server
app = Flask(__name__)

@app.route('/')
def hello():
    return '<h1>Hello Blockchain!</h1>'

# run server
if __name__ == '__main__':
    app.run()
```
