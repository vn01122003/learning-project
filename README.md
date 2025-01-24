# Side-Project

## 1. Setup

### **Bước 1: Tạo môi trường ảo**
1. Di chuyển đến thư mục dự án:
   ```bash
   cd <đường dẫn đến thư mục dự án>
   ```
2. Tạo môi trường ảo với tên `pj1`:
   ```bash
   python -m venv pj1
   ```

### **Bước 2: Kích hoạt môi trường ảo**
- Trên **Windows** (PowerShell):
  ```bash
  activate pj1
  ```

### **Bước 3: Tải các thư viện**
1. Cài đặt các thư viện cần thiết:
   ```bash
   pip install "fastapi[standard]"
   ```

2. Lưu danh sách các thư viện đã cài đặt (nếu cần):
   ```bash
   pip freeze > requirements.txt
   ```

### **Bước 4: Khởi chạy app**
   ```bash
   fastapi dev
   ```

Bạn đã sẵn sàng để bắt đầu dự án! Nếu có bất kỳ thắc mắc nào, hãy liên hệ với nhóm phát triển.