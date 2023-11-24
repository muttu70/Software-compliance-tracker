import datetime
import uuid
import random
import string

class SoftwareComplianceTracker:
    def __init__(self):
        self.software_data = []
        print("Welcome to software compliance tracker")

    def generate_random_software_id(self):
        return str(uuid.uuid4())[:3]  

    def generate_access_key(self):
         return ''.join(random.choices(string.ascii_letters + string.digits, k=4))

    def create_software(self, name, license_type, validity_days):
        software_id = self.generate_random_software_id()  
        expiry_date = (datetime.date.today() + datetime.timedelta(days=validity_days)).strftime("%Y-%m-%d")
        access_key = self.generate_access_key()
        software_info = {
            'software_id': software_id,
            'name': name,
            'license_type': license_type,
            'expiry_date': expiry_date,
            'activation_status': 'Not Activated',
            'access_key': access_key
        }
        self.software_data.append(software_info)
        return f"{license_type} software {name} created successfully with expiry date: {expiry_date}. Software ID: {software_id}, Access Key: {access_key}"

    def display_available_software(self):
        available_software = "\nAvailable Software:\n"
        for software_info in self.software_data:
            available_software += f"Software ID: {software_info['software_id']}, Name: {software_info['name']}, Activation Status: {software_info['activation_status']}\n"
        return available_software

    def display_expiring_software(self, days_threshold=30):
        expiring_software = f"\nExpiring Software within the next {days_threshold} days:\n"
        current_date = datetime.date.today()
        for software_info in self.software_data:
            expiry_date = datetime.datetime.strptime(software_info['expiry_date'], "%Y-%m-%d").date()
            days_until_expiry = (expiry_date - current_date).days
            if 0 < days_until_expiry <= days_threshold:
                expiring_software += f"Software ID: {software_info['software_id']}, Name: {software_info['name']}, Expiry Date: {software_info['expiry_date']}, Days until expiry: {days_until_expiry}\n"
        return expiring_software

    def read_software_validity(self, software_id):
        for software_info in self.software_data:
            if software_info['software_id'] == software_id:
                expiry_date = datetime.datetime.strptime(software_info['expiry_date'], "%Y-%m-%d").date()
                current_date = datetime.date.today()

                if expiry_date >= current_date:
                    days_until_expiry = (expiry_date - current_date).days
                    return f"{software_info}\nLicense is valid for {days_until_expiry} days."
                else:
                    days_since_expiry = (current_date - expiry_date).days
                    return f"{software_info}\nSoftware has expired! Days since expiry: {days_since_expiry}"
        
        return f"Software with ID {software_id} not found."

    def activate_software(self, software_id, access_key):
        for software_info in self.software_data:
            if software_info['software_id'] == software_id:
                if software_info['activation_status'] == 'Not Activated' and software_info['access_key'] == access_key:
                    software_info['activation_status'] = 'Activated'
                    return f"Software with ID {software_id} activated successfully."
                elif software_info['activation_status'] == 'Activated':
                    return f"Software with ID {software_id} is already activated."
                else:
                    return "Invalid access key. Activation failed."

        return f"Software with ID {software_id} not found."

    def get_expiry_date(self, software_id):
        for software_info in self.software_data:
            if software_info['software_id'] == software_id:
                return f"Software with ID {software_id} has expiry date: {software_info['expiry_date']}"

        return f"Software with ID {software_id} not found."

    def update_software(self, software_id, name):
        for software_info in self.software_data:
            if software_info['software_id'] == software_id:
                license_type = software_info['license_type']
                expiry_date = datetime.datetime.strptime(software_info['expiry_date'], "%Y-%m-%d").date()

                if license_type == 'Mobile Validity':
                    amount = input(f"Enter the amount (in rupees) to extend the expiry date for {name}:\n1. 250 rupees for 28 days\n2. 600 rupees for 3 months\n")
                    try:
                        amount = int(amount)
                    except ValueError:
                        return "Invalid amount. Please enter a valid integer."

                    if amount == 1:
                        days_to_extend = 28
                    elif amount == 2:
                        days_to_extend = 90
                    else:
                        return "Invalid amount. Unable to extend the expiry date."

                elif license_type == 'Antivirus Update':
                    amount = input(f"Enter the amount (in rupees) to extend the expiry date for {name}:\n1. 800 rupees for 180 days\n2. 1500 rupees for 365 days\n")
                    try:
                        amount = int(amount)
                    except ValueError:
                        return "Invalid amount. Please enter a valid integer."

                    if amount == 1:
                        days_to_extend = 180
                    elif amount == 2:
                        days_to_extend = 365
                    else:
                        return "Invalid amount. Unable to extend the expiry date."

                elif license_type == 'Health License':
                    amount = input(f"Enter the amount (in rupees) to extend the expiry date for {name}:\n1. 5000 rupees for 2 years\n2. 7000 rupees for 5 years\n")
                    try:
                        amount = int(amount)
                    except ValueError:
                        return "Invalid amount. Please enter a valid integer."

                    if amount == 1:
                        days_to_extend = 730  # 2 years
                    elif amount == 2:
                        days_to_extend = 1825  # 5 years
                    else:
                        return "Invalid amount. Unable to extend the expiry date."

                new_expiry_date = (expiry_date + datetime.timedelta(days=days_to_extend)).strftime("%Y-%m-%d")

                software_info.update({
                    'name': name,
                    'expiry_date': new_expiry_date,
                    
                })
                return f"Software with ID {software_id} updated successfully. New expiry date: {new_expiry_date}"

        return f"Software with ID {software_id} not found."

    def delete_software(self, software_id):
        for software_info in self.software_data:
            if software_info['software_id'] == software_id:
                self.software_data.remove(software_info)
                return f"Software with ID {software_id} deleted successfully."
        
        return f"Software with ID {software_id} not found."

    def audit_compliance(self):
        audit_result = "\nSoftware Compliance Audit:\n"

        for software_info in self.software_data:
            audit_result += f"Software ID: {software_info['software_id']}, Name: {software_info['name']}, License Type: {software_info['license_type']}, Expiry Date: {software_info['expiry_date']}, Activation Status: {software_info['activation_status']}\n"
            
        return audit_result

