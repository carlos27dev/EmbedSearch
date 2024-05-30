import os
import pandas as pd
from dotenv import load_dotenv
from embedsearch.embeddings.embedding_generator import EmbeddingGenerator
from embedsearch.utils.utils import FileUtils

# Load environment variables from the .env file
load_dotenv()
api_key = os.getenv('COHERE_API_KEY')


def main():
    """
    Main entry point for the program.
    """
    # Query to perform
    query = input("Please enter your query: (E.g.: How COVID affects this plan?): ")

    # Directory path containing the files to be processed
    files_path = 'data/sample'

    # Path where the FAISS index (vector database) will be saved
    faiss_index_path = 'results/faiss_index.bin'

    # Number of results to display (number of nearest neighbors to search for)
    k = 5

    # Check if the files directory exists
    FileUtils.check_files_path(files_path)

    # Process the files and extract text
    paragraphs = FileUtils.process_files(files_path)

    # Create an instance of the embedding generator with the API key
    generator = EmbeddingGenerator(api_key)

    # Generate and save the embeddings in a FAISS index
    faiss_index = FileUtils.generate_and_save_embeddings(generator, paragraphs, faiss_index_path)

    print(f"\nFAISS index saved to {faiss_index_path}")

    # Perform the search query on the FAISS index
    results = FileUtils.search_query(query, generator, faiss_index, paragraphs, k)

    # Format the search results into a pandas DataFrame
    results_df = pd.DataFrame(results, columns=['Paragraph', 'Distance'])

    # Display the search results
    print("\nSearch results:")
    print(f"Query:'{query}'\nNearest neighbors:")
    print(results_df)


if __name__ == '__main__':
    main()
