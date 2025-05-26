#Madhav Parappuveettil
#Spending Tracker keeps track of daily spending



import csv
import os
from datetime import datetime

#I need this to read from my current expenses file and write the correct expenses to the correct category


CSV_FILE = 'spending.csv'

# Check if the CSV file exists, if not, create it with headers
def initialize_csv():
    if not os.path.exists(CSV_FILE):
        with open(CSV_FILE, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Date', 'Category', 'Description', 'Amount'])

def add_spending(date, category, description, amount):
    with open(CSV_FILE, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([date, category, description, amount])

def main():
    print('--- Spending Tracker ---')
    initialize_csv()
    while True:
        date = input('Enter date (YYYY-MM-DD) [leave blank for today]: ')
        if not date:
            date = datetime.today().strftime('%Y-%m-%d')
        category = input('Enter category (e.g., Food, Transport): ')
        description = input('Enter description: ')
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
