# FinTech Loan Modeling

This project demonstrates a data pipeline for creditworthiness assessment using PostgreSQL, Docker, and Python. The pipeline includes data ingestion, storage in a PostgreSQL database, and data export to CSV files for further analysis.

## Table of Contents

1. [Overview](#overview)
2. [Applications and Tools Used](#applications-and-tools-used)
3. [Project Structure](#project-structure)
4. Setup Instructions
   - [Prerequisites](#prerequisites)
   - [Step 1: Clone the Repository](#step-1-clone-the-repository)
   - [Step 2: Set Up the Project Directory](#step-2-set-up-the-project-directory)
   - [Step 3: Build and Run the Docker Containers](#step-3-build-and-run-the-docker-containers)
5. [Step-by-Step Instructions how to access the Data in PostgreSQL and export it](#Step-by-Step-Instructions-how-to-access-the-Data-in-PostgreSQL-and-export-it)
6. [Additional Information](#additional-information)

## Overview

This project sets up a data pipeline to:

- Download CSV files from Kaggle.
- Ingest data from CSV files.
- Store the data in a PostgreSQL database.
- Export the data back to CSV files for further analysis.

The project is containerized using Docker, allowing for easy setup and deployment.

## Applications and Tools Used

- **Python**: For data ingestion and processing.
- **PostgreSQL**: For storing the data.
- **Docker**: For containerizing the application and database.
- **Visual Studio Code (VSC)**: For development and viewing data.

## Project Structure

```
kmicku-DE2v2.3.5/
│
├── data/                          # Directory to store downloaded CSV files
│   ├── loan-test.csv
│   ├── loan-train.csv
│
├── Exported_information/          # Directory to store exported CSV files
│   ├── exported-loan-test.csv
│   ├── exported-loan-train.csv
│
├── .gitignore                     # Git ignore file to exclude unnecessary files                    
├── data_pipeline.py               # Main Python script for data pipeline
├── docker-compose.yml             # Docker Compose file to define multi-container applications
├── Dockerfile                     # Dockerfile to build the application container
├── kaggle.json                    # Kaggle API token (add to .gitignore to avoid exposing it)
├── README.md                      # Project documentation file
├── requirements.txt               # Python dependencies file
└── wait.sh         
```

## Setup Instructions

### Prerequisites

- **Docker**: Install Docker from Docker's official site.
  Follow the installation instructions provided on the site for your operating system. Install from [here](https://www.docker.com/).
- **Visual Studio Code (VSC)**: Recommended for development and viewing data. Install from [here](https://code.visualstudio.com/).
-  **Kaggle Account**: Create a Kaggle account and generate an API token. You can create an account [here](https://www.kaggle.com/).
- **Kaggle API Token**: Download the `kaggle.json` file and place it in the project directory.
- Download two CSV files from this Kaggle [repository](https://www.kaggle.com/datasets/vikasukani/loan-eligible-dataset/).
- Writes the data to the database into train and test tables.

### Step-by-Step Instructions for Setting Up Kaggle API

1. **Install Kaggle API**: Ensure that the Kaggle API is installed in your Docker container.
2. **Create Kaggle API Token**: Obtain your Kaggle API token and set it up in the Docker container. Starting from the website [here](https://www.kaggle.com/).
- Press on the top right corner round icon of the browser
  
   ![image](https://github.com/TuringCollegeSubmissions/kmicku-DE2v2.3.5/assets/40234505/f3e10596-6120-4420-bb74-041bdaf6b881)
- Press 'Settings'
  
   ![image](https://github.com/TuringCollegeSubmissions/kmicku-DE2v2.3.5/assets/40234505/8e362d1f-73b8-4f9d-a89c-f2514295a346)
- Press 'Create New Token'
  
   ![image](https://github.com/TuringCollegeSubmissions/kmicku-DE2v2.3.5/assets/40234505/949a3733-dfde-4271-9673-c9affa4bc695)
- Press 'Continue'
  
   ![image](https://github.com/TuringCollegeSubmissions/kmicku-DE2v2.3.5/assets/40234505/8d27947e-bdf5-47a9-ad05-f2e964b3a4fd)
- Place the downloaded .json file into the root directory of the project. The file structure should look something like this
  
```
  {"username":"johnhudson","key":"fafklaf155156nofna15148fnf"}
```

3. **Configure `.gitignore`**: For safety reasons, ensure that `.gitignore` excludes `.json` files to protect sensitive information.

### Step 1: Clone the Repository

Clone this repository to your local machine:

```
git clone https://github.com/TuringCollegeSubmissions/kmicku-DE2v2.3.5.git
cd location-of-your-project
```

### Step 2: Set Up the Project Directory

Ensure your project directory structure matches the above [Project Structure](#project-structure).

### Step 3: Build and Run the Docker Containers

Build and run the Docker containers:

```
docker-compose up --build
```

This command will:

- Build the Docker images.
- Start the PostgreSQL database container.
- Start the application container and run the data ingestion script.

### Step 4: Verify the Data in PostgreSQL

Access the PostgreSQL container and verify the data:

```
docker-compose exec db psql -U user -d credit_db
```

In the PostgreSQL interactive terminal, run:

```
\dt
SELECT * FROM train LIMIT 10;
SELECT * FROM test LIMIT 10;
\q
```

### Step 5: Export Data to CSV Files

To export data to CSV files in the `Exported information` directory:

1. Ensure the directory exists on your host machine.
2. Run the following commands in the PostgreSQL interactive terminal:

```
\copy train TO '/exported/loan-train.csv' CSV HEADER;
\copy test TO '/exported/loan-test.csv' CSV HEADER;
```

## Viewing Exported Data

To view the exported CSV files in Visual Studio Code:

1. Install the Excel Viewer or Rainbow CSV extension.
2. Open the `Exported information` directory in VSC.
3. Click on the CSV files to view them.

## Summary
- Ensure Docker Desktop is installed and running.
- Follow the updated README.md instructions.
- Verify the project structure matches the provided layout.
- Build and run the Docker containers using Docker Compose.
- Verify the data in the PostgreSQL database.
- Export data to CSV files as needed.

### Step-by-Step Instructions how to access the Data in PostgreSQL and export it

1. **Stop the Current `docker-compose` Process:** If you see the message "Data successfully written to the database!" and are you are stuck in the attached mode:

   - Press `Ctrl+C` to stop the `docker-compose up` process.

   **Restart Docker Compose in Detached Mode:** This will start the services in the background, allowing you to interact with the containers without the logs blocking your terminal. So you can continue with the command

   ```
   docker-compose up -d
   ```

2. **Access the PostgreSQL database container**: Use the following command to connect to the PostgreSQL database container.

   ```
   docker-compose exec db psql -U user -d credit_db
   ```

3. **Check the tables in the database**: Once inside the PostgreSQL interactive terminal, list all the tables to ensure that the data has been written successfully.

   ```
   \dt
   ```

   This command will display the list of tables in the `credit_db` database.

4. **View the data in the tables**: To verify the contents of the `train` and `test` tables, use the following SQL queries:

   ```
   SELECT * FROM train LIMIT 10;
   ```

   ```
   SELECT * FROM test LIMIT 10;
   ```

   This will display the first 10 rows from each table.

5. **Export data to CSV files**: After verifying the data, you can export the contents of the tables to CSV files located in the `Exported_information` directory.

   ```
   \copy train TO '/exported/loan-train.csv' CSV HEADER;
   ```

   ```
   \copy test TO '/exported/loan-test.csv' CSV HEADER;
   ```

6. **Exit the PostgreSQL interactive terminal**: Once you have exported the data, exit the PostgreSQL terminal by typing:

   ```
   \q
   ```

7. **Verify the exported CSV files**: The exported CSV files (`loan-train.csv` and `loan-test.csv`) should now be available in the `Exported_information` directory on your host machine. You can open and view these files using a text editor or any application that supports CSV file format, such as Visual Studio Code with the Excel Viewer or Rainbow CSV extension.

## Additional Information

- **Docker Compose**: Used to define and manage multi-container Docker applications.
- **PostgreSQL**: A powerful, open-source object-relational database system used.
- **Python Libraries**: `pandas` for data manipulation, `sqlalchemy` for database interaction.

## Author
- Karolis Mickus 2024
