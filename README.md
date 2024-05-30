# EmbedSearch Project

This project is a demonstration of how to extract text from files, generate embeddings using Co:here, and perform semantic searches using a FAISS index.

## Description

The project allows users to upload files (PDF, DOCX, TXT), extract their content, generate embeddings for each paragraph using the Co:here API, and perform semantic queries within the content using FAISS.

## Installation

1. Clone the repository:
    ```sh
   git clone https://github.com/carlos27dev/EmbedSearch
   cd EmbeddingsProject
    ```

2. Create and activate a virtual environment:
    ```sh
    python3 -m venv venv
    source venv/bin/activate
    ```

3. Install the dependencies:
    ```sh
    pip install -r requirements.txt
    ```

4. Install the dependencies:
    - Create a .env file in the root of the project with your Co:here API key.
    ```env
    COHERE_API_KEY=your_api_key
    ```

## Usage

1. Place the files you want to process in the data/sample directory.
2. Run the main script:
    ```sh
    python main.py
    ```
3. The program will prompt you to enter your query:
   ```sh
    Please enter your query: (E.g.: How COVID affects this plan?):  
    ```
4. The results will be displayed in the console.

## Author

- **Carlos Arriaga** - [carlos27dev](https://github.com/carlos27dev)
