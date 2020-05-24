from django.db import connection


# 自定义封装分页类
class SqlPaginator(object):
    """ 实现sql分页 """

    def __init__(self, sql, params, page_size):
        super().__init__()
        self.sql = sql      # 查询sql
        self.params = params    # sql查询的参数
        self.page_size = page_size  # 每页数据


    def page(self, now_page):
        """
        获取当前页数据
        :param now_page: 当前页码
        :return:
        """
        offset = (now_page - 1) * self.page_size    # 偏移量
        sql = self.sql + ' limit %s offset %s'
        # 获取数据库连接
        # from django.db import connection
        # 获取连接游标
        cursor = connection.cursor()
        # 根据游标执行sql
        self.params.extend([self.page_size, offset])
        rest = cursor.execute(sql, self.params)
        # 获取查询结果
        rows = cursor.fetchall()
        return rows