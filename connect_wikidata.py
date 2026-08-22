#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script kết nối GitHub với Wikidata
Tạo/cập nhật Wikidata item cho Liên Tấn Nhật Duy
"""

import pywikibot
from pywikibot import pagegenerators
import requests
import json
from datetime import datetime

# Cấu hình Wikidata
WIKIDATA_SITE = pywikibot.Site("wikidata", "wikidata")
REPO = WIKIDATA_SITE.data_repository()

# Thông tin người cần thêm vào Wikidata
PERSON_DATA = {
    "labels": {
        "vi": "Liên Tấn Nhật Duy",
        "en": "Lien Tan Nhat Duy"
    },
    "descriptions": {
        "vi": "Nhà sản xuất âm nhạc và DJ người Việt Nam",
        "en": "Vietnamese music producer and DJ"
    },
    "claims": {
        "P31": "Q5",  # instance of: human
        "P106": "Q36834",  # occupation: music producer
        "P106": "Q177220",  # occupation: DJ
        "P569": "+2002-11-16T00:00:00Z",  # date of birth: November 16, 2002
        "P19": "Q13827",  # place of birth: Kiên Giang Province (Việt Nam)
        "P27": "Q881",  # country of citizenship: Vietnam
        "P937": "Q11816",  # work location: Vietnam
        "P580": "+2002-11-16T00:00:00Z",  # start time: 2002
    },
    "aliases": {
        "vi": ["DJ D.R TheBattery", "DR THE PIN"],
        "en": ["DJ D.R TheBattery", "DR THE PIN"]
    }
}

def create_wikidata_item():
    """Tạo Wikidata item mới"""
    try:
        print("🔄 Bắt đầu kết nối với Wikidata...")
        
        # Tạo item mới
        item = pywikibot.ItemPage(REPO)
        item.editLabels(PERSON_DATA["labels"], summary="Tạo item mới cho nhạc sĩ Việt Nam")
        print(f"✅ Tạo labels thành công")
        
        # Thêm descriptions
        item.editDescriptions(PERSON_DATA["descriptions"], summary="Thêm mô tả")
        print(f"✅ Thêm descriptions thành công")
        
        # Thêm aliases
        item.editAliases(PERSON_DATA["aliases"], summary="Thêm các tên gọi khác")
        print(f"✅ Thêm aliases thành công")
        
        # Thêm claims (properties)
        for prop, value in PERSON_DATA["claims"].items():
            target = pywikibot.ItemPage(REPO, value) if value.startswith("Q") else value
            claim = pywikibot.Claim(REPO, prop)
            
            if isinstance(target, pywikibot.ItemPage):
                claim.setTarget(target)
            else:
                claim.setTarget(pywikibot.WbTime(year=2002, month=11, day=16))
            
            item.addClaim(claim, summary=f"Thêm {prop}")
        
        print(f"✅ Thêm properties thành công")
        print(f"\n🎉 Tạo Wikidata item thành công!")
        print(f"📍 Item ID: {item.id}")
        print(f"🔗 Link: https://www.wikidata.org/wiki/{item.id}")
        
        return item
        
    except Exception as e:
        print(f"❌ Lỗi: {str(e)}")
        return None

def update_wikidata_item(item_id):
    """Cập nhật Wikidata item hiện có"""
    try:
        print(f"🔄 Đang cập nhật item {item_id}...")
        
        item = pywikibot.ItemPage(REPO, item_id)
        item.get()
        
        # Cập nhật labels
        item.editLabels(PERSON_DATA["labels"], summary="Cập nhật labels")
        print(f"✅ Cập nhật labels thành công")
        
        # Cập nhật descriptions
        item.editDescriptions(PERSON_DATA["descriptions"], summary="Cập nhật mô tả")
        print(f"✅ Cập nhật descriptions thành công")
        
        print(f"\n🎉 Cập nhật Wikidata item thành công!")
        print(f"🔗 Link: https://www.wikidata.org/wiki/{item_id}")
        
        return item
        
    except Exception as e:
        print(f"❌ Lỗi: {str(e)}")
        return None

def connect_github_to_wikidata(wikidata_id, github_url):
    """Kết nối GitHub URL với Wikidata item"""
    try:
        print(f"🔗 Kết nối GitHub với Wikidata...")
        
        item = pywikibot.ItemPage(REPO, wikidata_id)
        item.get()
        
        # P1324 = GitHub URL
        claim = pywikibot.Claim(REPO, "P1324")
        claim.setTarget(github_url)
        item.addClaim(claim, summary="Thêm GitHub repository link")
        
        print(f"✅ Kết nối GitHub thành công!")
        print(f"🔗 Wikidata: https://www.wikidata.org/wiki/{wikidata_id}")
        print(f"🔗 GitHub: {github_url}")
        
        return True
        
    except Exception as e:
        print(f"❌ Lỗi: {str(e)}")
        return False

def main():
    """Hàm chính"""
    print("=" * 60)
    print("🌐 WIKIDATA ↔️ GITHUB CONNECTOR")
    print("=" * 60)
    print()
    
    # Lựa chọn thao tác
    print("Chọn thao tác:")
    print("1. Tạo Wikidata item mới")
    print("2. Cập nhật Wikidata item hiện có")
    print("3. Kết nối GitHub với Wikidata")
    print()
    
    choice = input("Nhập lựa chọn (1-3): ").strip()
    
    if choice == "1":
        create_wikidata_item()
    elif choice == "2":
        item_id = input("Nhập Wikidata item ID (ví dụ: Q123): ").strip()
        update_wikidata_item(item_id)
    elif choice == "3":
        item_id = input("Nhập Wikidata item ID: ").strip()
        github_url = "https://github.com/lientannhatduy/Li-n-t-n-nh-t-duy-dj-d.r-thebattery"
        connect_github_to_wikidata(item_id, github_url)
    else:
        print("❌ Lựa chọn không hợp lệ!")

if __name__ == "__main__":
    main()
