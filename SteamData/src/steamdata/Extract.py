#Developed by Anthony Villalobos 9/23/2026
#Extract class for ETL program
import pandas as pd
from loguru import logger

#class Extract:

class Extract:

    def read_csv(self):
        """
        Reads the CSV file containing Steam games data and returns a DataFrame.
        """
        #todo: use pathlib to make this more robust and cross-platform
        try:
            df = pd.read_csv('SteamGamesData/games.csv')
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
