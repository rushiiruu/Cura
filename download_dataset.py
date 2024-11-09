import csv

def load_medicine_data(csv_file):
    medicines = []
    with open(csv_file, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            medicines.append(row)
    return medicines

def search_medicine(medicine_name, medicines):
    results = [med for med in medicines if medicine_name.lower() in med['Medicine Name'].lower()]
    return results

# Example usage
if __name__ == "__main__":
    csv_file = 'Medicine_Details.csv'  # Replace with your file path

    # Load the medicines from the CSV file
    medicines = load_medicine_data(csv_file)

    # Input from user to search for a medicine
    user_input = input("Enter the name of the medicine to search: ")
    
    # Search for the medicine
    results = search_medicine(user_input, medicines)

    # Display results
    if results:
        for med in results:
            print(f"\nName: {med['Medicine Name']}")
            print(f"Composition: {med['Composition']}")
            print(f"Uses: {med['Uses']}")
            print(f"Side Effects: {med['Side_effects']}")
            print(f"Image URL: {med['Image URL']}")
    else:
        print("Medicine not found.")
