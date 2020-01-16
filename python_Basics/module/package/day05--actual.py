

'''
    random 函数生成随机数
    使用方法：
        random.randint(起始数，结束数)     #括号内指定的是生成的范围数

'''
'''
    什么是虚拟环境：
        1、建立在宿主环境上的独立容器
        2、具备和宿主环境相同的功能
        3、可以快速创建、删除，方便管理
    好处：
        独立--相互隔离，互不影响
        纯净--只有一个项目用的包和依赖，好管理
        方便--摒弃频繁安装/卸载包和依赖
        
    虚拟环境----virtualenv
        使用 pip install virtualenv   进行安装
        创建虚拟环境：
            virutalenv 虚拟环境名称
        进入/退出虚拟环境：
            activate/deactivate
            
            进入到 虚拟环境目录/Scripts/
            执行activate进入虚拟环境
            执行deactivate退出虚拟环境
            
        pip install virtualenvwrapper-win   #在Windows上安装执行这个
        pip install virtualenvwrapper       #在Linux上或者mac os上安装执行这个
        
        #前提条件，需要将WORKON_HOME=虚拟环境存放位置    添加到环境变量
        workon 虚拟环境名称       #自由切换虚拟环境
        
    虚拟环境----pipenv
        pip install pipenv      #安装pipenv命令，需要在要使用的目录下进行安装
        pipenv --python 2.7     #创建一个安装python2.7版本的虚拟环境
        pipenv shell            #进入创建好的虚拟环境
'''