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


def is_e_rightbracket(uni_ch):
    """判断一个 unicode 是否英文右括号。"""
    if uni_ch == u')':
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
    newstring = ""
    char_list = list(ustr)
    #print char_list
    for i in range(0, len(char_list)):
        if i < len(char_list) - 1:
            if (is_chinese(char_list[i]) and isdigit(char_list[i + 1])) or (is_chinese(char_list[i]) and isalpha(char_list[i + 1])):
                char_list[i] = char_list[i]+" "
            elif (isdigit(ustr[i]) and is_chinese(ustr[i + 1])):
                char_list[i] = char_list[i]+" "
            elif (isalpha(ustr[i]) and is_chinese(ustr[i + 1])):
                char_list[i] = char_list[i]+" "
            elif (is_e_rightbracket(ustr[i]) and is_chinese(ustr[i + 1])):
                char_list[i] = char_list[i]+" "
            elif (is_c_rightbracket(ustr[i]) and isdigit(ustr[i + 1])) or (is_c_rightbracket(ustr[i]) and isalpha(ustr[i + 1])):
                char_list[i] = char_list[i]+" "

        newstring = newstring + char_list[i]
    return newstring

def add_spaces_to_file(file_name):
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
