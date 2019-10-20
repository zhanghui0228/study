import os.path
import constants


def get_file_type(file_name):
    '''
    根据文件的名称来判断文件的类型
    :param file_name:文件名称
    :return:文件类型

    '''
    result = constants.FILE_TYPE_OTHER
    #if not os.path.isfile(file_name):
    #    return result
    path_name, ext = os.path.splitext(file_name)
    #将文件的后缀名统一转换为小写
    ext = ext.lower()
    if ext in ('.png', '.jpg', '.gif', '.bmp'):
        result = constants.FILE_TYPE_IMG
    elif ext in ('.doc', '.docx'):
        result = constants.FILE_TYPE_DOC
    elif ext in ('.xls', '.xlsx'):
        result = constants.FILE_TYPE_EXCEL
    elif ext in ('.ppt', '.pptx'):
        result = constants.FILE_TYPE_PPT
    return result

