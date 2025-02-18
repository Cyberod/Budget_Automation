import json
import os

FILE_PATH = 'budget_plans.json'

def save_budget_plan(plan_name, budget_plan, subcategories=None):
    """Save custom budget plans to storage."""
    plans = load_budget_plans()  # Load existing plans safely
    if subcategories:
        plans[plan_name] = {"categories": budget_plan, "subcategories": subcategories}
    else:
        plans[plan_name] = budget_plan  

    with open(FILE_PATH, 'w') as f:
        json.dump(plans, f, indent=4)

def load_budget_plans():
    """Load all saved budget plans from storage."""
    if not os.path.exists(FILE_PATH) or os.path.getsize(FILE_PATH) == 0:
        return {}  # Return an empty dictionary if file does not exist or is empty
    
    try:
        with open(FILE_PATH, 'r') as f:
            return json.load(f)
    except (json.JSONDecodeError, FileNotFoundError):
        return {}  # Return empty dictionary on error
