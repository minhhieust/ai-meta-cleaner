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
  Copy the `ai-meta-cleaner` folder into your global Claude skills directory:
  ```bash
  # macOS / Linux
  cp -r ai-meta-cleaner ~/.claude/skills/

  # Windows (PowerShell)
  Copy-Item -Recurse ai-meta-cleaner "$env:USERPROFILE\.claude\skills\"
  ```
* **For OpenAI Codex (Global):**
  Copy the `ai-meta-cleaner` folder into your Codex skills directory:
  * **Windows:** `C:\Users\<OS_UserName>\.codex\skills\`
    ```powershell
    Copy-Item -Recurse ai-meta-cleaner "C:\Users\<OS_UserName>\.codex\skills\"
    ```
  * **macOS / Linux:** `~/.codex/skills/` (or `~/.agents/skills/`)
    ```bash
    cp -r ai-meta-cleaner ~/.codex/skills/
    ```
  *(Alternatively, place the folder inside `.claude/skills/` or `.codex/skills/` within any specific project repository).*

### Usage

#### 1. Via Claude Code or Codex
**Method A: Quick Chat Attachment (Easiest)**
Select an image from the chat box of **Codex** or **Claude Code** (or copy and paste the image directly into the chat), then use this simple prompt:
```text
$ai-meta-cleaner remove AI Meta for this image
```
*(Note: In Claude Code, you can also invoke the skill using `/ai-meta-cleaner`).*

**Method B: Natural Language with File or Folder Paths**
Prompt your AI agent with specific paths for single or batch processing:
> *"Clean AI metadata from `/path/to/my_image.png`"*
> *"Batch remove C2PA tags from all images in `./assets/banners`"*
> *"Clean metadata recursively in `./posts` and save them to `./posts_clean`"*

#### 2. Via Command Line (CLI)
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
  Sao chép thư mục `ai-meta-cleaner` vào thư mục skills của Claude:
  ```bash
  # macOS / Linux
  cp -r ai-meta-cleaner ~/.claude/skills/

  # Windows (PowerShell)
  Copy-Item -Recurse ai-meta-cleaner "$env:USERPROFILE\.claude\skills\"
  ```
* **Dành cho OpenAI Codex (Toàn cục):**
  Sao chép thư mục `ai-meta-cleaner` vào thư mục skills của Codex:
  * **Trên Windows:** Lưu tại đường dẫn `C:\Users\<OS_UserName>\.codex\skills\`
    ```powershell
    Copy-Item -Recurse ai-meta-cleaner "C:\Users\<OS_UserName>\.codex\skills\"
    ```
  * **Trên macOS / Linux:** Lưu tại `~/.codex/skills/` (hoặc `~/.agents/skills/`)
    ```bash
    cp -r ai-meta-cleaner ~/.codex/skills/
    ```
  *(Hoặc bạn có thể đặt thư mục này vào `.claude/skills/` hay `.codex/skills/` bên trong thư mục dự án cụ thể của bạn).*

### Hướng dẫn sử dụng

#### 1. Sử dụng qua Claude Code hoặc Codex
**Cách 1: Dán ảnh trực tiếp vào khung chat (Đơn giản nhất)**
Bạn có thể chọn ảnh từ khung chat của **Codex** hoặc **Claude Code** (hoặc sao chép ảnh và dán thẳng vào khung chat), sau đó dùng prompt đơn giản sau để xóa AI Meta cho ảnh:
```text
\$ai-meta-cleaner xóa AI Meta cho ảnh này
```
*(Lưu ý: Trên Claude Code, bạn cũng có thể gọi bằng dấu gạch chéo `/ai-meta-cleaner`).*

**Cách 2: Ra lệnh bằng ngôn ngữ tự nhiên với đường dẫn file/thư mục**
> *"Xóa metadata AI cho ảnh `C:\images\anh_tin_tuc.png`"*
> *"Làm sạch tag C2PA hàng loạt cho tất cả ảnh trong thư mục `./banners`"*
> *"Dọn dẹp metadata toàn bộ ảnh kể cả thư mục con trong `./posts` và lưu sang `./posts_clean`"*

#### 2. Chạy trực tiếp qua dòng lệnh (CLI)
```bash
# Làm sạch 1 file ảnh (xuất ra file clean_photo.png cùng thư mục)
python scripts/remove_c2pa.py duong/dan/photo.png

# Làm sạch hàng loạt tất cả ảnh trong 1 thư mục
python scripts/remove_c2pa.py duong/dan/thu_muc

# Quét cả thư mục con (-r) và xuất sang thư mục riêng (-o)
python scripts/remove_c2pa.py duong/dan/thu_muc -r -o duong/dan/thu_muc_sach
```
