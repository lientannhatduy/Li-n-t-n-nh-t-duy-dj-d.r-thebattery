#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
WIKIDATA AUTHENTICATION & USAGE GUIDE
Hướng dẫn xác thực và sử dụng script kết nối Wikidata
Updated with improved structure, examples, and best practices
"""

# ============================================================
# 📚 HƯỚNG DẪN SỬ DỤNG - WIKIDATA CONNECTOR
# ============================================================

"""
╔════════════════════════════════════════════════════════════╗
║           WIKIDATA CONNECTOR - COMPLETE GUIDE              ║
║      Kết nối GitHub với Wikidata - Hướng dẫn Đầy Đủ      ║
╚════════════════════════════════════════════════════════════╝

📖 TABLE OF CONTENTS
═══════════════════
1. Installation & Setup
2. Authentication Methods
3. Running the Script
4. Core Features
5. Credentials & Security
6. Wikidata Properties Reference
7. Usage Examples
8. Troubleshooting
9. FAQ
10. Resources & Support


1️⃣ INSTALLATION & SETUP
════════════════════════

STEP 1: Install Dependencies
───────────────────────────
pip install pywikibot requests

Hoặc từ requirements.txt:

pip install -r requirements.txt

STEP 2: Verify Installation
───────────────────────────
python3 -c "import pywikibot; print('✅ Pywikibot installed successfully')"

STEP 3: Create Wikidata Account (if needed)
──────────────────────────────────────────
Visit: https://www.wikidata.org/wiki/Special:CreateAccount
- Choose a username
- Set a strong password
- Verify your email
- Enable 2FA (recommended)


2️⃣ AUTHENTICATION METHODS
═════════════════════════

Choose ONE method based on your needs:

┌─────────────────────────────────────────────────────────────┐
│ A) USERNAME & PASSWORD (Simple)                             │
├─────────────────────────────────────────────────────────────┤
│ ✅ Pros:                                                     │
│   - No browser required                                     │
│   - Quickest setup                                          │
│   - Credentials cached locally                             │
│                                                             │
│ ❌ Cons:                                                     │
│   - Password stored as plain text                          │
│   - Less secure                                            │
│   - Not recommended for shared systems                     │
│                                                             │
│ 📍 Best for: Personal development, local testing           │
└─────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────┐
│ B) OAUTH 2.0 (Recommended)                                  │
├─────────────────────────────────────────────────────────────┤
│ ✅ Pros:                                                     │
│   - Industry-standard security                             │
│   - Password never stored                                  │
│   - Tokens are revocable                                   │
│   - Better for team environments                           │
│                                                             │
│ ❌ Cons:                                                     │
│   - Requires browser interaction                           │
│   - Slightly more setup                                    │
│                                                             │
│ 📍 Best for: Production, shared accounts, CI/CD            │
└─────────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────────┐
│ C) SAVED CREDENTIALS (Fastest)                              │
├─────────────────────────────────────────────────────────────┤
│ ✅ Pros:                                                     │
│   - Reuse existing authentication                          │
│   - Fastest startup                                        │
│   - No re-authentication needed                            │
│                                                             │
│ ❌ Cons:                                                     │
│   - Requires prior authentication                          │
│   - Inherits security of stored method                     │
│                                                             │
│ 📍 Best for: Repeated tasks, automation                    │
└─────────────────────────────────────────────────────────────┘


3️⃣ RUNNING THE SCRIPT
═════════════════════

Basic Usage:
───────────
python3 connect_wikidata.py

What Happens Next:
──────────────────
1. Script displays authentication menu
2. Choose your authentication method (1, 2, 3, or 4)
3. Enter credentials or approve OAuth
4. Access main menu with operations
5. Select operation: create, update, or link

Troubleshooting Startup Issues:
───────────────────────────────
❌ "ModuleNotFoundError: No module named 'pywikibot'"
→ Run: pip install pywikibot requests

❌ "Permission denied"
→ Ensure .wikidata_config.json has correct permissions
→ Run: chmod 600 .wikidata_config.json

❌ "No such file or directory"
→ Run script from repository root directory
→ Check: pwd should show the correct path


