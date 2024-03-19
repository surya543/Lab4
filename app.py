from flask import Flask, render_template, request
import pandas as pd
from sklearn.linear_model import LinearRegression

app = Flask(__name__)

# Load trained model
model = LinearRegression()
# Assuming model is trained and ready for prediction

# Render HTML template for input form
@app.route('/')
def index():
    return render_template('index.html')

# Handle form submission and prediction
@app.route('/predict', methods=['POST'])
def predict():
    # Retrieve input data from form
    length = float(request.form['length'])
    width = float(request.form['width'])
    height = float(request.form['height'])
    
    # Perform prediction using the model
    prediction = model.predict([[length, width, height]])
    
    # Pass prediction result to HTML template for display
    return render_template('index.html', prediction=prediction[0])

if __name__ == '__main__':
    app.run(debug=True)
