# AI Meta Cleaner (Agent Skill)

[English](#english) | [Tiếng Việt](#tiếng-việt)

---

## English

An open-standard **Agent Skill** compatible with **Claude Code** and **OpenAI Codex** to strip AI metadata (`C2PA Content Credentials`, `EXIF`, `XMP`, `IPTC`) from single images or entire directories while preserving maximum visual quality.

### Features
- **Strips All AI Provenance:** Removes C2PA JUMBF containers, IPTC `DigitalSourceType`, XMP, and EXIF tags to prevent false AI flags on social platforms.
- **Maximum Quality:** Uses lossless PNG compression, lossless WebP, and 4:4:4 (`subsampling=0`, `quality=100`) JPEG encoding.
- **Single & Batch Processing:** Supports cleaning a single image or batch-processing entire folders (including nested subfolders with `-r`).
- **Auto-Prefixing:** Saves cleaned outputs as `clean_<original_filename>` by default.

### Installation

#### 1. Install Python Dependency
```bash
pip install -r requirements.txt
```

#### 2. Install as an Agent Skill
* **For Claude Code (Global):**
  ```bash
  cp -r ai-meta-cleaner ~/.claude/skills/
  ```
* **For OpenAI Codex (Global):**
  ```bash
  cp -r ai-meta-cleaner ~/.agents/skills/
  ```
  *(Alternatively, place the folder inside `.claude/skills/` or `.agents/skills/` within any project repository).*

### Usage

#### Via Claude Code or Codex
Once installed, simply prompt your AI agent naturally:
> *"Clean AI metadata from `/path/to/my_image.png`"*
> *"Batch remove C2PA tags from all images in `./assets/banners`"*
> *"Clean metadata recursively in `./posts` and save them to `./posts_clean`"*

#### Via Command Line (CLI)
```bash
# Clean a single image (outputs clean_photo.png in the same folder)
python scripts/remove_c2pa.py path/to/photo.png

# Batch clean all images in a directory
python scripts/remove_c2pa.py path/to/folder

# Recursively clean subfolders and output to a custom directory
python scripts/remove_c2pa.py path/to/folder -r -o path/to/clean_folder
```

---

## Tiếng Việt

**Agent Skill** chuẩn mở tương thích với **Claude Code** và **OpenAI Codex**, giúp xóa sạch toàn bộ siêu dữ liệu AI (`C2PA Content Credentials`, `EXIF`, `XMP`, `IPTC`) khỏi một file ảnh hoặc hàng loạt ảnh trong thư mục mà vẫn giữ nguyên chất lượng hiển thị cao nhất.

### Tính năng nổi bật
- **Xóa triệt để dấu vết AI:** Loại bỏ hoàn toàn chứng chỉ số C2PA (JUMBF), thẻ IPTC `DigitalSourceType`, XMP và EXIF nhằm tránh việc các nền tảng mạng xã hội (như Facebook) gắn nhãn AI gây giảm tương tác.
- **Giữ chất lượng tối đa:** Xuất ảnh PNG không suy hao (Lossless), WebP Lossless và JPEG chất lượng 100 (`subsampling=0`) giúp chữ và chi tiết ảnh luôn sắc nét.
- **Xử lý đơn lẻ & hàng loạt:** Hỗ trợ làm sạch từng file ảnh hoặc quét toàn bộ thư mục (bao gồm cả thư mục con với tùy chọn `-r`).
- **Tự động đặt tên:** Mặc định lưu file mới với tiền tố `clean_<tên_file_gốc>` và tự động bỏ qua các file đã có tiền tố `clean_`.

### Cài đặt

#### 1. Cài đặt thư viện Python cần thiết
```bash
pip install -r requirements.txt
```

#### 2. Cài đặt làm Agent Skill
* **Dành cho Claude Code (Toàn cục):**
  ```bash
  cp -r ai-meta-cleaner ~/.claude/skills/
  ```
* **Dành cho OpenAI Codex (Toàn cục):**
  ```bash
  cp -r ai-meta-cleaner ~/.agents/skills/
  ```
  *(Hoặc đặt thư mục này vào `.claude/skills/` hay `.agents/skills/` bên trong thư mục dự án của bạn).*

### Hướng dẫn sử dụng

#### Gọi tự nhiên qua Claude Code hoặc Codex
Sau khi cài đặt, bạn chỉ cần ra lệnh bằng ngôn ngữ tự nhiên:
> *"Xóa metadata AI cho ảnh `/duong/dan/toi/anh_tin_tuc.png`"*
> *"Làm sạch tag C2PA hàng loạt cho tất cả ảnh trong thư mục `./banners`"*
> *"Dọn dẹp metadata toàn bộ ảnh kể cả thư mục con trong `./posts` và lưu sang `./posts_clean`"*

#### Chạy trực tiếp qua dòng lệnh (CLI)
```bash
# Làm sạch 1 file ảnh (xuất ra file clean_photo.png cùng thư mục)
python scripts/remove_c2pa.py duong/dan/photo.png

# Làm sạch hàng loạt tất cả ảnh trong 1 thư mục
python scripts/remove_c2pa.py duong/dan/thu_muc

# Quét cả thư mục con (-r) và xuất sang thư mục riêng (-o)
python scripts/remove_c2pa.py duong/dan/thu_muc -r -o duong/dan/thu_muc_sach
```
