#!/usr/bin/env python3
"""
Split a PDF into fixed-size chunks (default: 50 pages) and stop at a given end page (default: 230).
Each chunk is written as a separate PDF, named by its page range (1-based, inclusive).

Examples:
    python split_pdf_chunks.py -i input.pdf -o out_dir
    python split_pdf_chunks.py -i input.pdf -o out_dir -s 40 -e 180

Notes:
- Page numbers in arguments are 1-based.
- End page will be capped to the total number of pages if it exceeds it.
- If the PDF has fewer pages than the first chunk, a single chunk up to end page is produced.
"""

import argparse
import os
import sys

# Try both pypdf (new) and PyPDF2 (common) for maximum compatibility
try:
    from pypdf import PdfReader, PdfWriter
    LIB = "pypdf"
except Exception:
    try:
        from PyPDF2 import PdfReader, PdfWriter  # type: ignore
        LIB = "PyPDF2"
    except Exception as e:
        print("Error: Could not import pypdf or PyPDF2. Please install one of them:\n"
              "  pip install pypdf\n"
              "or\n"
              "  pip install PyPDF2", file=sys.stderr)
        sys.exit(1)


def split_pdf_by_chunks(input_path: str, output_dir: str, chunk_size: int = 50, end_page: int = 230) -> None:
    """
    Split a PDF into chunks of `chunk_size` pages, stopping at `end_page` (1-based, inclusive).
    Writes files to `output_dir` with names like `input_001-050.pdf`, `input_051-100.pdf`, etc.

    Args:
        input_path: Path to source PDF.
        output_dir: Directory to write output PDFs. Will be created if missing.
        chunk_size: Number of pages per chunk. (Default: 50)
        end_page: 1-based page number at which to stop splitting, inclusive. (Default: 230)
    """
    if chunk_size <= 0:
        raise ValueError("chunk_size must be a positive integer.")
    if end_page <= 0:
        raise ValueError("end_page must be a positive integer (1-based).")

    # Load the PDF
    reader = PdfReader(input_path)
    total_pages = len(reader.pages)

    # Cap end_page to the actual document size
    end_page_capped = min(end_page, total_pages)

    if end_page_capped < 1:
        print("Nothing to do: end_page is less than 1 after capping.", file=sys.stderr)
        return

    # Prepare output directory
    os.makedirs(output_dir, exist_ok=True)

    # Base name for output files
    base = os.path.splitext(os.path.basename(input_path))[0]

    # Iterate in 1-based page space
    start_page = 1
    file_count = 0

    while start_page <= end_page_capped:
        stop_page = min(start_page + chunk_size - 1, end_page_capped)  # inclusive, 1-based

        writer = PdfWriter()
        # Convert to 0-based indices for reader.pages
        for p in range(start_page - 1, stop_page):
            writer.add_page(reader.pages[p])

        # Build filename with zero-padded ranges (e.g., 001-050)
        width = len(str(end_page_capped))
        fname = f"{base}_{str(start_page).zfill(width)}-{str(stop_page).zfill(width)}.pdf"
        out_path = os.path.join(output_dir, fname)

        with open(out_path, "wb") as f:
            writer.write(f)

        file_count += 1
        print(f"Wrote: {out_path} (pages {start_page}-{stop_page})")

        # Advance to next chunk
        start_page = stop_page + 1

    print(f"Done. Library used: {LIB}. Chunks written: {file_count}. End page reached: {end_page_capped}/{total_pages}.")


def main():
    parser = argparse.ArgumentParser(description="Split a PDF into fixed-size chunks, stopping at a given end page.")
    parser.add_argument("-i", "--input", required=True, help="Path to input PDF")
    parser.add_argument("-o", "--output", required=True, help="Output directory for chunked PDFs")
    parser.add_argument("-s", "--size", type=int, default=50, help="Chunk size in pages (default: 50)")
    parser.add_argument("-e", "--end", type=int, default=230, help="End page (1-based, inclusive). Stop splitting at this page (default: 230)")

    args = parser.parse_args()

    try:
        split_pdf_by_chunks(args.input, args.output, chunk_size=args.size, end_page=args.end)
    except Exception as ex:
        print(f"Error: {ex}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
