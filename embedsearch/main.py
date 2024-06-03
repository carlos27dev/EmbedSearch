import os
import textwrap
import pandas as pd
from dotenv import load_dotenv
from embedsearch.embeddings.embedding_generator import EmbeddingGenerator
from embedsearch.utils.utils import Utils

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
    print("\nChecking documents directory exists.")
    Utils.check_files_path(files_path)
    print("Documents directory found.")

    # Process the files and extract text
    print("\nExtracting text...")
    paragraphs = Utils.process_files(files_path)
    print("Text extracted.")

    # Create an instance of the embedding generator with the API key
    print("\nGenerating an Embedding Engine...")
    generator = EmbeddingGenerator(api_key)
    print("Embedder generated.")

    # Generate and save the embeddings in a FAISS index
    print("\nGenerating and saving embeddings...")
    faiss_index = Utils.generate_and_save_embeddings(generator, paragraphs, faiss_index_path)
    print("Embeddings saved succesfully to FAISS index.")

    print(f"FAISS index saved to {faiss_index_path}")

    # Perform the search query on the FAISS index
    print("\nSearching your query...")
    results = Utils.search_query(query, generator, faiss_index, paragraphs, k)
    print("Search completed.")

    # Format the search results into a pandas DataFrame
    results_df = pd.DataFrame(results, columns=['Paragraph', 'Distance'])

    # Display the search results
    print("\nSearch results:")
    print(f"Query:'{query}'\nNearest neighbors:")
    for i, row in results_df.iterrows():
        paragraph = textwrap.fill(row['Paragraph'], width=80)
        print(f"\nParagraph:\n{paragraph}")
        print(f"Distance: {row['Distance']}")

if __name__ == '__main__':
    main()
