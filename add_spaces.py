#! /usr/bin/python
# -*- coding: UTF-8 -*-


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
    if (uni_ch >= u'\u0041' and uni_ch <= u'\u005a') or (uni_ch >= u'\u0061' and uni_ch <= u'\u007a'):
        return True
    else:
        return False


def is_e_leftbracket(uni_ch):
    """判断一个 unicode 是否英文左括号。"""
    if uni_ch == u'(' or uni_ch == u'[':
        return True
    else:
        return False


def is_e_rightbracket(uni_ch):
    """判断一个 unicode 是否英文右括号。"""
    if uni_ch == u')' or uni_ch == u']':
        return True
    else:
        return False


def is_c_leftbracket(uni_ch):
    """判断一个 unicode 是否中文左括号。"""
    if uni_ch == u'\uff08':
        return True
    else:
        return False


def is_c_rightbracket(uni_ch):
    """判断一个 unicode 是否中文右括号。"""
    if uni_ch == u'\uff09':
        return True
    else:
        return False


def add_spaces_to_ustring(ustr):
    """给 unicode 字符串添加合理的空格。"""
    newstring = ""
    char_list = list(ustr)
    length = len(char_list)
    for i in range(0, length):
        if i < length - 1:
            #中文(括号)与英文(括号)之间需要增加空格
            if (is_chinese(char_list[i]) and isalpha(char_list[i + 1]))\
                or (isalpha(char_list[i]) and is_chinese(char_list[i + 1])):
                char_list[i] += u" "
            elif (isalpha(char_list[i]) and is_c_leftbracket(char_list[i + 1]))\
                or (is_c_rightbracket(char_list[i]) and isalpha(char_list[i + 1])):
                char_list[i] += u" "
            elif (is_chinese(char_list[i]) and is_e_leftbracket(char_list[i + 1]))\
                or (is_e_rightbracket(char_list[i]) and is_chinese(char_list[i + 1])):
                char_list[i] += u" "
            #中文(括号)与数字之间需要增加空格
            if (is_chinese(char_list[i]) and isdigit(char_list[i + 1]))\
                or (isdigit(char_list[i]) and is_chinese(char_list[i + 1])):
                char_list[i] += u" "
            elif (isdigit(char_list[i]) and is_c_leftbracket(char_list[i + 1]))\
                or (is_c_rightbracket(char_list[i]) and isdigit(char_list[i + 1])):
                char_list[i] += u" "

        newstring = newstring + char_list[i]
    return newstring

def add_spaces_to_file(file_name):
    """给文本文件添加合理的空格。"""
    try:
        with open(file_name, 'r+') as text:
            #line_list = [add_spaces_to_ustring(unicode(line.rstrip(), "UTF-8")).encode('UTF-8') + '\n' for line in text]
            line_list = [add_spaces_to_ustring(line.rstrip().decode("UTF-8")).encode('UTF-8') + '\n' for line in text]
            text.seek(0)
            text.truncate(0)
            text.writelines(line_list)
            print 'Finished adding spaces.'
    except IOError as err:
        print 'File error: ' + str(err)


if __name__ == '__main__':
    print 'Please input a file name.'
    print 'Usage - "test.txt", "/home/user/test/abc.md"'
    target_file = raw_input("@> ")
    if target_file is '':
        target_file = 'test.txt'
    print 'Target file is ' + target_file + '  !\n'
    add_spaces_to_file(target_file)
    print 'Process is completed.'
