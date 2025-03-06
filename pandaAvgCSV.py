import csv
import pandas
import statistics

# Read the entire CSV file into a pandas DataFrame
df = pandas.read_csv('myfile4.csv')
print("df to string")
print(df.to_string())

# Filter out the column, value_eur
temp_values = df['Temp']
print("temp values",type(temp_values),temp_values)
mean_value_temp = round(statistics.mean(temp_values), 2)
print("Mean Value Temp:", mean_value_temp)
noise_values = df['Noise']
mean_value_noise = round(statistics.mean(noise_values), 2)
print("Mean Value Noise:", mean_value_noise)
"""
with open('myfile4.csv', 'r') as file:
    # Create a CSV reader object
    csv_reader = csv.reader(file)
    # Iterate over each row in the CSV file
    print("Printing rows")
    num1 = 0
    for row in csv_reader:
        # Print the value of the cell at index 2 (3rd cell in the row)
        print(row[0],row[1])
        #num1 = num1 + float(row[0])
    """    
