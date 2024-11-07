from flask import Flask, jsonify, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('dashboard.html')

@app.route('/api/costs', methods=['GET'])
def get_costs():
    cost_data = [
        {'service': 'AWS CloudShell', 'cost': 0.0},
        {'service': 'AWS CloudTrail', 'cost': 0.127153},
        {'service': 'AWS Cost Explorer', 'cost': 0.16},
        {'service': 'AWS Glue', 'cost': 0.0},
        {'service': 'AWS Key Management Service', 'cost': 0.0},
        {'service': 'AWS Lambda', 'cost': 0.0},
        {'service': 'AWS Step Functions', 'cost': 0.0},
        {'service': 'Amazon API Gateway', 'cost': 0.0},
        {'service': 'Amazon QuickSight', 'cost': 0.0},
        {'service': 'Amazon Simple Notification Service', 'cost': 0.0},
        {'service': 'Amazon Simple Queue Service', 'cost': 0.0},
        {'service': 'Amazon Simple Storage Service', 'cost': 0.01},
        {'service': 'Amazon CloudWatch', 'cost': 0.0},
    ]
    return jsonify(cost_data)

if __name__ == '__main__':
    app.run(debug=True)
