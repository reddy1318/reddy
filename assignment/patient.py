#write a method to takes details  from the patient the store

class PatientManagementSystem:
    def _init_(self):
        self.patient_records = [] 
        self.patient_info = {}  
    def add_patient(self, name, age, gender, address, phone_number, medical_history=None):
        patient_record = {
            "Name": name,
            "Age": age,
            "Gender": gender,
            "Address": address,
            "Phone Number": phone_number,
        }
        if medical_history is not None:
            patient_record["Medical History"] = medical_history

        self.patient_records.append(patient_record)
        self.patient_info[name] = {
            "Age": age,
            "Gender": gender,
            "Address": address,
            "Phone Number": phone_number,
        }
        if medical_history is not None:
            self.patient_info[name]["Medical History"] = medical_history
    def get_patient_info(self, name):
        if name in self.patient_info:
            return self.patient_info[name]
        else:
            return "Patient not found in the system."
    def list_all_patients(self):
        return self.patient_records
patient_system = PatientManagementSystem()
patient_system.add_patient("John Doe", 35, "Male", "123 Main St", "555-123-4567", "Hypertension")
patient_system.add_patient("Jane Smith", 28, "Female", "456 Elm St", "555-987-6543")
patient_info = patient_system.get_patient_info("John Doe")
print("Patient Information:")
print(patient_info)
all_patients = patient_system.list_all_patients()
print("\nAll Patients:")
for patient in all_patients:
    print(patient)


#write a method to display all the details of patients
class PatientManagementSystem:
    def _init_(self):
        self.patient_records = [] 
        self.patient_info = {}  
    def add_patient(self, name, age, gender, address, phone_number, medical_history=None):
        patient_record = {
            "Name": name,
            "Age": age,
        }
class PatientManagementSystem:
    def display_all_patients(self):
        print("Patient Details:")
        for patient_record in self.patient_records:
            print("Patient Record:")
            for key, value in patient_record.items():
                print(f"{key}: {value}")
patient_system = PatientManagementSystem()
patient_system.add_patient("John Doe", 35, "Male", "123 Main St", "555-123-4567", "Hypertension")
patient_system.add_patient("Jane Smith", 28, "Female", "456 Elm St", "555-987-6543")
patient_system.display_all_patients()


#write a method to search particular patient from the list search by id
class PatientManagementSystem:
    def _init_(self):
        self.patient_records = [] 
        self.patient_info = {}  
    def add_patient(self, patient_id, name, age, gender, address, phone_number, medical_history=None):
        patient_record = {
            "ID": patient_id,
            "Name": name,
            "Age": age,
            "Gender": gender,
            "Address": address,
            "Phone Number": phone_number,
        }
        if medical_history is not None:
            patient_record["Medical History"] = medical_history
        self.patient_records.append(patient_record)
        self.patient_info[patient_id] = {
            "Name": name,
            "Age": age,
            "Gender": gender,
            "Address": address,
            "Phone Number": phone_number,
        }

        if medical_history is not None:
            self.patient_info[patient_id]["Medical History"] = medical_history

    def search_patient_by_id(self, patient_id):
        if patient_id in self.patient_info:
            return self.patient_info[patient_id]
        else:
            return "Patient not found in the system."
patient_system = PatientManagementSystem()
patient_system.add_patient(1, "John Doe", 35, "Male", "123 Main St", "555-123-4567", "Hypertension")
patient_system.add_patient(2, "Jane Smith", 28, "Female", "456 Elm St", "555-987-6543")
patient_id_to_search = 1
patient_info = patient_system.search_patient_by_id(patient_id_to_search)
print("Patient Information:")
print(patient_info)



#write a method delete a particular patient details by id.
hospital_records = []
def add_patient_details():
    patient_id = input("Enter patient ID: ")
    for patient in hospital_records:
        if patient["ID"] == patient_id:
            print("Patient ID already exists. Please choose a different ID.")
            return
    name = input("Enter patient name: ")
    age = input("Enter patient age: ")
    gender = input("Enter patient gender: ")
    disease = input("Enter patient disease: ")
    patient_data = {
        "ID": patient_id,
        "Name": name,
        "Age": age,
        "Gender": gender,
        "Disease": disease
    }
    hospital_records.append(patient_data)
    print("Patient details added successfully!")
