# Envlt



## 这是环境工具，集合了资产，地形，散步的功能

***
## 开发日志
### _wangshuo_  _zhuyihan_
***

#### 2024/06/26

- [x] 开发建立资产表的功能
- [x] 开发项目克隆功能

***

#### 2024/06/25

- [x] 开发创建新场景的功能
    - [x] 上传图片功能
    - [x] 创建temp临时配置文件类
        - 记录QFileDialog上次选择路径，temp/envlt/config/file_dialog_last_choose.json
    - [x] 增加 检查场景存在功能
    - [x] 写入数据库
- [x] 增加自定义MessageBox
    - [x] 支持information, warning, error

***

#### 2024/6/27

- [x] 开发场景克隆功能: 
   - [x] `envlt_database`模块中新增`insert_data_to_table`方法,用于往表中插入数据,接受参数类型为`列表`和`字符串`
   - [x] `mainWindow`中完成`_clone_scene`方法
- [x] 其余修改项：
   - [x] 修改`mainWindow`中`choose_image`方法,使其可以根据触发槽函数对象不同设置不同文本框的内容
   - [x] 将`mainWindow`中`now_time`变量设置为初始化变量,用于`_clone_scene`方法



   