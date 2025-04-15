import json

def load_cookies_to_header():
    try:
        with open('cookie.json', 'r') as f:
            cookies = json.load(f)
        
        cookie_parts = []
        for cookie in cookies:
            if 'name' in cookie and 'value' in cookie:
                cookie_parts.append(f"{cookie['name']}={cookie['value']}")
        
        return '; '.join(cookie_parts)
    except Exception as e:
        print(f"读取cookie文件失败: {str(e)}")
        return ""

# 使用示例:
if __name__ == "__main__":
    cookie_header = load_cookies_to_header()
    print(f"Cookie header: {cookie_header}")