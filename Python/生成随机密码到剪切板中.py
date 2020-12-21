def set_clipboard_text(text='hello my friend'):
    '''
    设置文本到剪切板中
    
    text:
        字符串类型,表示要复制的内容。
    
    需要pywin32模块；
        pip install pywin32
    '''
    import win32clipboard as w
    
    w.OpenClipboard()  
    w.EmptyClipboard()  
    w.SetClipboardText(text)  
    w.CloseClipboard()

def create_random_passwd(pass_type='1234', pass_length=16):
    '''
    生成随机的密码

    pass_type:
        字符串类型，密码所包含的种类[1.大写  2.小写  3.数字  4.特殊字符]
        例如，不要数字就写\'124\'，默认为\'1234\'包含所有种类。
                
    pass_length:
        字符串类型，密码的长度，默认长度为16位。
        
    return:
        字符串类型，返回生成的密码
    '''
    from random import choice
    
    capital_list = [chr(i) for i in range(65,91)]
    lower_list = [chr(i) for i in range(97,123)]
    num_list = [chr(i) for i in range(48,58)]
    symbol_list = ['!', '@', '#', '$', '%', '^', '&', '*', '.']

    combination = []
    if '1' in pass_type:
        combination += capital_list
    if '2' in pass_type:
         combination += lower_list
    if '3' in pass_type:
        combination += num_list
    if '4' in pass_type:
        combination += symbol_list
    if not combination:
        combination += capital_list+lower_list+num_list+symbol_list

    if pass_length < 1:
        pass_length = 16
    
    password = ''
    for _ in range(pass_length):
        password += choice(combination)
    
    return password

if __name__ == '__main__':
    print('1.大写  2.小写  3.数字  4.特殊字符')
    print('默认为\'1234\',即包含所有种类，不要数字就写\'124\',默认长度为16位')
    pass_type = input('现在想要的密码种类：')
    pass_length = eval(input('密码长度：'))
    
    password = create_random_passwd(pass_type, pass_length)
    print('生成的密码：',password)
    set_clipboard_text(password)
