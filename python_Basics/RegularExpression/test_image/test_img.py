import re

'''
    使用正则表达式练习去获取图片地址
'''

def test_re_img():
    ''' 正则表达式获取图片 '''
    #1、读取图片网页文件
    with open('img.html', 'r', encoding='UTF8') as f:
        ImageHtml = f.read()
        #print(ImageHtml)
        #1、书写匹配图片的正则表达式
        pattren = re.compile(r'<img.+?src=\"(.+?)\".+?>')
        ImageList = pattren.findall(ImageHtml)
        for li in ImageList:
            url = li.replace('amp;', '')
            # with open('imgurl.txt', 'a', encoding='UTF8') as w:
            #     w.write(url)
            print(url)


if __name__ == '__main__':
    test_re_img()