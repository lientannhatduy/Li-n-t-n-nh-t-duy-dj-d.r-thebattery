#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Wikipedia Bot - Tìm kiếm và lấy thông tin từ Wikipedia
"""

import wikipedia
import sys

def search_wikipedia(query, language='vi'):
    """
    Tìm kiếm thông tin trên Wikipedia
    
    Args:
        query (str): Từ khóa tìm kiếm
        language (str): Ngôn ngữ (mặc định: 'vi' - Tiếng Việt)
    
    Returns:
        dict: Kết quả tìm kiếm
    """
    wikipedia.set_lang(language)
    
    try:
        # Tìm kiếm
        print(f"\n🔍 Đang tìm kiếm: '{query}' trên Wikipedia ({language})...")
        
        # Lấy trang Wikipedia
        page = wikipedia.page(query, auto_suggest=True)
        
        result = {
            'title': page.title,
            'url': page.url,
            'summary': page.summary[:500] + "...",  # Lấy 500 ký tự đầu
            'content': page.content,
            'links': page.links[:10]  # Lấy 10 link đầu tiên
        }
        
        return result
    
    except wikipedia.exceptions.DisambiguationError as e:
        print(f"⚠️ Tìm thấy nhiều kết quả có liên quan:")
        for option in e.options[:5]:
            print(f"  - {option}")
        return None
    
    except wikipedia.exceptions.PageError:
        print(f"❌ Không tìm thấy trang: '{query}'")
        return None
    
    except Exception as e:
        print(f"❌ Lỗi: {str(e)}")
        return None

def display_result(result):
    """Hiển thị kết quả tìm kiếm"""
    if not result:
        return
    
    print("\n" + "="*60)
    print(f"📄 Tiêu đề: {result['title']}")
    print(f"🔗 URL: {result['url']}")
    print("="*60)
    print(f"\n📝 Tóm tắt:\n{result['summary']}")
    print("\n" + "="*60)

def interactive_mode():
    """Chế độ tương tác - người dùng nhập từ khóa"""
    print("="*60)
    print("🤖 WIKIPEDIA BOT - Tìm kiếm thông tin Wikipedia")
    print("="*60)
    print("Nhập từ khóa để tìm kiếm (hoặc 'exit' để thoát)")
    print()
    
    while True:
        try:
            query = input("🔍 Nhập từ khóa tìm kiếm: ").strip()
            
            if query.lower() == 'exit':
                print("👋 Tạm biệt!")
                break
            
            if not query:
                print("⚠️ Vui lòng nhập từ khóa")
                continue
            
            result = search_wikipedia(query, language='vi')
            display_result(result)
            
        except KeyboardInterrupt:
            print("\n👋 Tạm biệt!")
            break
        except Exception as e:
            print(f"❌ Lỗi: {str(e)}")

def main():
    """Hàm chính"""
    if len(sys.argv) > 1:
        # Nếu có argument, tìm kiếm từ argument đó
        query = ' '.join(sys.argv[1:])
        result = search_wikipedia(query, language='vi')
        display_result(result)
    else:
        # Nếu không có argument, chạy chế độ tương tác
        interactive_mode()

if __name__ == '__main__':
    main()
