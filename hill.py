import numpy as np

#生成随机密钥矩阵randomKey
randomKey=np.random.randint(0,3,(3,3))
#随机密钥矩阵randomKey的逆矩阵_randomKey
#需要注意的是逆矩阵的元素不可以为负数，若存在负数，则将所有元素+26的若干倍，再mod26，得到全为正整数的逆矩阵
_randomKey=np.linalg.inv(randomKey)#逆矩阵
for i in range(3):
    for j in range(3):
        if _randomKey[i][j] < 0:
            _randomKey[i][j]=_randomKey[i][j]+26

#randomKey=[[1,2,3],[1,1,2],[0,1,2]]
#_randomKey=[[0,1,25],[2,24,25],[25,1,1]]

# 明文plain_text,明文字母在字母表中的索引plain_text_index
# 输入明文。返回加密后的密文
def hillEncrypt(plain_text):
    # 不足三个时补字母X
    if len(plain_text) % 3 == 1:
        plain_text = plain_text + 'XX'
    elif len(plain_text) % 3 == 2:
        plain_text = plain_text + 'X'

    # 得到明文字母的【ascii码%65】的索引plain_text_index
    plain_text = plain_text.upper()
    plain_text_index = []
    for i in plain_text:
        i = ord(i) - 65
        plain_text_index.append(i)

    # 索引列表 plain_text_index转换为n行3列矩阵index_matrix（三个一组）
    index_matrix = np.array(plain_text_index).reshape((int(len(plain_text_index) / 3), 3))

    # n行3列矩阵index_matrix与3*3随机密钥矩阵randomKey相乘，并mod26
    # 得到加密后的数字矩阵encrypt_matrix
    encrypt_matrix = []
    for e in index_matrix:
        encrypt_matrix.append(np.dot(e, randomKey) % 26)

    # 将加密后的数字矩阵encrypt_matrix转换为列表encrypt_list
    encrypt_list = []
    for i in range(int(len(plain_text_index) / 3)):
        for j in range(3):
            encrypt_list.append(encrypt_matrix[i][j])

    # 将列表encrypt_list根据ascii码转换为字母，存入列表_encrypt
    _encrypt = []
    for i in encrypt_list:
        _encrypt.append(chr(i + 65))

    # 列表_encrypt转化为字符串
    _encrypt = ''.join([str(i) for i in _encrypt])

    return _encrypt


# 密文cipher_text,
def hillDecrypt(cipher_text):
    # 得到密文字母的【ascii码+65】的索引cipher_text_index
    cipher_text_index = []
    for i in cipher_text:
        i = ord(i) + 65
        cipher_text_index.append(i)

    # 索引列表 cipher_text_index转换为n行3列矩阵cipher_index_matrix（三个一组）
    cipher_index_matrix = np.array(cipher_text_index).reshape((int(len(cipher_text_index) / 3), 3))



    # n行3列矩阵cipher_index_matrix与3*3随机密钥矩阵randomKey的逆矩阵_randomKey相乘，并mod26
    # 得到数字矩阵decrypt_matrix
    decrypt_matrix = []
    for e in cipher_index_matrix:
        decrypt_matrix.append(np.dot( e,_randomKey) % 26)

    # 将加密后的数字矩阵decrypt_matrix转换为列表decrypt_list
    decrypt_list = []
    for i in range(int(len(cipher_text_index) / 3)):
        for j in range(3):
            decrypt_list.append(decrypt_matrix[i][j])

    # 将列表decrypt_list根据ascii码转换为字母，存入列表_decrypt
    _decrypt = []
    for i in decrypt_list:
        _decrypt.append(chr(int(i + 65)))
    # 列表_decrypt转化为字符串
    _decrypt = ''.join([str(i) for i in _decrypt])

    return _decrypt

if __name__=='__main__':
    print("*****Hill加密*****")
    print("加密请输入D:")
    user_input=input()


    print('生成随机密钥矩阵：')
    print(randomKey)
    print('随机密钥矩阵的逆矩阵：')
    print(_randomKey)

    print('请输入明文:')
    message = input()
    print("Hill加密结果: \n" + "明文: " + message)
    result_cipher=hillEncrypt(message)
    print("Cipher: "+result_cipher)
    print("\nHill解密结果: \n" + "密文: " + result_cipher)
    print("Plaintext:"+hillDecrypt(result_cipher))