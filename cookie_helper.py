import json
from datetime import datetime

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
        f.write("# https://curl.haxx.se/rfc/cookie_spec.html\n")
        f.write("# This is a generated file!  Do not edit.\n\n")

        for cookie in cookies:
            # 确保domain格式正确
            domain = cookie.get('domain', '')
            if domain.startswith('.'):
                domain = domain[1:]
            
            # 其他字段
            http_only = "TRUE" if cookie.get('httpOnly', False) else "FALSE"
            path = cookie.get('path', '/')
            secure = "TRUE" if cookie.get('secure', False) else "FALSE"
            expiry = int(cookie.get('expirationDate', 0))
            name = cookie.get('name', '')
            value = cookie.get('value', '')
            
            # 正确的Netscape格式: domain include_subdomains path secure expiry name value
            line = f"{domain}\tTRUE\t{path}\t{secure}\t{expiry}\t{name}\t{value}\n"
            f.write(line)

    print(f"已生成cookie文件: {output_file}")
    

# 使用示例:
if __name__ == "__main__":
    cookie_header = load_cookies_to_header()
    print(f"Cookie header: {cookie_header}")
    
    json_to_netscape('cookie.json', 'cookies.txt')