4️⃣ CORE FEATURES
════════════════

✅ CREATE WIKIDATA ITEM
──────────────────────
What it does:
  - Creates a new Wikidata item (Q-number)
  - Adds labels, descriptions, and aliases
  - Automatically populates with pre-configured data
  - Returns the new item ID

When to use:
  - First time creating a Wikipedia page for someone
  - Migrating profile data to Wikidata
  - Creating structured data for artists/creators

Output:
  Item ID: Q12345
  URL: https://www.wikidata.org/wiki/Q12345


✅ UPDATE WIKIDATA ITEM
──────────────────────
What it does:
  - Modifies existing item data
  - Updates labels and descriptions
  - Adds or changes properties
  - Maintains version history

When to use:
  - Correcting information
  - Adding new properties
  - Updating after item creation

Requirements:
  - Must have existing Wikidata item ID (Q-number)
  - Account must have edit permissions


✅ LINK GITHUB TO WIKIDATA
──────────────────────────
What it does:
  - Adds GitHub repository link to Wikidata item
  - Uses property P1324 (GitHub URL)
  - Creates persistent connection between profiles

When to use:
  - Documenting software projects
  - Linking artist/creator profiles to code
  - Creating comprehensive biographical data

Data structure:
  P1324 = GitHub URL
  Example: https://github.com/lientannhatduy/Li-n-t-n-nh-t-duy-dj-d.r-thebattery


5️⃣ CREDENTIALS & SECURITY
═══════════════════════════

File Location:
──────────────
.wikidata_config.json (in repository root)

File Contents:
──────────────
{
  "username": "your_wikidata_username",
  "password": "your_password"
}

Security Best Practices:
────────────────────────
✅ DO:
  ✓ Use OAuth 2.0 when possible
  ✓ Add .wikidata_config.json to .gitignore
  ✓ Set file permissions to 600 (chmod 600)
  ✓ Use strong passwords (16+ characters)
  ✓ Enable 2FA on your Wikidata account
  ✓ Rotate credentials regularly
  ✓ Clear credentials when done (option 4)

❌ DON'T:
  ✗ Commit credentials to Git
  ✗ Share .wikidata_config.json
  ✗ Use weak passwords
  ✗ Store credentials in environment variables (plain text)
  ✗ Use production credentials for testing

Rotating Credentials:
─────────────────────
1. Choose option 4 in auth menu to clear old credentials
2. Change password on Wikidata.org
3. Re-authenticate with new password
4. Old .wikidata_config.json is deleted


6️⃣ WIKIDATA PROPERTIES REFERENCE
════════════════════════════════

Common Properties Used:
──────────────────────

IDENTITY
┌─────┬──────────────────────────────────┐
│ P31 │ instance of (e.g., Q5 = human)   │
│ P106│ occupation (e.g., Q36834 = music │
│     │  producer, Q177220 = DJ)         │
└─────┴──────────────────────────────────┘

BIOGRAPHICAL
┌─────┬──────────────────────────────────┐
│ P569│ date of birth                    │
│ P570│ date of death                    │
│ P19 │ place of birth                   │
│ P20 │ place of death                   │
└─────┴──────────────────────────────────┘

RELATIONS & IDENTITY
┌──────┬────────────────────────────────┐
│ P27  │ country of citizenship          │
│ P937 │ work location                   │
│ P735 │ given name                      │
│ P734 │ family name                     │
└──────┴────────────────────────────────┘

EXTERNAL LINKS
┌──────┬────────────────────────────────┐
│ P1324│ GitHub URL                      │
│ P2397│ YouTube channel ID              │
│ P856 │ official website                │
│ P2888│ exact match                     │
└──────┴────────────────────────────────┘

Finding More Properties:
────────────────────────
Visit: https://www.wikidata.org/wiki/Wikidata:List_of_properties
Search by name or ID to find additional properties.

Common Item IDs:
────────────────
Q5       = human (Con người)
Q36834   = music producer (Nhà sản xuất nhạc)
Q177220  = DJ (Nhạc sĩ DJ)
Q13827   = Kiên Giang Province (Tỉnh Kiên Giang)
Q881     = Vietnam (Việt Nam)
Q11816   = Vietnam (Đất nước Việt Nam)

