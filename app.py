from flask import Flask, request, render_template_string
import pickle

app = Flask(__name__)

# Load model
# model = pickle.load(open("phishing_model.pkl", "rb"))

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>Phishing URL Detector</title>
</head>
<body>
    <h2>Phishing URL Detector</h2>

    <form method="POST">
        <input type="text" name="url" placeholder="Enter URL" required>
        <button type="submit">Check</button>
    </form>

    {% if prediction is not none %}
        <h3>Result:</h3>
        {% if prediction == 1 %}
            <p style="color:red;">⚠️ Phishing URL</p>
        {% else %}
            <p style="color:green;">✅ Safe URL</p>
        {% endif %}
    {% endif %}
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def home():
    prediction = None

    if request.method == "POST":
        url = request.form["url"]
        # dummy prediction (replace later with real features)
        prediction = 1 if "login" in url else 0

    return render_template_string(HTML, prediction=prediction)

if __name__ == "__main__":
    app.run(debug=True)
