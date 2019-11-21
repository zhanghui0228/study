from trans.tools import gen_trans_id
from work.tools import get_file_type
from datetime import datetime

def test_trans_tool():
    '''
    测试trans包下面tools模块
    :return:
    '''
    id1 = gen_trans_id()
    print(id1)
    date = datetime(2018, 5, 20, 13, 14, 00)
    id2 = gen_trans_id(date)
    print(id2)


def test_work_tool():
    '''
    测试work包下面的tools模块
    :return:
    '''
    file_name = 'c:\\user\\test.txt\\desktop\\test.txt.jpg'
    rest = get_file_type(file_name)
    print(rest)
if __name__ == '__main__':
    test_trans_tool()
    test_work_tool()