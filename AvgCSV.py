import csv

def main():
    # Load the data from the CSV file
    file_name = 'myfile4.csv'
    data = []
    
    with open(file_name, mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(row)

    # Display the full dataset
    print("\nFull Dataset:")
    print(f"{'Day':<10} {'Temp':<10} {'Noise':<10}")
    for row in data:
        print(f"{row['Day']:<10} {row['Temp']:<10} {row['Noise']:<10}")

    # Extract "Temp" and "Noise" columns
    temp_values = [float(row['Temp']) for row in data]
    noise_values = [float(row['Noise']) for row in data]

    # Calculate statistics
    avg_temp = round(sum(temp_values) / len(temp_values), 2)
    avg_noise = round(sum(noise_values) / len(noise_values), 2)

    # Display the results
    print("\nStatistics:")
    print(f"Average Temperature: {avg_temp}°C")
    print(f"Average Noise Level: {avg_noise} dB")

if __name__ == "__main__":
    main()
