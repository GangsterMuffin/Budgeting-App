#Madhav Parappuveettil
#Spending Tracker keeps track of daily spending



import csv
import os
from datetime import datetime

# Set the CSV file path to the saves directory
CSV_FILE = os.path.join('saves', 'spending.csv')

# Ensure the saves directory exists
if not os.path.exists('saves'):
    os.makedirs('saves')

# I need this to read from my current expenses file and write the correct expenses to the correct category


# Check if the CSV file exists, if not, create it with headers
def load_from_csv():
    if not os.path.exists(CSV_FILE):
        print("Can't find spending.csv, creating a new one.")
        with open(CSV_FILE, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Date', 'Category', 'Description', 'Amount'])

def add_spending(date, category, description, amount):
    with open(CSV_FILE, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([date, category, description, amount])

def main():
    print('--- Spending Tracker ---')
    load_from_csv()
    while True:
        date = datetime.today().strftime('%Y-%m-%d')
        description = input('Enter description: ')
        category = input('Enter category (e.g., Food, Transport): ') #category can implement a dropdown later. It can also automatically detect categories from description
        amount = input('Enter amount: ')
        try:
            amount = float(amount)
        except ValueError:
            print('Invalid amount. Please enter a number.')
            continue
        add_spending(date, category, description, amount)
        print('Spending recorded!')
        cont = input('Add another? (y/n): ').strip().lower()
        if cont != 'y':
            break
    print('All done! Your spending has been saved to spending.csv.')

if __name__ == '__main__':
    main()