#!/bin/bash

# Check if a directory is provided as an argument
if [ $# -ne 1 ]; then
    echo "Usage: $0 <directory_path>"
    exit 1
fi

# Store the provided directory path
DIR_PATH="$1"

# Check if the provided path is a directory
if [ ! -d "$DIR_PATH" ]; then
    echo "Error: '$DIR_PATH' is not a directory."
    exit 1
fi

# Count the number of PDF files in the directory
PDF_COUNT=$(find "$DIR_PATH" -type f -name "*.pdf" | wc -l)

if [ "$PDF_COUNT" -eq 0 ]; then
    echo "No PDF files found in '$DIR_PATH'."
    exit 0
fi

echo "Found $PDF_COUNT PDF files in '$DIR_PATH'. Processing..."

# Process each PDF file in the directory
find "$DIR_PATH" -type f -name "*.pdf" | while read -r pdf_file; do
    echo "Processing: $pdf_file"
    python3 extract_pdf.py "$pdf_file"
done

echo "All PDF files processed successfully." 