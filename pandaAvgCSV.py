import pandas as pd

def main():
    # Load the data from the CSV file
    file_name = 'myfile4.csv'
    data = pd.read_csv(file_name)

    # Display the full dataset
    print("\nFull Dataset:")
    print(data)

    # Extract "Temp" and "Noise" columns
    temp_values = data['Temp']
    noise_values = data['Noise']

    # Calculate statistics
    avg_temp = round(temp_values.mean(), 2)
    avg_noise = round(noise_values.mean(), 2)

    # Display the results
    print("\nStatistics:")
    print("Average Temperature:", avg_temp)
    print("Average Noise Level:", avg_noise)

if __name__ == "__main__":
    main()
