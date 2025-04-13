@app.route('/')
def hello_world():
    return '<h1>Hello World :)</h1>'

@app.route('/greet')
@app.route('/greet/<name>')
def greet(name=""):
    return f"Hello {name}"

def celsius_to_fahrenheit(celsius):
    return celsius * 9 / 5 + 32

@app.route('/convert/<celsius>')
def convert(celsius):
    try:
        c = float(celsius)
        f = celsius_to_fahrenheit(c)
        return f"{c}°C is {f:.2f}°F"
    except ValueError:
        return "Invalid input! Please enter a number."
