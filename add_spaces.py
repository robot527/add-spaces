#! /usr/bin/python
# -*- coding: UTF-8 -*-
# author: robot527
# created at 2016-05-30

"""
自动给中文英文之间加入合理的空格
"""

def is_chinese(uni_ch):
    """判断一个 unicode 是否是汉字。"""
    if uni_ch >= u'\u4e00' and uni_ch <= u'\u9fa5':
        return True
    else:
        return False


def isdigit(uni_ch):
    """判断一个 unicode 是否是十进制数字。"""
    if uni_ch >= u'\u0030' and uni_ch <= u'\u0039':
        return True
    else:
        return False

def isalpha(uni_ch):
    """判断一个 unicode 是否是字母。"""
    if (uni_ch >= u'\u0041' and uni_ch <= u'\u005a') \
        or (uni_ch >= u'\u0061' and uni_ch <= u'\u007a'):
        return True
    else:
        return False


def is_en_symbol(uni_ch):
    """判断一个 unicode 是否是英文符号。"""
    if uni_ch in [u':', u';', u'%', u'!', u'?', u'`', u'°', u'*', u'_',\
            u'<', u'=', u'>', u'"', u'$', u'&', u'\'', u',', u'.', u'~',\
            u'/', u'@', u'\\', u'^', u'|']:
        return True
    else:
        return False


def is_en_l_bracket(uni_ch):
    """判断一个 unicode 是否是英文左括号。"""
    if uni_ch == u'(' or uni_ch == u'[':
        return True
    else:
        return False


def is_en_r_bracket(uni_ch):
    """判断一个 unicode 是否是英文右括号。"""
    if uni_ch == u')' or uni_ch == u']':
        return True
    else:
        return False


def is_zh_l_bracket(uni_ch):
    """判断一个 unicode 是否是中文左括号。"""
    if uni_ch == u'\uff08':
        return True
    else:
        return False


def is_zh_r_bracket(uni_ch):
    """判断一个 unicode 是否是中文右括号。"""
    if uni_ch == u'\uff09':
        return True
    else:
        return False


def add_spaces_to_string(string, code):
    """给字符串添加合理的空格。"""
    from re import sub
    newustr = ""
    flag = 0
    ustr = string.decode(code)
    ch_lst = list(ustr)
    length = len(ch_lst)
    for i in range(0, length):
        if i < length - 1:
            #中文(括号)与英文(括号)之间需要增加空格
            if (is_chinese(ch_lst[i]) and isalpha(ch_lst[i + 1])) \
                or (isalpha(ch_lst[i]) and is_chinese(ch_lst[i + 1])):
                ch_lst[i] += u" "
            elif (isalpha(ch_lst[i]) and is_zh_l_bracket(ch_lst[i + 1])) \
                or (is_zh_r_bracket(ch_lst[i]) and isalpha(ch_lst[i + 1])):
                ch_lst[i] += u" "
            elif (is_chinese(ch_lst[i]) and is_en_l_bracket(ch_lst[i + 1])) \
                or (is_en_r_bracket(ch_lst[i]) and is_chinese(ch_lst[i + 1])):
                ch_lst[i] += u" "
            #中文与英文符号之间需要增加空格
            elif (is_chinese(ch_lst[i]) and is_en_symbol(ch_lst[i + 1])) \
                or (is_en_symbol(ch_lst[i]) and is_chinese(ch_lst[i + 1])):
                ch_lst[i] += u" "
                flag = 1
            #中文(括号)与数字之间需要增加空格
            elif (is_chinese(ch_lst[i]) and isdigit(ch_lst[i + 1]))\
                or (isdigit(ch_lst[i]) and is_chinese(ch_lst[i + 1])):
                ch_lst[i] += u" "
            elif (isdigit(ch_lst[i]) and is_zh_l_bracket(ch_lst[i + 1]))\
                or (is_zh_r_bracket(ch_lst[i]) and isdigit(ch_lst[i + 1])):
                ch_lst[i] += u" "

        newustr += ch_lst[i]
    newstring = newustr.encode(code)
    if flag == 1:
        #处理中文里的粗体字和斜体字
        newstring = sub(r' \* ', '*', newstring)
        newstring = sub(r' \*\* ', '**', newstring)
        newstring = sub(' _ ', '_', newstring)
        newstring = sub(' __ ', '__', newstring)

    return add_space_betw_digit_and_unit(newstring)


def add_space_betw_digit_and_unit(string):
    """给数字与单位之间增加空格。"""
    from re import sub
    # 常用单位，不齐全
    units = ['bps', 'Kbps', 'Mbps', 'Gbps',
            'B', 'KB', 'MB', 'GB', 'TB', 'PB',
            'g', 'Kg', 't',
            'h', 'm', 's']
    for unit in units:
        pattern = r'(?<=\d)' + unit #positive lookbehind assertion,
                                    #如果前面是括号中 '=' 后面的字符串，则匹配成功
        repl = ' ' + unit
        string = sub(pattern, repl, string)
    return string


def add_spaces_to_file(file_name, code="gbk"):
    """给文本文件的内容添加合理的空格, 生成处理过的新文件。"""
    import os.path
    dir_name = os.path.dirname(file_name)
    base_name = os.path.basename(file_name)
    if dir_name == '':
        new_file = code + "-" + base_name
    else:
        new_file = dir_name + "/" + code + "-" + base_name
    try:
        with open(file_name) as text:
            line_list = [add_spaces_to_string(line, code) \
                            for line in text]
    except UnicodeDecodeError as err:
        return str(err)
    except IOError as err:
        return str(err)
    try:
        with open(new_file, "w") as nfile:
            nfile.writelines(line_list)
            print 'Finished adding spaces, generated new file: %s' % new_file
            return 'Success.'
    except IOError as err:
        return str(err)


if __name__ == '__main__':
    import sys
    argc = len(sys.argv)
    codeset = ['gb2312', 'gbk', 'utf8', 'gb18030', 'hz',\
                'iso2022_jp_2', 'big5', 'big5hkscs']
    if argc == 1:
        print 'Usage: python add_spaces.py /path/to/file code(e.g. gbk, utf8)'
        print '    or python add_spaces.py /path/to/file'
    elif argc == 2:
        for item in codeset:
            if add_spaces_to_file(sys.argv[1], item) == 'Success.':
                print 'Processing completed.'
                break
    elif argc == 3:
        if sys.argv[2] in codeset:
            print add_spaces_to_file(sys.argv[1], sys.argv[2])
        else:
            print 'Parameter code (%s) error!' % sys.argv[2]
            print 'Supported codes are ' + ', '.join(codeset)
    else:
        print 'Usage: python add_spaces.py /path/to/file code'
