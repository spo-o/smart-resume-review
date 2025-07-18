# Import modules:
# 1. CVsReader from the OCR_Reader module which is used for reading CVs
# 2. CVsInfoExtractor from the ChatGPT_Pipeline module which is used for extracting specific information from the CVs
from OCR_Reader import CVsReader
from ChatGPT_Pipeline import CVsInfoExtractor
import sys
from datetime import datetime
import csv
import os

# Fetching command line arguments
cvs_directory_path_arg, openai_api_key_arg, desired_positions_arg = sys.argv[1], sys.argv[2], sys.argv[3].split(",")

# Splitting the desired positions into a list and removing any leading or trailing whitespace
desired_positions = [position.strip() for position in desired_positions_arg]


# Create an instance of CVsReader. 
# The cvs_directory_path argument, which represents the directory where the CV files are located.
cvs_reader = CVsReader(cvs_directory_path = cvs_directory_path_arg)

# Use the read_cv method of the CVsReader instance to read all CVs in the specified directory.
# The result is a dataframe where each row corresponds to a different CV's file name and content.
cvs_content_df = cvs_reader.read_cv()

# Create an instance of CVsInfoExtractor.
# It takes as an argument the dataframe returned by the read_cv method of the CVsReader instance and the desired positions in a list.
cvs_info_extractor = CVsInfoExtractor(cvs_df = cvs_content_df, openai_api_key = openai_api_key_arg, desired_positions = desired_positions)

# Use the extract_cv_info method of the CVsInfoExtractor instance to extract the desired information from the CVs.
# This method presumably returns a list of dataframes, each dataframe corresponding to the extracted information from each CV.
extract_cv_info_dfs = cvs_info_extractor.extract_cv_info()
# Get Job Description from user input
print("\n--- Job Description Keyword Gap Analysis ---")
print("Paste the job description below (press Enter twice to finish):")

jd_lines = []
while True:
    line = input()
    if line == "":
        break
    jd_lines.append(line)
job_description_text = " ".join(jd_lines)

print("\n==== Summary ====")
print(f"Total CVs Processed: {len(cvs_content_df)}")
print(f"Job Description Keywords: {len(job_description_text.split())} words")



os.makedirs("output", exist_ok=True)
csv_path = "output/keyword_analysis.csv"

with open(csv_path, "w", newline="") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(["Filename", "Common Keywords", "Missing Keywords"])

    for index, row in cvs_content_df.iterrows():
        filename = row['Filename']
        results = compare_keywords(row['CV_Text'], job_description_text)
        writer.writerow([
            filename,
            ", ".join(results['common_keywords']),
            ", ".join(results['missing_keywords'])
        ])
print(f"Keyword analysis saved to {csv_path}")
# Optional: export to JSON if --json flag is passed
if "--json" in sys.argv:
    output_json = []
    for index, row in cvs_content_df.iterrows():
        results = compare_keywords(row['CV_Text'], job_description_text)
        output_json.append({
            "filename": row['Filename'],
            "common_keywords": results['common_keywords'],
            "missing_keywords": results['missing_keywords']
        })

    with open("output/keyword_analysis.json", "w") as json_file:
        import json
        json.dump(output_json, json_file, indent=2)

    print(" Keyword analysis also saved to output/keyword_analysis.json")


with open("logs/keyword_gap_log.txt", "a") as f:
    f.write(f"\n--- {datetime.now()} ---\n")
    f.write(f"Resume: {filename}\n")
    f.write(f"Common: {results['common_keywords']}\n")
    f.write(f"Missing: {results['missing_keywords']}\n")