def search_patient_by_id(patient_id):
    found = False
    for patient in hospital_records:
        if patient["ID"] == patient_id:
            found = True
            print("Patient ID:", patient["ID"])
            print("Name:", patient["Name"])
            print("Age:", patient["Age"])
            print("Gender:", patient["Gender"])
            print("Disease:", patient["Disease"])
            break
    if not found:
        print("Patient not found.")
def delete_patient_by_id(patient_id):
    """Delete a patient by ID."""
    found = False
    for patient in hospital_records:
        if patient["ID"] == patient_id:
            hospital_records.remove(patient)
            found = True
            print("Patient with ID", patient_id, "deleted successfully.")
            break
    if not found:
        print("Patient not found. Deletion failed.")
def main():
    while True:
        print("\nHospital Management System")
        print("1. Add Patient Details")
        print("2. Search for a Patient by ID")
        print("3. Delete a Patient by ID")
        print("4. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            add_patient_details()
        elif choice == '2':
            patient_id = input("Enter patient ID to search: ")
            search_patient_by_id(patient_id)
        elif choice == '3':
            patient_id = input("Enter patient ID to delete: ")
            delete_patient_by_id(patient_id)
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()



#   write a method to update a selected patient details by id.
hospital_records = []
def add_patient_details():
    patient_id = input("Enter patient ID: ")
    for patient in hospital_records:
        if patient["ID"] == patient_id:
            print("Patient ID already exists. Please choose a different ID.")
            return

    name = input("Enter patient name: ")
    age = input("Enter patient age: ")
    gender = input("Enter patient gender: ")
    disease = input("Enter patient disease: ")
    patient_data = {
        "ID": patient_id,
        "Name": name,
        "Age": age,
        "Gender": gender,
        "Disease": disease
    }
    hospital_records.append(patient_data)
    print("Patient details added successfully!")
def search_patient_by_id(patient_id):
    found = False
    for patient in hospital_records:
        if patient["ID"] == patient_id:
            found = True
            print("Patient ID:", patient["ID"])
            print("Name:", patient["Name"])
            print("Age:", patient["Age"])
            print("Gender:", patient["Gender"])
            print("Disease:", patient["Disease"])
            break
    if not found:
        print("Patient not found.")
def update_patient_by_id(patient_id):
    found = False
    for patient in hospital_records:
        if patient["ID"] == patient_id:
            print("Current Details:")
            print("Patient ID:", patient["ID"])
            print("Name:", patient["Name"])
            print("Age:", patient["Age"])
            print("Gender:", patient["Gender"])
            print("Disease:", patient["Disease"])
            print("\n")
            name = input("Enter updated name (leave blank to keep current value): ")
            age = input("Enter updated age (leave blank to keep current value): ")
            gender = input("Enter updated gender (leave blank to keep current value): ")
            disease = input("Enter updated disease (leave blank to keep current value): ")
            if name:
                patient["Name"] = name
            if age:
                patient["Age"] = age
            if gender:
                patient["Gender"] = gender
            if disease:
                patient["Disease"] = disease
            found = True
            print("Patient with ID", patient_id, "updated successfully.")
            break
    if not found:
        print("Patient not found. Update failed.")
def main():
    while True:
        print("Hospital Management System")
        print("1. Add Patient Details")
        print("2. Search for a Patient by ID")
        print("3. Update Patient Details by ID")
        print("4. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            add_patient_details()
        elif choice == '2':
            patient_id = input("Enter patient ID to search: ")
            search_patient_by_id(patient_id)
        elif choice == '3':
            patient_id = input("Enter patient ID to update: ")
            update_patient_by_id(patient_id)
        elif choice == '4':
            break
        else:
            print("Invalid choice. Please try again.")

if __name__== "__main__":
    main()