Find more: https://www.wikidata.org/w/api.php?action=wbsearchentities&search=TERM&language=en&format=json


7️⃣ USAGE EXAMPLES
═════════════════

EXAMPLE 1: First Time Setup
──────────────────────────
$ python3 connect_wikidata.py

🔐 WIKIDATA AUTHENTICATION
Choose authentication:
1. Username & Password
2. OAuth 2.0
3. Saved credentials
4. Clear saved credentials
0. Exit

→ Enter: 1
→ Username: your_username
→ Password: ••••••••

✅ Login successful!

🌐 WIKIDATA ↔️ GITHUB CONNECTOR
1. Create new item
2. Update existing item
3. Link GitHub
4. Back to auth
0. Exit

→ Enter: 1
→ Creating new Wikidata item...
✅ Success! Item ID: Q123456
🔗 Link: https://www.wikidata.org/wiki/Q123456


EXAMPLE 2: Update Item Information
───────────────────────────────────
→ Enter: 2 (Update item)
→ Item ID: Q123456
→ Updating item Q123456...
✅ Labels updated
✅ Descriptions updated
✅ Complete!


EXAMPLE 3: Link GitHub Repository
──────────────────────────────────
→ Enter: 3 (Link GitHub)
→ Item ID: Q123456
→ Linking GitHub repository...
✅ GitHub link added!
🔗 Repository: https://github.com/lientannhatduy/...
🔗 Wikidata: https://www.wikidata.org/wiki/Q123456


8️⃣ TROUBLESHOOTING
═══════════════════

Authentication Issues
─────────────────────

❌ "Login failed" or "Invalid credentials"
→ Verify username and password at https://www.wikidata.org/
→ Check for typos in username
→ Ensure caps lock is off
→ Try OAuth 2.0 instead

❌ "Two-factor authentication required"
→ Use OAuth 2.0 method (handles 2FA automatically)
→ Or disable 2FA temporarily for password auth

❌ "Connection timeout"
→ Check internet connection
→ Try again in a few minutes
→ Check Wikidata status: https://www.wikidata.org/wiki/Wikidata:Status


Item Operations
───────────────

❌ "Item not found"
→ Verify item ID format: Q + numbers only
→ Check if item exists: https://www.wikidata.org/wiki/Q123456
→ Ensure correct item ID copied

❌ "Permission denied"
→ Account needs edit permissions
→ Verify email on Wikidata
→ Wait 4 days if new account (anti-spam)
→ Check auto-confirmed user status

❌ "Item already exists"
→ Search Wikidata first: https://www.wikidata.org/wiki/Special:Search
→ Update existing item instead
→ Merge duplicates if needed


File Issues
───────────

❌ ".wikidata_config.json: Permission denied"
→ Fix permissions: chmod 600 .wikidata_config.json
→ Check file ownership: ls -la .wikidata_config.json
→ Delete and re-authenticate if needed

❌ "Cannot write config file"
→ Check directory permissions: chmod 755 .
→ Ensure disk space available
→ Try sudo if necessary (not recommended)


9️⃣ FREQUENTLY ASKED QUESTIONS
══════════════════════════════

Q: How long do OAuth tokens last?
A: OAuth tokens don't expire in Pywikibot. They remain valid until
   revoked manually or if Wikidata invalidates them for security.

Q: Can I use this script with bot accounts?
A: Yes! Bot accounts are recommended for automated tasks.
   Flag your account as a bot at:
   https://www.wikidata.org/wiki/Wikidata:Bots

Q: What if I forget my Wikidata password?
A: Reset it at: https://www.wikidata.org/wiki/Special:ChangePassword
   Then clear credentials (option 4) and re-authenticate.

Q: Can multiple users share the same script?
A: Not recommended. Each user should:
   1. Have their own Wikidata account
   2. Authenticate separately
   3. Store credentials in separate files

Q: How do I handle errors in batch operations?
A: The script includes error handling for each operation.
   Check logs for specific failures and retry individually.

Q: Can I undo changes made through this script?
A: Yes! Wikidata maintains full version history.
   Revert changes at: https://www.wikidata.org/wiki/ITEM_ID

