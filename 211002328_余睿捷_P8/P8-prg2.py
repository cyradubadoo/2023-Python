#编写程序，分别输入3个字符串，依次验证其是否为有效的中华人民共和国电话号码、中华人民共和国邮政编码和网站网址格式。
# （1）中华人民共和国电话号码必须是8位号码，如果有区号，区号必须是3位。
# （2）中华人民共和国邮政编码必须是6位数字。
# （3）网站网址的正则表示参考：r'^https?://\w+(?:\.[^\.]+)+(?:/.+)*$'

import re

def validate_phone_number(phone_number):
    return re.match(r'^((\d{3}-)?\d{8})$', phone_number) is not None

def validate_postcode(postcode):
    return re.match(r'^\d{6}$', postcode) is not None

def validate_website(website):
    return re.match(r'^https?://\w+(?:.[^.]+)+(?:/.+)*$', website) is not None

phone_number = input("请输入中华人民共和国电话号码：") 
if validate_phone_number(phone_number):
    print("有效的中华人民共和国电话号码") 
else: print("无效的中华人民共和国电话号码")

postcode = input("请输入中华人民共和国邮政编码：")
if validate_postcode(postcode):
    print("有效的中华人民共和国邮政编码")
else: print("无效的中华人民共和国邮政编码")

website = input("请输入网站网址：")
if validate_website(website):
    print("有效的网站网址")
else: print("无效的网站网址")