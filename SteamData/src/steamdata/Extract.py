#Developed by Anthony Villalobos 9/23/2026
#Extract class for ETL program
import pandas as pd
from loguru import logger
from pathlib import Path

#class Extract:

class Extract:

    def path_obtain(self):
        """
        Obtains the path to the CSV file containing Steam games data.
        """
        # Use pathlib to construct the path to the CSV file

        #parente path
        parent_path = Path(__file__).resolve().parents[3] #go back to main path
        csv_path = parent_path / "SteamGamesData" / "games.csv"  # Adjust the path as needed
        #print(f"CSV path: {csv_path}")  # Debugging statement to check the path
        if not csv_path.exists():
            logger.error(f"The CSV file at {csv_path} does not exist. Please check the file path and try again.")
            return None
        return csv_path

    def read_csv(self):
        """
        Reads the CSV file containing Steam games data and returns a DataFrame.
        """

        csv = self.path_obtain()
        #todo: use pathlib to make this more robust and cross-platform
        try:
            df = pd.read_csv(csv)
            print("CSV FILE FROM READ_CSV FUNCTION: ", df.head())  # Debugging statement to check the DataFrame
            if df.empty:
                logger.error("The CSV file is empty. Please check the file and try again.")
                return None
            return df
        except FileNotFoundError:
            logger.error("The CSV file wasn't found. Please check the file path and try again.")
            return None
        except Exception as e:
            logger.error(f"An error occurred while reading the CSV file: {e}")
            return None
