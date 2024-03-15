import os
import pandas as pd
from textblob import TextBlob
import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.probability import FreqDist
from nltk import pos_tag
from textblob import TextBlob
from textblob import Word

# Download NLTK resources
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('averaged_perceptron_tagger')

# Specify the folder containing text files
folder_path = "d:\pythonProject\jobproject"

# Get a list of all text files in the folder
text_files = [file for file in os.listdir(folder_path) if file.endswith(".txt")]

# Initialize output dataframe
output_df = pd.DataFrame(columns=["FileName"] + ["POSITIVE SCORE", "NEGATIVE SCORE", "POLARITY SCORE", "SUBJECTIVITY SCORE",
                                                 "AVG SENTENCE LENGTH", "PERCENTAGE OF COMPLEX WORDS", "FOG INDEX",
                                                 "AVG NUMBER OF WORDS PER SENTENCE", "COMPLEX WORD COUNT", "WORD COUNT",
                                                 "SYLLABLE PER WORD", "PERSONAL PRONOUNS", "AVG WORD LENGTH"])

# Text analysis function
def analyze_text(text):
    blob = TextBlob(text)
    words = word_tokenize(text)
    print(blob)
    print(words)

    # Perform text analysis as before
    # ...

# Iterate through each text file
# for text_file in text_files:
#     file_path = os.path.join(folder_path, text_file)

#     # Read the content of the text file
#     with open(file_path, 'r', encoding='utf-8') as file:
#         text_content = file.read()
# Iterate through each text file
for text_file in text_files:
    file_path = os.path.join(folder_path, text_file)

    try:
        # Read the content of the text file
        with open(file_path, 'r', encoding='utf-8') as file:
            text_content = file.read()

        # Analyze the text
        analysis_result = analyze_text(text_content)

        # Append results to output dataframe
        output_df = output_df.append({"FileName": text_file, **{output_df.columns[i + 1]: analysis_result[i] for i in range(len(output_df.columns) - 1)}}, ignore_index=True)

    except Exception as e:
        print(f"Error processing {text_file}: {e}")


    # Analyze the text
    analysis_result = analyze_text(text_content)

    # Append results to output dataframe
    output_df = output_df._append({"FileName": text_file, **{output_df.columns[i + 1]: analysis_result[i] for i in range(len(output_df.columns) - 1)}}, ignore_index=True)

# Save the output dataframe to Excel
output_df.to_excel("Output.xlsx", index=False)
