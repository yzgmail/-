"""
作者：杨滢榕
版本：V2.0
功能：1.实现有关凯撒密码的加密解密
     2.舍弃1.0版本的函数
时间：07/09/2019
"""

def jiami(shuru,pianyi):
    """
     加密程序
    """
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
                'v', 'w''x', 'y', 'z']
    shuru_new = ""
    for i in range(len(shuru)):
        if shuru[i] in alphabet:
            temp = ord(shuru[i])
            number = (temp - 97 + pianyi) % 26
            shuru_new = chr(number + 97)
            print(shuru_new,end="" )

def jiemi(shuru,pianyi):
    """
解密程序
    """
    pass








def main():
    # 主程序
    print("1.凯撒加密")
    print("2.凯撒解密")
    choice = input()
    if choice == "1":
        shuru = input("请输入加密字符串：")
        pianyi = int(input("偏移位数："))
        jiami(shuru,pianyi)
        print()
    elif choice == "2":
        shuru = input("请输入解密字符串：")
        pianyi = int(input("请输入偏移位数："))
        jiemi(shuru,pianyi)
        print()
    else:
        print("输入错误，请重试")
        main()

if __name__ == '__main__':
    # 执行主程序
    main()