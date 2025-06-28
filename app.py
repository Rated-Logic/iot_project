from flask import Flask, request, render_template_string

app = Flask(__name__)

# --- Styled Homepage ---
HOME_PAGE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>IoT Sensor API</title>
    <style>
        body {
            font-family: 'Segoe UI', sans-serif;
            background: #f5f9fc;
            color: #333;
            text-align: center;
            padding: 50px;
        }
        .container {
            background: white;
            padding: 30px;
            margin: auto;
            width: 80%;
            max-width: 500px;
            border-radius: 12px;
            box-shadow: 0 4px 12px rgba(0,0,0,0.1);
        }
        h1 {
            color: #0077cc;
        }
        code {
            background: #eef;
            padding: 3px 6px;
            border-radius: 6px;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>📡 IoT Sensor API</h1>
        <p>This API receives temperature and humidity readings from a GSM-connected device.</p>
        <p><strong>To submit data, use:</strong></p>
        <p>
            <code>/submit?temp=25&hum=60</code>
        </p>
        <p>Made with ❤ for IoT Projects</p>
    </div>
</body>
</html>
"""

# --- Styled Submit Page ---
SUBMIT_PAGE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Data Received</title>
    <style>
        body {
            font-family: 'Segoe UI', sans-serif;
            background: #e9f7ef;
            color: #2d3e50;
            text-align: center;
            padding: 60px;
        }
        .box {
            background: white;
            padding: 30px;
            margin: auto;
            width: 80%;
            max-width: 450px;
            border-radius: 12px;
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
        }
        h2 {
            color: #28a745;
        }
        .data {
            font-size: 1.2rem;
            margin: 15px 0;
        }
        .home-link {
            margin-top: 20px;
            display: inline-block;
            text-decoration: none;
            color: #0077cc;
        }
    </style>
</head>
<body>
    <div class="box">
        <h2>✅ Data Received Successfully!</h2>
        <p class="data"><strong>Temperature:</strong> {{ temp }} °C</p>
        <p class="data"><strong>Humidity:</strong> {{ hum }} %</p>
        <a href="/" class="home-link">← Back to Home</a>
    </div>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(HOME_PAGE)

@app.route('/submit', methods=['GET'])
def receive_data():
    temp = request.args.get('temp')
    hum = request.args.get('hum')

    if not temp or not hum:
        return "❌ Missing 'temp' or 'hum' in query string."

    # Optional: log to file
    with open("data_log.txt", "a") as f:
        f.write(f"Temp: {temp}, Humidity: {hum}\n")

    return render_template_string(SUBMIT_PAGE, temp=temp, hum=hum)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
