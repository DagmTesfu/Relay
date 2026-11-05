# app/engine.py

def validate_sale(sale_data):
    if sale_data["quantity"] > 0:
        print("Sale validated successfully.")
        return True
    else: 
        print("Error: Invalid sale amount.")  
        return False

def save_sale(sale_data):
    print("Sale saved successfully.")
    return True

def notify_manager(sale_data):
    print("Manager notified successfully.")
    return True

# 💡 ENSURE THIS IS DEFINED ABOVE THE ENGINE LOOP
actions_registry = {
    "validate_sale": validate_sale,
    "save_sale": save_sale,
    "notify_manager": notify_manager
}

def execute_workflow(workflow, sale_data):
    print("Starting workflow: ", workflow["name"])
    print()
    
    for step in workflow["steps"]:
        print("Executing: ", step)
        
        # This will now successfully see the dictionary above
        action_function = actions_registry.get(step)
        
        if action_function is None:
            print("Error: Action '", step, "' not found!")
            return False  
            
        success = action_function(sale_data)
        
        if not success:
            print("Workflow halted due to failure.")
            return False  
            
        print() 
                
    print("Workflow completed successfully.")
    return True
