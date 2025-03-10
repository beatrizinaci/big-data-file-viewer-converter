# Big Data File Converter

## Overview
The Big Data File Converter is a **Streamlit-based** application that allows users to upload and preview and export data in various formats, including CSV, ORC, Parquet and JSON. The application provides options to customize the file readinf process, sucj as specifying headers and delimiters for CSV files.

You can access the app [here](https://big-data-file-converter.streamlit.app/).

## Features
- Supports multiple file formats: CSV, ORC, Parquet, JSON
- Customizable options for CSV files (header and delimiter)
- Displays the content of the uploaded files in a user-friendly format
- User can export data as csv

## Instalation
To run the Big Data File Converter locally, follow these steps:

1. Clone the repository:
    ```sh
    git clone https://github.com/beatrizinaci/big-data-file-viewer-converter.git
    cd big-data-file-viewer-converter
    ```

2. Create a virtual environment and activate it:
    ```sh
    python3 -m venv venv
    source venv/bin/activate
    ```

3. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```
### Running the application
To start the application, run the following command:
```sh
streamlit run src/app.py
```

## Usage

1. Upload one or more files via the interface.
2. Select applicable options (e.g., delimiter for CSV files).
3. Preview the data directly in the app.
4. Export data as CSV 

## Future improvements 

1. Add button to export to different file formats