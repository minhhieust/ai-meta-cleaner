---
name: ai-meta-cleaner
description: Strip AI metadata (C2PA Content Credentials, EXIF, XMP, IPTC) from single images or batch process entire directories while preserving maximum visual quality and outputting clean_ prefixed files. Use this skill when the user asks to remove AI tags, clean image metadata, strip C2PA, batch clean a folder of images, or prepare AI-edited images for social media.
---

# AI Meta Cleaner

This skill removes all embedded AI provenance tags (C2PA Content Credentials, IPTC `DigitalSourceType`, XMP, EXIF) from single image files or entire folders while maintaining maximum visual quality.

## Prerequisites
Ensure `Pillow` is installed in the active Python environment:
```bash
pip install -r scripts/../requirements.txt
```

## Workflow
When the user provides an image path or a directory path:

1. **Single Image or Directory (Top-level):**
   Run the bundled Python script located at `scripts/remove_c2pa.py` relative to this skill directory:
   ```bash
   python scripts/remove_c2pa.py "<input_file_or_directory_path>"
   ```
   - For a single image, it outputs `clean_<filename>` in the same folder.
   - For a directory, it processes all `.jpg`, `.jpeg`, `.png`, and `.webp` files (skipping existing `clean_*` files) and saves `clean_<filename>` alongside each original.
   - All newly created file paths are printed to `stdout` (one per line).

2. **Recursive Directory Processing (Include Subfolders):**
   Add the `-r` flag if the user wants to clean images inside nested subdirectories:
   ```bash
   python scripts/remove_c2pa.py "<directory_path>" -r
   ```

3. **Custom Output File or Output Directory:**
   Use the `-o` flag to save the cleaned file(s) to a specific destination:
   ```bash
   python scripts/remove_c2pa.py "<input_path>" -o "<custom_output_path>"
   ```

4. Report the list of newly generated clean file paths back to the user.
