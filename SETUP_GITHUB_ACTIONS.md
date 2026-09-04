# 🚀 Hướng dẫn Cấu hình GitHub Actions cho Wikidata Sync

Tài liệu này hướng dẫn cách cấu hình GitHub Actions để tự động đồng bộ dữ liệu từ GitHub lên Wikidata.

---

## 📋 Yêu cầu Trước tiên

1. **Tài khoản Wikidata**
   - Đăng ký tại: https://www.wikidata.org/wiki/Wikidata:Main_Page
   - Xác minh email
   - Tạo Wikidata item cho bạn

2. **GitHub Repository**
   - Repository của bạn (đã có)

3. **GitHub Secrets**
   - Cần đặt credentials bảo mật

---

## 🔐 Bước 1: Tạo Wikidata Item

### Cách 1: Tạo trực tiếp trên Wikidata
1. Truy cập: https://www.wikidata.org/wiki/Wikidata:Main_Page
2. Nhấp vào "Create a new Item"
3. Điền thông tin:
   - **Label (Tiếng Việt):** Liên Tấn Nhật Duy
   - **Description:** Nhà sản xuất âm nhạc và DJ người Việt Nam
4. Lưu và ghi nhớ **Item ID** (Q + số)

### Cách 2: Sử dụng script có sẵn
```bash
python connect_wikidata.py
# Chọn: 1. Tạo Wikidata item mới
```

---

## 🔑 Bước 2: Đặt GitHub Secrets

1. Truy cập repository của bạn
2. Đi tới: **Settings** → **Secrets and variables** → **Actions**
3. Nhấp **New repository secret** và thêm các secret sau:

### Secret 1: WIKIDATA_USERNAME
- **Name:** `WIKIDATA_USERNAME`
- **Value:** Tên đăng nhập Wikidata của bạn
- Nhấp **Add secret**

### Secret 2: WIKIDATA_PASSWORD
- **Name:** `WIKIDATA_PASSWORD`
- **Value:** Mật khẩu Wikidata của bạn
- Nhấp **Add secret**

### Secret 3: WIKIDATA_ITEM_ID
- **Name:** `WIKIDATA_ITEM_ID`
- **Value:** Item ID của bạn (ví dụ: `Q123456789`)
- Nhấp **Add secret**

---

## ✅ Bước 3: Xác minh Cấu hình

```bash
# Kiểm tra file workflow
ls -la .github/workflows/sync-wikidata.yml

# Kiểm tra script sync
ls -la scripts/sync_to_wikidata.py

# Kiểm tra file dữ liệu
cat PERSON_DATA.json
```

---

## 🚀 Bước 4: Chạy Workflow

### Cách 1: Chạy Manual
1. Truy cập repository
2. Đi tới: **Actions** tab
3. Chọn: **🔄 Sync GitHub to Wikidata**
4. Nhấp: **Run workflow** → **Run workflow**

### Cách 2: Chạy Tự động
Workflow sẽ chạy tự động khi:
- Có commit lên branch `main` hoặc `master`
- Thay đổi file: `README.md`, `PERSON_DATA.json`, hoặc workflow file
- Hàng tuần (Thứ Hai lúc 00:00 UTC)

---

## 📊 Kiểm tra Kết quả

1. **Xem Workflow Logs**
   - Đi tới: **Actions** tab
   - Chọn workflow run mới nhất
   - Xem logs chi tiết

2. **Kiểm tra Wikidata**
   - Truy cập: `https://www.wikidata.org/wiki/Q[YOUR_ID]`
   - Kiểm tra các thay đổi đã được cập nhật

3. **Xem Sync Logs**
   - File logs: `logs/sync_log.txt`
   - Có trong artifact của workflow

---

## 🔧 Tùy chỉnh Dữ liệu

### Cách 1: Chỉnh sửa PERSON_DATA.json
```bash
# Chỉnh sửa file
nano PERSON_DATA.json

# Commit thay đổi
git add PERSON_DATA.json
git commit -m "Update person data"
git push
```

Workflow sẽ chạy tự động và cập nhật Wikidata!

