import json
from http.cookies import SimpleCookie

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

def json_to_netscape(json_file, output_file):
    with open(json_file, 'r', encoding='utf-8') as f:
        cookies = json.load(f)

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write("# Netscape HTTP Cookie File\n")
        f.write("# https://www.netscape.com\n")
        f.write("# This is a generated file!\n")

        for cookie in cookies:
            for c in cookie.get('cookies', []):
                domain = c['domain']
                path = c.get('path', '/')
                expiry = c['expiry']
                secure = 'TRUE' if c.get('secure', False) else 'FALSE'
                httponly = 'TRUE' if c.get('httpOnly', False) else 'FALSE'
                name = c['name']
                value = c['value']

                f.write(f"{domain}\tTRUE\t{path}\t{secure}\t{expiry}\t{name}\t{value}\n")

    print(f"Cookies successfully converted to Netscape format in {output_file}")
    

# 使用示例:
if __name__ == "__main__":
    cookie_header = load_cookies_to_header()
    print(f"Cookie header: {cookie_header}")
    
    json_to_netscape('cookie.json', 'cookies.txt')