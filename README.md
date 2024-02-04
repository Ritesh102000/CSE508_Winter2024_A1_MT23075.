# CSE508_Winter2024_A1_MT23075.
# Tokenization Script

This Python script performs tokenization on text files using the spaCy library. It includes the following preprocessing steps:

1. Lowercasing the text.
2. Tokenization using spaCy.
3. Removing stopwords, punctuation, and blank space tokens.

## Usage

1. Clone or download this repository.

2. Install the required dependencies:

    ```bash
    pip install spacy
    ```

3. Download the spaCy English language model:

    ```bash
    python -m spacy download en_core_web_sm
    ```

4. Create a folder named `text_files` and place your text files (e.g., file1.txt, file2.txt, ...) in it.

5. Run the script by executing:

    ```bash
    python tokenization_script.py
    ```

    Follow the on-screen prompts to enter the names of the files you want to process.

6. The processed output will be stored in the `output` folder.

## Notes

- The script tokenizes text files, removing stopwords, punctuation, and blank space tokens.
- Make sure to provide valid filenames and ensure the presence of the `text_files` and `output` folders.