Q: Is this script production-ready?
A: Yes, with proper credentials management and error handling.
   Test thoroughly with test items first (create on
   https://test.wikidata.org first).


🔟 RESOURCES & SUPPORT
══════════════════════

Official Documentation
──────────────────────
📖 Wikidata Main Page
   https://www.wikidata.org/wiki/Wikidata:Main_Page

📖 Wikidata Properties List
   https://www.wikidata.org/wiki/Wikidata:List_of_properties

📖 Pywikibot Documentation
   https://doc.wikimedia.org/pywikibot/master/


Developer Guides
────────────────
🔧 Pywikibot Getting Started
   https://www.mediawiki.org/wiki/Manual:Pywikibot/Getting_started

🔧 Wikidata for Software Developers
   https://www.wikidata.org/wiki/Wikidata:Data_access


Community & Support
───────────────────
💬 Wikidata Requests for Help
   https://www.wikidata.org/wiki/Wikidata:Requests_for_help

💬 Wikidata Discord Community
   https://discord.gg/wikimedia

💬 Pywikibot Issues on Gerrit
   https://gerrit.wikimedia.org/r/#/q/project:pywikibot/core


GitHub & This Project
─────────────────────
📦 This Repository
   https://github.com/lientannhatduy/Li-n-t-n-nh-t-duy-dj-d.r-thebattery

🐛 Report Issues
   https://github.com/lientannhatduy/Li-n-t-n-nh-t-duy-dj-d.r-thebattery/issues

📝 Contributing
   https://github.com/lientannhatduy/Li-n-t-n-nh-t-duy-dj-d.r-thebattery#contributing


Testing Resources
─────────────────
🧪 Wikidata Sandbox (for testing)
   https://www.wikidata.org/wiki/Wikidata:Sandbox

🧪 Test.wikidata.org (isolated testing)
   https://test.wikidata.org/wiki/Wikidata:Main_Page


═══════════════════════════════════════════════════════════════

                    QUICK START CHECKLIST

✓ Install: pip install -r requirements.txt
✓ Create: Wikidata account (if needed)
✓ Run: python3 connect_wikidata.py
✓ Choose: Authentication method
✓ Select: Operation (create/update/link)
✓ Monitor: Check https://www.wikidata.org/wiki/Q[YOUR_ID]

═══════════════════════════════════════════════════════════════
"""

# ============================================================
# QUICK START EXAMPLE
# ============================================================

def quick_start_example():
    """
    Ví dụ nhanh để bắt đầu - Quick start to get going
    """
    
    print("""
    ╔════════════════════════════════════════════════════════════╗
    ║         QUICK START - BẮTĐẦU NHANH (5 PHÚT)               ║
    ╚════════════════════════════════════════════════════════════╝
    
    ⚡ BƯỚC 1: Cài đặt (Install)
    ──────────────────────────
    $ pip install pywikibot requests
    
    ⚡ BƯỚC 2: Chạy script (Run)
    ──────────────────────────
    $ python3 connect_wikidata.py
    
    ⚡ BƯỚC 3: Chọn xác thực (Authenticate)
    ─────────────────────────────────────
    Menu will show:
    1. Username & Password (simple)
    2. OAuth 2.0 (recommended)
    3. Saved credentials (fast)
    
    Choose option 1 or 2
    
    ⚡ BƯỚC 4: Nhập thông tin (Enter credentials)
    ──────────────────────────────────────────
    Username: your_wikidata_username
    Password: ••••••••••
    
    ⚡ BƯỚC 5: Chọn thao tác (Select operation)
    ────────────────────────────────────────
    1. Tạo item mới (Create new item)
    2. Cập nhật item (Update item)
    3. Kết nối GitHub (Link GitHub)
    
    Choose based on what you need
    
    ⚡ BƯỚC 6: Nhập thông tin (Provide info)
    ──────────────────────────────────────
    Follow prompts to complete operation
    
    ✅ HOÀN TẤT! (Done!)
    ──────────────────
    Item created: https://www.wikidata.org/wiki/Q[YOUR_ID]
    
    """)

if __name__ == "__main__":
    quick_start_example()
