import argparse
import os
import sys
from PIL import Image

SUPPORTED_EXTENSIONS = (".jpg", ".jpeg", ".png", ".webp")

def process_single_image(input_path, output_path=None):
    abs_input = os.path.abspath(input_path)
    
    if not output_path:
        directory = os.path.dirname(abs_input)
        original_filename = os.path.basename(abs_input)
        output_path = os.path.join(directory, f"clean_{original_filename}")
    else:
        output_path = os.path.abspath(output_path)

    try:
        with Image.open(abs_input) as img:
            if img.mode not in ("RGB", "RGBA"):
                img = img.convert("RGB")

            # Tạo ảnh mới chỉ chứa dữ liệu điểm ảnh (xóa sạch EXIF, XMP, IPTC, C2PA)
            clean_img = Image.new(img.mode, img.size)
            clean_img.putdata(list(img.getdata()))

            ext_lower = output_path.lower()
            
            if ext_lower.endswith((".jpg", ".jpeg")):
                if clean_img.mode == "RGBA":
                    clean_img = clean_img.convert("RGB")
                clean_img.save(output_path, format="JPEG", quality=100, subsampling=0)
                
            elif ext_lower.endswith(".png"):
                clean_img.save(output_path, format="PNG", compress_level=1)
                
            elif ext_lower.endswith(".webp"):
                clean_img.save(output_path, format="WEBP", lossless=True)
                
            else:
                clean_img.save(output_path)

        # In ra đường dẫn đầy đủ của từng file mới tạo
        print(output_path)
        return True

    except Exception as e:
        print(f"❌ Error processing '{abs_input}': {e}", file=sys.stderr)
        return False

def process_target(target_path, output_path=None, recursive=False):
    if not os.path.exists(target_path):
        print(f"❌ Error: Path not found at '{target_path}'", file=sys.stderr)
        sys.exit(1)

    # Trường hợp 1: Đầu vào là một file đơn lẻ
    if os.path.isfile(target_path):
        success = process_single_image(target_path, output_path)
        if not success:
            sys.exit(1)
        return

    # Trường hợp 2: Đầu vào là một thư mục (Batch processing)
    if os.path.isdir(target_path):
        abs_dir = os.path.abspath(target_path)
        
        if output_path:
            os.makedirs(output_path, exist_ok=True)

        files_to_process = []
        if recursive:
            for root, _, files in os.walk(abs_dir):
                for f in files:
                    if f.lower().endswith(SUPPORTED_EXTENSIONS) and not f.startswith("clean_"):
                        files_to_process.append(os.path.join(root, f))
        else:
            for f in os.listdir(abs_dir):
                full_p = os.path.join(abs_dir, f)
                if os.path.isfile(full_p) and f.lower().endswith(SUPPORTED_EXTENSIONS) and not f.startswith("clean_"):
                    files_to_process.append(full_p)

        if not files_to_process:
            print("⚠️ No eligible images found to clean.", file=sys.stderr)
            return

        for file_path in sorted(files_to_process):
            if output_path:
                # Giữ cấu trúc thư mục con nếu dùng cờ -r cùng -o
                rel_path = os.path.relpath(file_path, abs_dir)
                rel_dir = os.path.dirname(rel_path)
                base_name = os.path.basename(rel_path)
                target_sub_dir = os.path.join(output_path, rel_dir)
                os.makedirs(target_sub_dir, exist_ok=True)
                dest_file = os.path.join(target_sub_dir, f"clean_{base_name}")
            else:
                dest_file = None

            process_single_image(file_path, dest_file)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Remove AI metadata (C2PA, EXIF, XMP, IPTC) from a single image or batch process a directory."
    )
    parser.add_argument("target_path", help="Path to a source image file or a directory of images")
    parser.add_argument("-o", "--output", help="Optional custom output file path (for single file) or output directory (for batch)", default=None)
    parser.add_argument("-r", "--recursive", action="store_true", help="Recursively process subdirectories when target_path is a folder")
    
    args = parser.parse_args()
    process_target(args.target_path, args.output, args.recursive)
