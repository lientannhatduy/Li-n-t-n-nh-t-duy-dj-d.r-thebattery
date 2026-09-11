># 🌐 Automatic Wikidata Setup Guide

Hướng dẫn tự động tạo và quản lý Wikidata item cho Liên Tấn Nhật Duy

---

## 📋 Yêu Cầu

✅ **Wikidata Account**
- Username: `lientannhatduy`
- Email: `lientannhatduy@gmail.com`
- Account phải được xác nhận (4 ngày)

✅ **GitHub Secrets** (để GitHub Actions có thể tạo Wikidata)

---

## 🚀 Bước 1: Xác Nhận Tài Khoản Wikidata

### Nếu vừa tạo account mới:
1. Kiểm tra email `lientannhatduy@gmail.com`
2. Click link xác nhận
3. **Đợi 4 ngày** để account được auto-confirmed (để có quyền edit)

### Kiểm tra trạng thái:
```
Truy cập: https://www.wikidata.org/wiki/Special:Preferences
Xem: User preferences → Rights (phải có "edit" right)
```

---

## 🔐 Bước 2: Setup GitHub Secrets

GitHub Actions cần credentials để tạo Wikidata. Bạn cần add 2 secrets:

### Cách thêm Secrets:

1. **Vào Repository Settings**
   ```
   https://github.com/lientannhatduy/Li-n-t-n-nh-t-duy-dj-d.r-thebattery/settings/secrets/actions
   ```

2. **Tạo 2 secrets mới:**

   **Secret 1: WIKIDATA_USERNAME**
   - Name: `WIKIDATA_USERNAME`
   - Value: `lientannhatduy`
   - Click "Add secret"

   **Secret 2: WIKIDATA_PASSWORD**
   - Name: `WIKIDATA_PASSWORD`
   - Value: *Mật khẩu Wikidata của bạn*
   - Click "Add secret"

✅ Bây giờ GitHub Actions có thể kết nối Wikidata!

---

## 🎯 Bước 3: Chạy Script Lần Đầu

### Cách 1: Chạy Tự Động (GitHub Actions)

```
1. Vào: Actions tab của repository
2. Chọn: "🌐 Auto Wikidata Update" workflow
3. Click: "Run workflow" → "Run workflow" (button xanh)
```

Hoặc push code sẽ trigger tự động:
```bash
git add .
git commit -m "trigger wikidata update"
git push
```

### Cách 2: Chạy Thủ Công (Local)

```bash
# Cài dependencies
pip install pywikibot requests

# Tạo file credentials
cat > .wikidata_config.json << EOF
{
  "username": "lientannhatduy",
  "password": "YOUR_PASSWORD"
}
EOF

# Chạy script
python3 auto_create_wikidata.py
```

---

## ✅ Xác Nhận Thành Công

Khi script chạy xong, bạn sẽ thấy:

```
✅ SUCCESS!
============================================================
Item ID: Q123456
Wikidata URL: https://www.wikidata.org/wiki/Q123456
GitHub URL: https://github.com/lientannhatduy/...
============================================================
```

