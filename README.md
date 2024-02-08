# CSE508_Winter2024_A1_MT23075.

# Text Processing and Information Retrieval

## Introduction
This repository contains Python scripts for text processing and information retrieval tasks. It includes functionalities for tokenization, building inverted indexes, executing Boolean queries, building positional indexes, and retrieving documents based on proximity of query terms.

## Sections

### Section 1: Tokenization and Saving Tokenized Data to Files
This section tokenizes the content of text files, removes punctuation and stop words, and saves the tokenized data to output files.

- `tokenization(x)`: Tokenizes the content of a text file.
  - Parameters:
    - `x`: The filename (without the .txt extension).
  - Returns:
    - `tokens`: List of tokens extracted from the text file.

- `main()`: Handles user input for the number of queries and individual queries, tokenizes the query terms and operations, builds an inverted index from tokenized files, saves the inverted index to a file, loads the inverted index from the file, executes Boolean queries using the inverted index, and displays query results.

### Section 2: Building an Inverted Index and Executing Boolean Queries
This section builds an inverted index from tokenized documents and executes Boolean queries using the index.

- `inv_index()`: Builds an inverted index from tokenized documents.
  - Returns:
    - The inverted index.

- `save_index(index, filename='inverted_index.pkl')`: Saves the inverted index to a pickle file.
  - Parameters:
    - `index`: The inverted index to be saved.
    - `filename`: The filename for the pickle file (default: 'inverted_index.pkl').

- `load_index(filename='inverted_index.pkl')`: Loads the inverted index from a pickle file.
  - Parameters:
    - `filename`: The filename of the pickle file (default: 'inverted_index.pkl').
  - Returns:
    - The loaded inverted index.

- `execute_query(query, inverted_index)`: Executes Boolean queries using the inverted index.
  - Parameters:
    - `query`: The Boolean query.
    - `inverted_index`: The inverted index.
  - Returns:
    - `results`: Set of documents retrieved for the query.

### Section 3: Building a Positional Index and Retrieving Documents
This section builds a positional index from tokenized documents and retrieves documents based on the proximity of query terms.

- `positional_index()`: Builds a positional index from tokenized documents.
  - Returns:
    - The positional index.

- `save_positional_index(index, filename)`: Saves the positional index to a pickle file.
  - Parameters:
    - `index`: The positional index to be saved.
    - `filename`: The filename for the pickle file.

- `load_positional_index(filename)`: Loads the positional index from a pickle file.
  - Parameters:
    - `filename`: The filename of the pickle file.
  - Returns:
    - The loaded positional index.

- `retrieve_documents(query, index)`: Retrieves documents based on the proximity of query terms.
  - Parameters:
    - `query`: The query string.
    - `index`: The positional index.
  - Returns:
    - `relevant_documents`: Set of relevant documents.

## Additional Comments
- The code follows a modular design, with functions encapsulating specific tasks.
- Error handling is present for file operations and user input.
- External libraries such as Spacy are utilized for natural language processing tasks.
- Both inverted and positional indexes are employed for efficient document retrieval based on different criteria.
- Further optimization and enhancement can be applied for specific use cases, such as improving the efficiency of query execution and index building.
