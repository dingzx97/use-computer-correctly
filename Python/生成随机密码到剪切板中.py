def set_clipboard_text(text='hello my friend'):
    '''
    设置文本到剪切板中

    text:
        str类型,表示要复制的内容。
    
    需要pywin32模块；
        pip install pywin32
    '''
    import win32clipboard as w
    
    w.OpenClipboard()  
    w.EmptyClipboard()  
    w.SetClipboardText(text)  
    w.CloseClipboard()

def create_random_passwd(pass_type='1234', pass_length='16'):
    '''
    生成随机的密码

    pass_type:
        str类型，密码所包含的种类[1.大写  2.小写  3.数字  4.特殊字符]
        例如，不要数字就写\'124\'，默认为\'1234\'包含所有种类。
                
    pass_length:
        str类型，密码的长度，默认长度为16位。
        
    return:
        str类型，返回生成的密码
    '''
    from string import ascii_lowercase, ascii_uppercase, digits, punctuation
    from secrets import choice

    combination = ''
    password = ''
    
    if pass_type:
        if '1' in pass_type:
            combination += ascii_uppercase
        if '2' in pass_type:
            combination += ascii_lowercase
        if '3' in pass_type:
            combination += digits
        if '4' in pass_type:
            combination += punctuation
    else :
        combination += ascii_uppercase + ascii_lowercase + digits + punctuation
    
    if pass_length:
        pass_length = eval(pass_length)
    else:
        pass_length = 16
    
    for _ in range(pass_length):
        password += choice(combination)
    
    return password

if __name__ == '__main__':
    print('1.大写  2.小写  3.数字  4.特殊字符')
    print('默认为\'1234\',即包含所有种类，不要数字就写\'124\',默认长度为16位')
    pass_type = input('现在想要的密码种类：')
    pass_length = input('密码长度：')
    
    password = create_random_passwd(pass_type, pass_length)
    print('生成的密码：',password)
    set_clipboard_text(password)