### Kiểm tra trên Wikidata:
1. Truy cập URL trên (https://www.wikidata.org/wiki/Q123456)
2. Xem thông tin:
   - ✅ Label: Liên Tấn Nhật Duy
   - ✅ Description: Vietnamese DJ, music producer, and software developer
   - ✅ Properties: Country, Occupations, GitHub link

---

## 📊 Thông Tin Được Tạo

Script sẽ tạo Wikidata item với:

### Labels (Tên)
- **English**: Liên Tấn Nhật Duy
- **Vietnamese**: Liên Tấn Nhật Duy

### Descriptions (Mô Tả)
- **English**: Vietnamese DJ, music producer, and software developer
- **Vietnamese**: Nhạc sĩ DJ, nhà sản xuất nhạc, và lập trình viên người Việt Nam

### Aliases (Bí Danh)
- Lien Tan Nhat Duy
- Duy Lien
- DJ Duy

### Properties (Thuộc Tính)
| Property | Value | Ý Nghĩa |
|----------|-------|---------|
| P31 | Q5 | Instance of: Human (Con người) |
| P27 | Q881 | Country: Vietnam (Đất nước: Việt Nam) |
| P106 | Q36834, Q177220, Q5482740 | Occupations: Music Producer, DJ, Programmer |
| P1324 | https://github.com/lientannhatduy | GitHub URL |

---

## 🔄 Cập Nhật Thường Xuyên

Script có thể chạy tự động:

### Tùy Chọn 1: Chạy theo lịch (Tháng 1 lần)
Đã setup trong `.github/workflows/auto_wikidata.yml`:
```yaml
schedule:
  - cron: '0 0 1 * *'  # Run on 1st of each month
```

### Tùy Chọn 2: Chạy thủ công khi cần
```bash
# Trên GitHub Actions
1. Actions → "🌐 Auto Wikidata Update"
2. "Run workflow" button
```

### Tùy Chọn 3: Chạy khi push
Workflow tự động trigger khi push:
```bash
git push
# → GitHub Actions tự động chạy script
```

---

## 🛠️ Chỉnh Sửa Thông Tin

Muốn thay đổi thông tin Wikidata? Edit file `auto_create_wikidata.py`:

```python
WIKIDATA_CONFIG = {
    "person": {
        "label_en": "Liên Tấn Nhật Duy",  # ← Thay đổi tên
        "description_en": "...",  # ← Thay đổi mô tả
        "aliases": ["...", "..."],  # ← Thêm bí danh
    },
    "properties": {
        "P106": ["Q36834", "Q177220"],  # ← Thay đổi nghề nghiệp
        # Thêm properties khác
    }
}
```

Rồi commit và push:
```bash
git add auto_create_wikidata.py
git commit -m "update: Modify Wikidata properties"
git push
```

---

## 📍 Wikidata Properties Tham Khảo

Muốn thêm thuộc tính khác? Xem danh sách:

| Property | Meaning | Example |
|----------|---------|---------|
| P569 | Date of birth | "1990-01-01" |
| P19 | Place of birth | Q13827 (Kiên Giang) |
| P937 | Work location | Q881 (Vietnam) |
| P2397 | YouTube channel | "UCxxxxxx" |
| P856 | Official website | "https://example.com" |
| P407 | Language | Q7850 (Vietnamese) |

Find more: https://www.wikidata.org/wiki/Wikidata:List_of_properties

---

## ❓ Troubleshooting

### ❌ "Login failed"
**Giải pháp:**
- ✓ Kiểm tra username/password đúng không
- ✓ Xác nhận account email
- ✓ Đợi 4 ngày nếu account mới

### ❌ "Permission denied"
**Giải pháp:**
- ✓ Account phải được auto-confirmed (4 ngày)
- ✓ Xem: Special:Preferences → Rights phải có "edit"
- ✓ Thử lại sau 4 ngày

### ❌ "Secrets not found"
**Giải pháp:**
- ✓ Vào: Settings → Secrets → Add secrets
- ✓ Thêm `WIKIDATA_USERNAME` và `WIKIDATA_PASSWORD`

### ❌ "Item not created"
**Giải pháp:**
- ✓ Kiểm tra logs: Actions → Run details
- ✓ Xem lỗi cụ thể
- ✓ Báo lỗi nếu cần

---

## 📚 Tài Liệu Thêm

- 📖 Wikidata Main Page: https://www.wikidata.org
- 📖 Pywikibot Docs: https://doc.wikimedia.org/pywikibot/master/
- 📖 Properties List: https://www.wikidata.org/wiki/Wikidata:List_of_properties

---

## ✨ Kế Tiếp?

- ✅ Tạo Wikidata item
- ✅ Setup GitHub Actions
- 🎯 **Thêm nhiều properties** (ngày sinh, địa điểm, v.v.)
- 🎯 **Link với Wikipedia** (khi có bài viết)
- 🎯 **Tạo items khác** (dự án, bạn bè, v.v.)

---

**Có gì cần giúp? Comment lại nhé!** 🚀
