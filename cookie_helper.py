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
    # 读取JSON格式的cookie
    with open(json_file, 'r', encoding='utf-8') as f:
        cookies = json.load(f)

    # 写入Netscape格式
    with open(output_file, 'w', encoding='utf-8') as f:
        # 写入Netscape cookie文件头
        f.write("# Netscape HTTP Cookie File\n")
        f.write("# https://curl.haxx.se/rfc/cookie_spec.html\n")
        f.write("# This is a generated file!  Do not edit.\n\n")

        for cookie in cookies:
            domain = cookie.get('domain', '')
            domain_flag = "TRUE" if cookie.get('hostOnly', False) else "FALSE"
            path = cookie.get('path', '/')
            secure = "TRUE" if cookie.get('secure', False) else "FALSE"
            expiry = int(cookie.get('expirationDate', 0))
            name = cookie.get('name', '')
            value = cookie.get('value', '')

            # 格式: domain domain_flag path secure expiry name value
            line = f"{domain}\t{domain_flag}\t{path}\t{secure}\t{expiry}\t{name}\t{value}\n"
            f.write(line)

    print(f"Cookie文件已转换: {output_file}")
    

# 使用示例:
if __name__ == "__main__":
    cookie_header = load_cookies_to_header()
    print(f"Cookie header: {cookie_header}")
    
    json_to_netscape('cookie.json', 'cookies.txt')