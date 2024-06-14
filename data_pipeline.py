import os
import time
import logging
import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.exc import OperationalError
from kaggle.api.kaggle_api_extended import KaggleApi
from dotenv import load_dotenv
from pathlib import Path


# Load environment variables from .env file
load_dotenv()

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


# Define function to download dataset from Kaggle
def download_kaggle_dataset():
    api = KaggleApi()
    api.authenticate()

    # Specify the dataset URL
    dataset = 'vikasukani/loan-eligible-dataset'
    download_path = Path('./data')
    
    # Download the dataset
    api.dataset_download_files(dataset, path=download_path, unzip=True)


# Ensure the data directory exists
data_dir = Path('./data')
data_dir.mkdir(parents=True, exist_ok=True)

# Download the CSV files
download_kaggle_dataset()

# Define file paths
train_path = data_dir / 'loan-train.csv'
test_path = data_dir / 'loan-test.csv'

# Check if files are downloaded
if not train_path.is_file() or not test_path.is_file():
    raise FileNotFoundError("The required CSV files were not found in the data directory after download.")

# Load CSV files
train_df = pd.read_csv(train_path)
test_df = pd.read_csv(test_path)

# Database connection
db_url = os.getenv('DATABASE_URL')
if not db_url:
    raise EnvironmentError("DATABASE_URL environment variable is not set")

engine = create_engine(db_url)

# Retry mechanism to wait for the database to be ready
retry_count = 5
retry_wait = 10  # seconds

for i in range(retry_count):
    try:
        # Attempt to connect to the database
        conn = engine.connect()
        conn.close()
        logger.info("Database connection successful!")
        break
    except OperationalError:
        logger.warning(f"Database not ready, retrying in {retry_wait} seconds...")
        time.sleep(retry_wait)
else:
    raise Exception("Could not connect to the database after several attempts.")

# Write data to database
train_df.to_sql('train', engine, if_exists='replace', index=False)
test_df.to_sql('test', engine, if_exists='replace', index=False)

logger.info("Data successfully written to the database!")
