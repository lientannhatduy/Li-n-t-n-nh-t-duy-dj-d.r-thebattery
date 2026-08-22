#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Script kết nối GitHub với Wikidata (có xác thực)
Tạo/cập nhật Wikidata item cho Liên Tấn Nhật Duy
Hỗ trợ xác thực OAuth và Username/Password
"""

import pywikibot
from pywikibot import pagegenerators, config
import requests
import json
import os
from datetime import datetime
from pathlib import Path

# ============= CẤU HÌNH XÁC THỰC =============

class WikidataAuthenticator:
    """Xác thực với Wikidata"""
    
    def __init__(self):
        self.site = None
        self.repo = None
        self.config_file = ".wikidata_config.json"
        
    def load_credentials(self):
        """Tải thông tin xác thực từ file"""
        if os.path.exists(self.config_file):
            try:
                with open(self.config_file, 'r') as f:
                    creds = json.load(f)
                print(f"✅ Tải thông tin xác thực từ {self.config_file}")
                return creds
            except Exception as e:
                print(f"❌ Lỗi khi tải file: {str(e)}")
                return None
        return None
    
    def save_credentials(self, username=None, password=None, oauth_token=None):
        """Lưu thông tin xác thực vào file"""
        creds = {}
        if username:
            creds['username'] = username
        if password:
            creds['password'] = password
        if oauth_token:
            creds['oauth_token'] = oauth_token
        
        try:
            with open(self.config_file, 'w') as f:
                json.dump(creds, f, indent=2)
            os.chmod(self.config_file, 0o600)  # Chỉ owner có thể đọc
            print(f"✅ Lưu thông tin xác thực vào {self.config_file}")
            return True
        except Exception as e:
            print(f"❌ Lỗi khi lưu file: {str(e)}")
            return False
    
    def authenticate_with_username(self, username, password):
        """Xác thực bằng tên đăng nhập và mật khẩu"""
        try:
            print("🔐 Đang xác thực với Wikidata (Username/Password)...")
            
            # Cấu hình cho Pywikibot
            config.usernames['wikidata']['wikidata'] = username
            config.passwords['wikidata']['wikidata'] = password
            
            # Kết nối
            self.site = pywikibot.Site("wikidata", "wikidata")
            self.repo = self.site.data_repository()
            
            # Kiểm tra xác thực
            if self.site.user():
                print(f"✅ Đăng nhập thành công với tài khoản: {self.site.user()}")
                self.save_credentials(username=username, password=password)
                return True
            else:
                print("❌ Đăng nhập thất bại!")
                return False
                
        except Exception as e:
            print(f"❌ Lỗi xác thực: {str(e)}")
            return False
    
    def authenticate_with_oauth(self):
        """Xác thực bằng OAuth 2.0"""
        try:
            print("🔐 Đang xác thực với Wikidata (OAuth 2.0)...")
            print("\n⚠️  Bạn sẽ được chuyển hướng đến trang xác thực Wikidata")
            print("Vui lòng đăng nhập và cấp quyền truy cập")
            print()
            
            # Pywikibot tự động xử lý OAuth flow
            self.site = pywikibot.Site("wikidata", "wikidata")
            self.repo = self.site.data_repository()
            
            # Kiểm tra xác thực
            if self.site.user():
                print(f"✅ Xác thực OAuth thành công với tài khoản: {self.site.user()}")
                return True
            else:
                print("❌ Xác thực OAuth thất bại!")
                return False
                
        except Exception as e:
            print(f"❌ Lỗi OAuth: {str(e)}")
            return False
    
    def authenticate_with_saved_credentials(self):
        """Xác thực bằng thông tin đã lưu"""
        try:
            print("🔐 Đang xác thực bằng thông tin đã lưu...")
            creds = self.load_credentials()
            
            if not creds:
                print("❌ Không tìm thấy thông tin xác thực đã lưu")
                return False
            
            if 'username' in creds and 'password' in creds:
                return self.authenticate_with_username(creds['username'], creds['password'])
            else:
                print("❌ Thông tin xác thực không đầy đủ")
                return False
                
        except Exception as e:
            print(f"❌ Lỗi: {str(e)}")
            return False
    
    def clear_credentials(self):
        """Xóa thông tin xác thực đã lưu"""
        try:
            if os.path.exists(self.config_file):
                os.remove(self.config_file)
                print("✅ Xóa thông tin xác thực thành công")
                return True
        except Exception as e:
            print(f"❌ Lỗi khi xóa: {str(e)}")
            return False

# ============= DỮ LIỆU NGƯỜI DÙNG =============

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
        "P569": "+2002-11-16T00:00:00Z",  # date of birth: November 16, 2002
        "P19": "Q13827",  # place of birth: Kiên Giang Province
        "P27": "Q881",  # country of citizenship: Vietnam
        "P937": "Q11816",  # work location: Vietnam
    },
    "aliases": {
        "vi": ["DJ D.R TheBattery", "DR THE PIN"],
        "en": ["DJ D.R TheBattery", "DR THE PIN"]
    }
}

# ============= CÁC HÀM CHÍNH =============

def create_wikidata_item(repo):
    """Tạo Wikidata item mới"""
    try:
        print("\n📝 Bắt đầu tạo Wikidata item mới...")
        
        # Tạo item mới
        item = pywikibot.ItemPage(repo)
        item.editLabels(PERSON_DATA["labels"], summary="[GitHub] Tạo item mới cho nhạc sĩ Việt Nam")
        print(f"✅ Tạo labels thành công")
        
        # Thêm descriptions
        item.editDescriptions(PERSON_DATA["descriptions"], summary="[GitHub] Thêm mô tả")
        print(f"✅ Thêm descriptions thành công")
        
        # Thêm aliases
        item.editAliases(PERSON_DATA["aliases"], summary="[GitHub] Thêm các tên gọi khác")
        print(f"✅ Thêm aliases thành công")
        
        # Thêm claims (properties)
        for prop, value in PERSON_DATA["claims"].items():
            try:
                if value.startswith("Q"):
                    target = pywikibot.ItemPage(repo, value)
                    claim = pywikibot.Claim(repo, prop)
                    claim.setTarget(target)
                else:
                    claim = pywikibot.Claim(repo, prop)
                    claim.setTarget(pywikibot.WbTime(year=2002, month=11, day=16))
                
                item.addClaim(claim, summary=f"[GitHub] Thêm {prop}")
            except Exception as e:
                print(f"⚠️  Lỗi khi thêm {prop}: {str(e)}")
                continue
        
        print(f"\n🎉 Tạo Wikidata item thành công!")
        print(f"📍 Item ID: {item.id}")
        print(f"🔗 Link: https://www.wikidata.org/wiki/{item.id}")
        
        return item
        
    except Exception as e:
        print(f"❌ Lỗi: {str(e)}")
        return None

def update_wikidata_item(repo, item_id):
    """Cập nhật Wikidata item hiện có"""
    try:
        print(f"\n♻️ Đang cập nhật item {item_id}...")
        
        item = pywikibot.ItemPage(repo, item_id)
        item.get()
        
        # Cập nhật labels
        item.editLabels(PERSON_DATA["labels"], summary="[GitHub] Cập nhật labels")
        print(f"✅ Cập nhật labels thành công")
        
        # Cập nhật descriptions
        item.editDescriptions(PERSON_DATA["descriptions"], summary="[GitHub] Cập nhật mô tả")
        print(f"✅ Cập nhật descriptions thành công")
        
        print(f"\n🎉 Cập nhật Wikidata item thành công!")
        print(f"🔗 Link: https://www.wikidata.org/wiki/{item_id}")
        
        return item
        
    except Exception as e:
        print(f"❌ Lỗi: {str(e)}")
        return None

def connect_github_to_wikidata(repo, wikidata_id):
    """Kết nối GitHub URL với Wikidata item"""
    try:
        print(f"\n🔗 Kết nối GitHub với Wikidata...")
        
        item = pywikibot.ItemPage(repo, wikidata_id)
        item.get()
        
        github_url = "https://github.com/lientannhatduy/Li-n-t-n-nh-t-duy-dj-d.r-thebattery"
        
        # P1324 = GitHub URL
        claim = pywikibot.Claim(repo, "P1324")
        claim.setTarget(github_url)
        item.addClaim(claim, summary="[GitHub] Thêm GitHub repository link")
        
        print(f"✅ Kết nối GitHub thành công!")
        print(f"🔗 Wikidata: https://www.wikidata.org/wiki/{wikidata_id}")
        print(f"🔗 GitHub: {github_url}")
        
        return True
        
    except Exception as e:
        print(f"❌ Lỗi: {str(e)}")
        return False

def show_authentication_menu():
    """Hiển thị menu xác thực"""
    print("\n" + "=" * 60)
    print("🔐 WIKIDATA AUTHENTICATION")
    print("=" * 60)
    print("Chọn phương thức xác thực:")
    print("1. Xác thực bằng tên đăng nhập & mật khẩu")
    print("2. Xác thực bằng OAuth 2.0")
    print("3. Sử dụng thông tin đã lưu")
    print("4. Xóa thông tin xác thực đã lưu")
    print("0. Thoát")
    print()

def show_main_menu():
    """Hiển thị menu chính"""
    print("\n" + "=" * 60)
    print("🌐 WIKIDATA ↔️ GITHUB CONNECTOR")
    print("=" * 60)
    print("Chọn thao tác:")
    print("1. Tạo Wikidata item mới")
    print("2. Cập nhật Wikidata item hiện có")
    print("3. Kết nối GitHub với Wikidata")
    print("4. Quay lại menu xác thực")
    print("0. Thoát")
    print()

def main():
    """Hàm chính"""
    authenticator = WikidataAuthenticator()
    authenticated = False
    
    while True:
        show_authentication_menu()
        auth_choice = input("Nhập lựa chọn (0-4): ").strip()
        
        if auth_choice == "1":
            username = input("Nhập tên đăng nhập Wikidata: ").strip()
            password = input("Nhập mật khẩu: ").strip()
            authenticated = authenticator.authenticate_with_username(username, password)
            
        elif auth_choice == "2":
            authenticated = authenticator.authenticate_with_oauth()
            
        elif auth_choice == "3":
            authenticated = authenticator.authenticate_with_saved_credentials()
            
        elif auth_choice == "4":
            authenticator.clear_credentials()
            continue
            
        elif auth_choice == "0":
            print("👋 Tạm biệt!")
            return
        
        else:
            print("❌ Lựa chọn không hợp lệ!")
            continue
        
        if authenticated:
            # Menu chính
            while True:
                show_main_menu()
                choice = input("Nhập lựa chọn (0-4): ").strip()
                
                if choice == "1":
                    create_wikidata_item(authenticator.repo)
                    
                elif choice == "2":
                    item_id = input("Nhập Wikidata item ID (ví dụ: Q123): ").strip()
                    update_wikidata_item(authenticator.repo, item_id)
                    
                elif choice == "3":
                    item_id = input("Nhập Wikidata item ID: ").strip()
                    connect_github_to_wikidata(authenticator.repo, item_id)
                    
                elif choice == "4":
                    break
                    
                elif choice == "0":
                    print("👋 Tạm biệt!")
                    return
                    
                else:
                    print("❌ Lựa chọn không hợp lệ!")

if __name__ == "__main__":
    main()
