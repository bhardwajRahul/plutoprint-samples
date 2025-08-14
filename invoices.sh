#!/bin/bash

# Loop over all invoice PDFs
for pdf in invoice-*.pdf; do
    # Extract base name without extension
    base=$(basename "$pdf" .pdf)

    # Step 1: Convert PDF page to PNG scaled to 340x460
    pdftoppm -png -scale-to-x 340 -scale-to-y 460 "$pdf" "$base"

    # Step 2: Apply 10px shadow using ImageMagick
    convert "${base}-1.png" \
        \( +clone -background black -shadow 80x4+0+0 \) \
        +swap -background transparent -layers merge +repage \
        "${base}.png"

    # Optional: remove intermediate file
    rm -f "${base}-1.png"

    echo "Processed $pdf → ${base}.png"
done
