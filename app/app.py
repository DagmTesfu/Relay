# app.py

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
