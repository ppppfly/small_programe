# encoding=UTF-8

import os
import commands

# 旧版本的列表（字符串）
old_package = ''
# 获取的旧版本列表
old_package_list = []
# 新的版本列表
package_str = ''


def get_result_list(result_str):
    target_list = result_str.split('\n')
    for i in target_list:
        if i:
            old_package_list.append(i.split(' ')[0])
    return old_package_list


def list_to_string(target_list):
    return ' '.join(target_list)


def get_package_update_list():
    if not old_package:
        print '没有版本发生改变'

    old_package_list_with_version = old_package.split('\n')
    current_package_str = commands.getoutput('pip list')
    current_list_with_version = current_package_str.split('\n')

    update_record_str = ''

    for package_name in old_package_list_with_version:
        for current_package_name in current_list_with_version:
            if package_name.split(' ')[0] in current_package_name:
                update_record_str += '%s  ---->  %s\n' % (package_name, current_package_name)

    return update_record_str

if __name__ == '__main__':
    commands.getoutput('pip install --upgrade pip')
    old_package = commands.getoutput('pip list --outdated')
    old_package_list = get_result_list(old_package)
    if len(old_package_list) > 0:
        os.system('pip install --upgrade ' + list_to_string(old_package_list))
        print '全部部件更新完毕；'
        print get_package_update_list()
    else:
        os.system('pip list')
        print '没有需要更新的部件'
