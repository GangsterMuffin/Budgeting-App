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
        # Create the CSV file with headers
        with open(CSV_FILE, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Date', 'Category', 'Description', 'Amount']) #is the the most optimal way to store the data?

def add_spending(date, category, description, amount):
    with open(CSV_FILE, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([date, category, description, amount])

def export_groceries_monthly_summary():
    import calendar
    from collections import defaultdict
    
    # Get current year and month
    today = datetime.today()
    year = today.year
    month = today.month
    num_days = calendar.monthrange(year, month)[1]
    
    # Prepare a dict for daily totals
    daily_totals = defaultdict(float)
    
    # Read spending.csv
    with open(CSV_FILE, mode='r', newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['Category'].lower() == 'groceries':
                row_date = datetime.strptime(row['Date'], '%Y-%m-%d')
                if row_date.year == year and row_date.month == month:
                    day = row_date.day
                    daily_totals[day] += float(row['Amount'])
    
    # Prepare header and row
    header = ['Category'] + [str(day) for day in range(1, num_days+1)]
    groceries_row = ['Groceries'] + [str(daily_totals[day]) if day in daily_totals else '0' for day in range(1, num_days+1)]
    
    # Write to summary CSV
    summary_file = os.path.join('saves', f'groceries_summary_{year}_{month:02d}.csv')
    with open(summary_file, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(header)
        writer.writerow(groceries_row)
    print(f'Groceries monthly summary exported to {summary_file}')

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