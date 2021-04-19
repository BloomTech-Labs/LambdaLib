from LambdaLib.Analysis.csv_similarity import csv_similarity_score


notes = """
Data Analysis Examples
- csv similarity score example
"""

# File Paths
true_data = "data/csv_true.csv"
test_data = "data/csv_test.csv"

# Calculates Similarity
average_score = csv_similarity_score(
    true_data,
    test_data,
)

# Output
print(notes)
print(f"Average Similarity Score: {100 * average_score:.2f}%")
