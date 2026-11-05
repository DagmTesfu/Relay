# test_engine.py

# Import the engine code we want to test
from app.engine import execute_workflow

# Test 1: Happy Path (All steps should pass smoothly)
def test_successful_workflow():
    my_workflows = {
        "name": "Daily Sales Automation",
        "steps": ["validate_sale", "save_sale", "notify_manager"]
    }
    my_sale_data = {
        "product": "Chocolate Cake",
        "quantity": 2,
        "amount": 500
    }
    
    # We expect the engine to return True
    assert execute_workflow(my_workflows, my_sale_data) is True

# Test 2: Validation Failure Path (Quantity is 0)
def test_failed_validation_workflow():
    my_workflows = {
        "name": "Daily Sales Automation",
        "steps": ["validate_sale", "save_sale"]
    }
    invalid_sale_data = {
        "product": "Chocolate Cake",
        "quantity": 0,  # This will trigger the False return in validate_sale
        "amount": 500
    }
    
    # We expect the engine to return False and stop early
    assert execute_workflow(my_workflows, invalid_sale_data) is False

# Test 3: Unknown Step Path (Action doesn't exist in registry)
def test_unknown_action_workflow():
    my_workflows = {
        "name": "Daily Sales Automation",
        "steps": ["non_existent_action"]
    }
    my_sale_data = {
        "product": "Chocolate Cake",
        "quantity": 2,
        "amount": 500
    }
    
    # We expect the engine to recognize the bad step and return False
    assert execute_workflow(my_workflows, my_sale_data) is False
