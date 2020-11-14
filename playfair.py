#playfair 算法
import numpy as np
import math

#先制造矩阵,将key放入矩阵，接着将key以外的字母放入矩阵,返回密钥矩阵
#参数说明：【key：密钥】 【matrix：矩阵】 【alphabet：25个字母,没有J】
def matrix(key):
    matrix=[] #制造矩阵（一维）

    for e in key.upper():#将key放入矩阵
        if e not in matrix:
            matrix.append(e)

    alphabet="ABCDEFGHIKLMNOPQRSTUVWXYZ"
    for e in alphabet:#将key以外的字母放入矩阵
        if e not in matrix:
            matrix.append(e)

    result=np.array(matrix).reshape((5,5))#将matrix转化为二维5*5数组
    return result

#传入明文，对明文进行预处理：
#1.去除空格号 2.重复字符之间加入’X‘ 3.
def message_to_digraphs(message_original):
    message=[]
    for e in message_original:
        message.append(e)

    while ' ' in message:    # 删除空格号
        message.remove(' ')

    #重复字符的处理:在重复字符后加入X
    #参数说明：【i:迭代数字】
    i=0
    for e in range(math.ceil(len(message)/2)):
        if message[i]==message[i+1]:
            message.insert(i+1,'X')
        i=i+2


    #如果明文是奇数个字母，需要在最后加上特殊字母'X'
    if len(message) % 2 == 1:
        message.append('X')

    # 每两个字符为一组
    i = 0
    new = []
    for x in range(1, math.ceil(len(message) / 2 + 1)):
        new.append(message[i:i + 2])
        i = i + 2
    return new

def find_position(key_matrix,letter):
    x=y=0
    for i in range(5):
        for j in range(5):
            if key_matrix[i][j]==letter:
                x=i
                y=j
    return x,y

def encrypt(message,key):
    message=message_to_digraphs(message.upper()) #传入明文
    key_matrix=matrix(key)#返回密钥矩阵
    cipher=[]
    for e in message:
        p1,q1=find_position(key_matrix,e[0])
        p2,q2=find_position(key_matrix,e[1])
        if p1 == p2:#只同行
                    #将会被它们右边的字符分别替代
                    #如果该字符在最右边一列，将会被同行 最左边一列的那个字符代替（其实就是“穿透”过去）
            if q1 == 4:
                q1 = -1
            if q2 == 4:
                q2 = -1
            cipher.append(key_matrix[p1][q1 + 1])
            cipher.append(key_matrix[p1][q2 + 1])
        elif q1 == q2:#只同列
                      #将会被它们下边的字母分别替代
                      #如果该字符在最下面一行，将会被同列 最上边一行的那个字符代替（其实就是“穿透”过去）
            if p1 == 4:
                p1 = -1
            if p2 == 4:
                p2 = -1
            cipher.append(key_matrix[p1 + 1][q1])
            cipher.append(key_matrix[p2 + 1][q2])
        else:#既不同行也不同列
            cipher.append(key_matrix[p1][q2])
            cipher.append(key_matrix[p2][q1])
    return cipher

def cipher_to_digraphs(cipher):
    i=0
    new=[]
    for x in range(math.ceil(len(cipher)/2)):
        new.append(cipher[i:i+2])
        i=i+2
    return new

def decrypt(cipher):
    cipher = cipher_to_digraphs(cipher)
    key_matrix = matrix(key)
    plaintext = []
    for e in cipher:
        p1, q1 = find_position(key_matrix, e[0])
        p2, q2 = find_position(key_matrix, e[1])
        if p1 == p2:
            if q1 == 4:
                q1 = -1
            if q2 == 4:
                q2 = -1
            plaintext.append(key_matrix[p1][q1 - 1])
            plaintext.append(key_matrix[p1][q2 - 1])
        elif q1 == q2:
            if p1 == 4:
                p1 = -1
            if p2 == 4:
                p2 = -1
            plaintext.append(key_matrix[p1 - 1][q1])
            plaintext.append(key_matrix[p2 - 1][q2])
        else:
            plaintext.append(key_matrix[p1][q2])
            plaintext.append(key_matrix[p2][q1])

    for unused in range(len(plaintext)):
        if "X" in plaintext:
            plaintext.remove("X")

    output = ""
    for e in plaintext:
        output += e
    return output.lower()


# 主函数
if __name__ == '__main__':
    print("*****playfair加密*****")
    print("加密请输入D,解密请输入E:")
    user_input = input()
    while (user_input != 'D' and user_input != 'E'):  # 输入合法性检测
        print("输入有误!请重新输入:")
        user_input = input()

    print('请输入密钥，密钥由英文字母组成:')
    key = input()

    if user_input == 'D':  # 加密
        print('请输入明文:')
        message = input()
        print("Encrypting: \n" + "Message: " + message)
        print("Break the message into digraphs: ")
        print(message_to_digraphs(message))
        print("Matrix: ")
        print(matrix(key))
        print("Cipher: ")
        print(encrypt(message,key))
    else:  # 解密
        print('请输入密文:')
        cipher = input()
        print("\nDecrypting: \n" + "Cipher: " + cipher)
        print("Plaintext:")
        print(decrypt(cipher))