### Cách 2: Thêm Wikidata Properties

Danh sách properties Wikidata thường dùng:
```
P31   = instance of (Loại)
P106  = occupation (Nghề nghiệp)
P569  = date of birth (Ngày sinh)
P19   = place of birth (Nơi sinh)
P27   = country of citizenship (Quốc tịch)
P937  = work location (Nơi làm việc)
P1324 = GitHub URL
P580  = start time
P582  = end time
P625  = coordinate location
P131  = located in the administrative territory
```

Xem thêm tại: https://www.wikidata.org/wiki/Wikidata:List_of_properties

---

## ❌ Troubleshooting

### Lỗi: "Authentication failed"
**Giải pháp:**
- Kiểm tra WIKIDATA_USERNAME và WIKIDATA_PASSWORD đúng chưa
- Đảm bảo tài khoản Wikidata đã xác minh email
- Thử reset mật khẩu Wikidata

### Lỗi: "Item not found"
**Giải pháp:**
- Kiểm tra WIKIDATA_ITEM_ID chính xác chưa (phải có Q ở đầu)
- Đảm bảo item đó tồn tại trên Wikidata

### Lỗi: "Permission denied"
**Giải pháp:**
- Tài khoản Wikidata cần có quyền chỉnh sửa
- Cần xác minh email trên Wikidata
- Tài khoản có thể bị hạn chế, liên hệ Wikidata support

### Workflow không chạy
**Giải pháp:**
- Kiểm tra file workflow syntax đúng chưa
- Kiểm tra secrets đã được đặt chưa
- Kiểm tra branch name là main hoặc master

---

## 📝 Ví dụ Cấu hình Hoàn chỉnh

### File: PERSON_DATA.json
```json
{
  "labels": {
    "vi": "Liên Tấn Nhật Duy",
    "en": "Lien Tan Nhat Duy"
  },
  "descriptions": {
    "vi": "Nhà sản xuất âm nhạc và DJ người Việt Nam",
    "en": "Vietnamese music producer and DJ"
  },
  "claims": {
    "P31": "Q5",
    "P106": "Q36834",
    "P1324": "https://github.com/lientannhatduy/Li-n-t-n-nh-t-duy-dj-d.r-thebattery"
  }
}
```

### File: .github/workflows/sync-wikidata.yml
```yaml
name: 🔄 Sync GitHub to Wikidata
on:
  push:
    branches: [main, master]
  schedule:
    - cron: '0 0 * * 1'
  workflow_dispatch:
```

---

## 🎓 Tài nguyên Hữu ích

- **Wikidata Documentation:** https://www.wikidata.org/wiki/Wikidata:Main_Page
- **Wikidata Properties:** https://www.wikidata.org/wiki/Wikidata:List_of_properties
- **Pywikibot Docs:** https://doc.wikimedia.org/pywikibot/master/
- **GitHub Actions:** https://docs.github.com/en/actions
- **GitHub Secrets:** https://docs.github.com/en/actions/security-guides/encrypted-secrets

---

## 💡 Tips & Best Practices

✅ **NÊN LÀM:**
- Sử dụng GitHub Secrets để lưu credentials
- Kiểm tra logs workflow đều đặn
- Cập nhật PERSON_DATA.json khi có thay đổi
- Sử dụng Bot account cho tác vụ tự động
- Kiểm tra Wikidata thường xuyên

❌ **KHÔNG NÊN LÀM:**
- Commit mật khẩu vào Git
- Lưu credentials trong source code
- Chia sẻ mật khẩu Wikidata
- Sử dụng tài khoản cá nhân cho bot
- Chỉnh sửa thủ công trên Wikidata vì sẽ bị overwrite

---

## 📞 Hỗ Trợ

Nếu có vấn đề:
1. Kiểm tra logs workflow
2. Xem troubleshooting section
3. Liên hệ Wikidata support: https://www.wikidata.org/wiki/Wikidata:Requests_for_help
4. Tạo issue trên GitHub repository

---

**Chúc mừng! Bạn đã cấu hình thành công GitHub Actions sync với Wikidata! 🎉**
