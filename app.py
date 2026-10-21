from flask import Flask, render_template, request, jsonify
from processing.calculator import FleetCalculator
import os

app = Flask(__name__)
DATA_PATH = os.path.join('data', 'drone_costs.csv')
calc = FleetCalculator(DATA_PATH)

@app.route('/', methods = ['GET', 'POST'])
def home():
  proposal = None
  if request.method == 'POST':
    # Get customer constraints
    drones = int(request.form.get('drones', 100))
    region = request.form.get('region', 'North America')
    complexity = request.form.get('complexity', '3D Animated')

    proposal = calc.calculate_proposal(drones, region, complexity)

  return render_template('index.html', proposal = proposal)

if __name__ == '__main__':
  app.run(debug = True)
