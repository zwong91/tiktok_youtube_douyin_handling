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
            # 保持domain的点号前缀
            domain = cookie.get('domain', '')
            
            # 设置正确的字段值
            path = cookie.get('path', '/')
            secure = "TRUE" if cookie.get('secure', False) else "FALSE"
            expiry = int(cookie.get('expirationDate', 0))
            name = cookie.get('name', '')
            value = cookie.get('value', '')
            
            # domain_flag要和domain的点号对应
            domain_flag = "TRUE" if domain.startswith('.') else "FALSE"
            
            # 按Netscape格式写入: domain domain-flag path secure expiry name value
            line = f"{domain}\t{domain_flag}\t{path}\t{secure}\t{expiry}\t{name}\t{value}\n"
            f.write(line)

    print(f"已生成cookie文件: {output_file}")
    

# 使用示例:
if __name__ == "__main__":
    cookie_header = load_cookies_to_header()
    print(f"Cookie header: {cookie_header}")
    
    json_to_netscape('cookie.json', 'cookies.txt')