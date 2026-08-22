#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
WIKIDATA AUTHENTICATION GUIDE
Hướng dẫn xác thực và sử dụng script kết nối Wikidata
"""

# ============================================================
# 📚 HƯỚNG DẪN SỬ DỤNG - WIKIDATA CONNECTOR
# ============================================================

"""
1️⃣ CÀI ĐẶT DEPENDENCIES
========================

pip install pywikibot requests

Hoặc:

pip install -r requirements.txt

2️⃣ PHƯƠNG THỨC XÁC THỰC
========================

A) XÁC THỰC BẰNG TÊN ĐĂNG NHẬP & MẬT KHẨU
   - Đơn giản nhất
   - Không cần trình duyệt
   - Thông tin được lưu trong .wikidata_config.json
   ⚠️  Lưu ý: Mật khẩu sẽ được lưu dưới dạng plain text (bảo mật thấp)

B) XÁC THỰC BẰNG OAUTH 2.0
   - An toàn nhất
   - Cần trình duyệt
   - Không lưu mật khẩu
   - Được khuyến khích sử dụng

C) DÙNG THÔNG TIN ĐÃ LƯU
   - Sử dụng lại thông tin xác thực trước
   - Nhanh chóng và tiện lợi

3️⃣ CÁCH CHẠY SCRIPT
==================

python connect_wikidata.py

Hoặc:

python3 connect_wikidata.py

4️⃣ CÁC TÍNH NĂNG
================

✅ Tạo Wikidata item mới
   - Thêm labels (tên)
   - Thêm descriptions (mô tả)
   - Thêm aliases (tên gọi khác)
   - Thêm properties/claims (thuộc tính)

✅ Cập nhật Wikidata item
   - Chỉnh sửa thông tin hiện có
   - Cập nhật descriptions
   - Thêm/sửa labels

✅ Kết nối GitHub với Wikidata
   - Liên kết GitHub URL (property P1324)
   - Tự động thêm link repository

5️⃣ STRUCTURE CỦA CREDENTIALS
============================

File .wikidata_config.json:

{
  "username": "your_wikidata_username",
  "password": "your_password"
}

⚠️  BẢOSECURITY:
- File này chỉ có quyền đọc của owner (chmod 600)
- Không commit vào Git
- Thêm .wikidata_config.json vào .gitignore

6️⃣ CÁC PROPERTY ĐƯỢC SỬ DỤNG
=============================

P31   = instance of (Loại)
P106  = occupation (Nghề nghiệp)
P569  = date of birth (Ngày sinh)
P19   = place of birth (Nơi sinh)
P27   = country of citizenship (Quốc tịch)
P937  = work location (Nơi làm việc)
P1324 = GitHub URL (Link GitHub)

7️⃣ VÍ DỤ SỬ DỤNG
================

>>> # Đăng nhập
>>> python connect_wikidata.py
>>> # Chọn: 1 (Username/Password) hoặc 2 (OAuth)
>>> # Nhập thông tin đăng nhập

>>> # Tạo item mới
>>> # Chọn: 1

>>> # Cập nhật item
>>> # Chọn: 2
>>> # Nhập item ID: Q12345

>>> # Kết nối GitHub
>>> # Chọn: 3
>>> # Nhập item ID: Q12345

8️⃣ TROUBLESHOOTING
==================

❌ "Đăng nhập thất bại"
   → Kiểm tra tên đăng nhập và mật khẩu
   → Đảm bảo tài khoản Wikidata đã kích hoạt
   → Thử xác thực OAuth

❌ "Item not found"
   → Kiểm tra item ID (Q + số)
   → Đảm bảo item đó tồn tại trên Wikidata

❌ "Permission denied"
   → Tài khoản Wikidata cần có quyền chỉnh sửa
   → Cần xác minh email

❌ "Connection error"
   → Kiểm tra kết nối Internet
   → Thử sau vài phút

9️⃣ WIKIDATA ITEM IDS
====================

Q5        = human (Con người)
Q36834    = music producer (Nhà sản xuất nhạc)
Q177220   = DJ (Nhạc sĩ DJ)
Q13827    = Kiên Giang Province (Tỉnh Kiên Giang)
Q881      = Vietnam (Việt Nam)
Q11816    = Vietnam (Đất nước Việt Nam)

🔟 BẢOMẬT CÓ TRÁCH NHIỆM
=======================

✅ NÊN LÀM:
  - Sử dụng OAuth 2.0 nếu có thể
  - Xóa credentials sau khi xong
  - Không commit .wikidata_config.json
  - Thêm vào .gitignore
  - Sử dụng Bot account cho tác vụ tự động

❌ KHÔNG NÊN LÀM:
  - Chia sẻ mật khẩu
  - Commit credentials vào Git
  - Lưu mật khẩu trong source code
  - Sử dụng tài khoản cá nhân cho bot

1️⃣1️⃣ RESOURCES
==============

📖 Wikidata Documentation:
   https://www.wikidata.org/wiki/Wikidata:Main_Page

📖 Pywikibot Documentation:
   https://doc.wikimedia.org/pywikibot/master/

📖 Wikidata Properties:
   https://www.wikidata.org/wiki/Wikidata:List_of_properties

🔐 OAuth Instructions:
   https://www.mediawiki.org/wiki/OAuth/For_Developers

1️⃣2️⃣ LIÊN HỆ & HỖ TRỢ
====================

GitHub Repository:
https://github.com/lientannhatduy/Li-n-t-n-nh-t-duy-dj-d.r-thebattery

Wikidata Help:
https://www.wikidata.org/wiki/Wikidata:Requests_for_help

Pywikibot Issues:
https://gerrit.wikimedia.org/r/#/q/project:pywikibot/core

"""

# ============================================================
# QUICK START EXAMPLE
# ============================================================

def quick_start_example():
    """
    Ví dụ nhanh để bắt đầu
    """
    
    print("""
    ╔════════════════════════════════════════════════════════════╗
    ║         QUICK START - BẮTĐẦU NHANH                        ║
    ╚════════════════════════════════════════════════════════════╝
    
    BƯỚC 1: Cài đặt
    ─────────────
    $ pip install pywikibot requests
    
    BƯỚC 2: Chạy script
    ──────────────────
    $ python connect_wikidata.py
    
    BƯỚC 3: Chọn phương thức xác thực
    ────────────────────────────────
    1. Username & Password (đơn giản)
    2. OAuth 2.0 (an toàn hơn)
    3. Thông tin đã lưu (nếu có)
    
    BƯỚC 4: Nhập thông tin đăng nhập Wikidata
    ────────────────────────────────────────
    Username: your_wikidata_username
    Password: ••••••••••
    
    BƯỚC 5: Chọn thao tác
    ───────────────────
    1. Tạo Wikidata item mới
    2. Cập nhật Wikidata item
    3. Kết nối GitHub
    
    BƯỚC 6: Nhập thông tin cần thiết
    ──────────────────────────────
    Ví dụ với "Tạo item mới":
    - Sẽ tạo item cho Liên Tấn Nhật Duy
    - Tự động thêm thông tin từ PERSON_DATA
    - In ra Item ID (Q-number)
    
    HOÀN TẤT! 🎉
    ──────────
    Item của bạn đã được tạo trên Wikidata
    Xem tại: https://www.wikidata.org/wiki/Q[YOUR_ID]
    
    """)

if __name__ == "__main__":
    quick_start_example()