tracker = SoftwareComplianceTracker()

while True:
    print("\n1. Create Mobile Validity Software\t2. Create Antivirus Update Software\t3. Create Health License Software\n4. Read Software Validity\t\t5. Update Software\t\t\t6. Delete Software\n7. Display Available Software\t\t8. Display Expiring Software\t\t9. Activate Software\n10. Get Expiry Date\t\t\t11. Exit")
    choice = input("Enter your choice (1-11): ")

    if choice == '1':
        name = input("Enter mobile software name: ")
        validity_days = 28
        print(tracker.create_software(name, 'Mobile Validity', validity_days))
    elif choice == '2':
        name = input("Enter antivirus software name: ")
        validity_days = 90
        print(tracker.create_software(name, 'Antivirus Update', validity_days))
    elif choice == '3':
        name = input("Enter health license software name: ")
        validity_days = 365
        print(tracker.create_software(name, 'Health License', validity_days))
    elif choice == '4':
        software_id = input("Enter software ID to read: ")
        print(tracker.read_software_validity(software_id))
    elif choice == '5':
        software_id = input("Enter software ID to update: ")
        name = input("Enter updated software name: ")
        print(tracker.update_software(software_id, name))
    elif choice == '6':
        software_id = input("Enter software ID to delete: ")
        print(tracker.delete_software(software_id))
    elif choice == '7':
        print(tracker.display_available_software())
    elif choice == '8':
        print(tracker.display_expiring_software())
    elif choice == '9':
        software_id = input("Enter software ID to activate: ")
        access_key = input("Enter access key for activation: ")
        print(tracker.activate_software(software_id, access_key))
    elif choice == '10':
        software_id = input("Enter software ID to get expiry date: ")
        print(tracker.get_expiry_date(software_id))
    elif choice == '11':
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 11.") 