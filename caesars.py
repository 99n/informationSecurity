# 凯撒密码算法:采用的是最经典的移位13位
def caesars_encrypt(plain_text):
    res=""
    plain_text=plain_text.upper()
    for i in plain_text:
        i=ord(i)-13
        res=res+chr(i)
    return res

def caesars_decrypt(chiper_text):
    res=''
    chiper_text=chiper_text.upper()
    for i in chiper_text:
        i=ord(i)+13
        res=res+chr(i)
    return res

if __name__=='__main__':
    print("*****凯撒加密*****")
    print("加密请输入D,解密请输入E:")
    user_input=input()
    while (user_input != 'D' and user_input != 'E'):  # 输入合法性检测
        print("输入有误!请重新输入:")
        user_input = input()
    if user_input == 'D':  # 加密
        print('请输入明文:')
        message = input()
        print("凯撒加密结果: \n" + "明文: " + message)
        result_cipher=caesars_encrypt(message)
        print("密文: "+result_cipher)

    else:  # 解密
        print('请输入密文:')
        cipher = input()
        print("凯撒解密结果: \n" + "密文: " + cipher)
        result_plain=caesars_decrypt(cipher)
        print("明文: "+result_plain)
