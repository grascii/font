#!/bin/bash

# increment_glyphs_dynamic.sh
# Usage: ./increment_glyphs_dynamic.sh <directory> <min_value> <increment_amount>
# Example: ./increment_glyphs_dynamic.sh ./glyphs 100 50

# 1. Argument Validation
if [ "$#" -ne 3 ]; then
    echo "Error: Exactly 3 arguments required."
    echo "Usage: $0 <directory> <min_value> <increment_amount>"
    exit 1
fi

DIR_PATH="$1"
MIN_VALUE="$2"
INCREMENT="$3"

# Validate inputs are positive integers
if ! [[ "$MIN_VALUE" =~ ^[0-9]+$ ]] || ! [[ "$INCREMENT" =~ ^[0-9]+$ ]]; then
    echo "Error: <min_value> and <increment_amount> must be positive integers."
    exit 1
fi

# Check if directory exists
if [ ! -d "$DIR_PATH" ]; then
    echo "Error: Directory '$DIR_PATH' does not exist."
    exit 1
fi

# 2. Process each .glyph file
find "$DIR_PATH" -maxdepth 1 -type f -name "*.glyph" | while read -r file; do
    # Skip empty files
    [ ! -s "$file" ] && continue

    # Use awk to process the file
    # - It looks for lines matching "Encoding: <num> <num> <num>"
    # - If the first number > MIN_VALUE, it increments it
    # - It prints the modified line or the original line
    awk -v min="$MIN_VALUE" -v inc="$INCREMENT" '
    # Match lines starting with "Encoding: " followed by three numbers
    /^Encoding: [0-9]+ -?[0-9]+ [0-9]+/ {
        # Split the line into fields
        # $1="Encoding:", $2=num1, $3=num2, $4=num4

        if ($2 >= min) {
            # Increment the first number ($2)
            $2 = $2 + inc
            # Reconstruct the line exactly as "Encoding: <new> <old> <old>"
            print "Encoding: " $2 " " $3 " " $4
            next
        }
    }
    # Print all other lines (including Encoding lines that did not match the condition)
    { print }
    ' "$file" > "$file.tmp" && mv "$file.tmp" "$file"

    # Check if the file was actually modified by comparing content (optional optimization)
    # Or just print status based on awk logic if you want to know what happened
    # For now, we just report success. To see changes, you might want to diff.
done

echo "Processing complete."
