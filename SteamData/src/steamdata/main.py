

from steamdata import Extract


def main():
    extract = Extract.Extract()
    df = extract.read_csv()
    if df is not None:
        print("CSV file read successfully.")
        print(df.head())  # Display the first few rows of the DataFrame
    else:
        print("Failed to read the CSV file.")

if __name__ == "__main__":
    main()