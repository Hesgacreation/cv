#!/bin/bash
set -e
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PDF_DIR="$(cd "$SCRIPT_DIR/../pdf" && pwd)"

echo "=== Compilation des fichiers LaTeX (TeX Live / pdflatex) ==="

for f in "$SCRIPT_DIR"/*.tex; do
    name=$(basename "$f")
    echo "Compilation de $name..."
    pdflatex -interaction=nonstopmode "$name" > /dev/null
    pdf_name="${name%.tex}.pdf"
    if [ -f "$pdf_name" ]; then
        cp "$pdf_name" "$PDF_DIR/"
        pages=$(pdfinfo "$pdf_name" | grep "Pages:" | awk '{print $2}')
        echo "  -> $pdf_name ($pages page(s)) exporté dans pdf/"
    fi
done

# Nettoyage des fichiers temporaires
rm -f "$SCRIPT_DIR"/*.aux "$SCRIPT_DIR"/*.log "$SCRIPT_DIR"/*.out "$SCRIPT_DIR"/*.synctex.gz

echo "=== Tout est à jour dans ../pdf/ ==="
