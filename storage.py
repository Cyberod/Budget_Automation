import json
import os

def save_budget_plan(plan_name, budget_plan):
    """Save custom budget plans to storage."""

    try:
        with open('budget_plans.json', 'r') as f:
            plans = json.load(f)
        
    except FileNotFoundError:
        plans = {}

    plans[plan_name] = budget_plan

    with open('budget_plans.json', 'w') as f:
        json.dump(plans, f)



def load_budget_plans():
    "Loads all saved budget plans from storage."""


    try:
        if os.path.getsize('budget_plans.json') > 0:
            with open('budget_plans.json', 'r') as f:
                return json.load(f)
        return{}
    except (FileNotFoundError, json.JSONDecodeError):
        return{}
