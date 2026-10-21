import pandas as pd

class FleetCalculator:
  def __init__(self, data_path):
    self.df = pd.read_csv(data_path)

  def calculate_proposal(self, desired_drones, region = "North America", complexity = "3D Animated"):
    # Grab operational cost baselines
    regional_mask = self.df['region'] == region
    # Match tiers based on fleet scale bounds
    tier = self.df[regional_mask & (self.df['min_drones'] <= desired_drones) & (self.df['max_drones'] >= desired_drones)]

    if tier.empty:
      # Default values
      per_drone_rate = 230
      logistics = 20000
    else:
      per_drone_rate = trier.iloc[0]['avg_cost_per_drone']
      logistics = tier.iloc[0]['base_logistics_fee']

    # Apply complexity factors

    if complexity == "3D Animated":
      complexity_multiplier = 1.3
    else:
      complexity_multiplier = 1

    drone_cost = desired_drones * per_drone_rate * complexity_multiplier
    total_estimate = drone_cost + logistics

    # Space constraints
    required_space_sq_m = desired_drones * 9

    return {
      "fleet_size": desired_drones,
      "drone_cost": round(drone_cost, 2),
      "logistics_fee": logistics,
      "total_price": round(total_estimate, 2),
      "required_takeoff_area_sq_m": required_takeoff_area_sq_m
    }
