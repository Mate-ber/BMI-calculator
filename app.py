from flask import Flask, render_template, redirect, url_for, request
import datetime

app = Flask(__name__)

bmi_values = []

@app.route('/calculate_bmi', methods=['GET'])
def calculate_bmi():
    weight = request.args.get('weight')
    height = request.args.get('height')

    try:
        weight = float(weight)
        height = float(height) / 100  # Convert cm to meters
    except (ValueError, TypeError):
        return render_template('index.html', bmi=None, average_bmi=None)

    bmi = round(weight / (height * height), 2)
    bmi_values.append(bmi)

    # Calculate the average BMI
    average_bmi = round(sum(bmi_values) / len(bmi_values), 2)

    return render_template('index.html', bmi=bmi, average_bmi=average_bmi)
