# Envlt

## 这是环境工具，集合了资产，地形，散步的功能

***

## 开发日志

### _wangshuo_  _zhuyihan_


***

### 2024/06/28

- [x] 开发日志系统
    - 创建日志:

```python
### 创建日志类

from ns_Envlt.envlt_log import log_factory

# 定义一个log农场
log = log_factory.LogFactory(log_name="unit_test2", user_dir=False)
# 写入日志
log.write_log(log_level=log_factory.LogLevel.INFO, content="my_test")
# 列举出所有日志路径
log.list_all_logs_path(user=False)
# 列举出指定数量的日志路径
log.list_logs_path(user=False, limit=1)

# 读取日志内容
log_file = log_factory.LogFileFactory(log_factory=log)
log_contents = log_file.read_line_content()  # 获取日志会从log农场提取logs_path_list的属性
```

- [x] 构建`Project`页面,实现场景信息的放置与自动排列。
    - [x] `mainWindow`同目录下添加`project_ui.py`.
    - [x] 修改`envlt_database`中的`get_asset_libs_data`方法,若传入表名为总表名则不添加`_libs`后缀.

***

### 2024/6/27

- [x] 开发场景克隆功能:
    - [x] `envlt_database`模块中新增`insert_data_to_table`方法,用于往表中插入数据,接受参数类型为`列表`和`字符串`
    - [x] `mainWindow`中完成`_clone_scene`方法
- [x] 其余修改项：
    - [x] 修改`mainWindow`中`choose_image`方法,使其可以根据触发槽函数对象不同设置不同文本框的内容
    - [x] 将`mainWindow`中`now_time`变量设置为初始化变量,用于`_clone_scene`方法

***

### 2024/06/26

- [x] 开发建立资产表的功能
- [x] 开发项目克隆功能

***

### 2024/06/25

- [x] 开发创建新场景的功能
    - [x] 上传图片功能
    - [x] 创建temp临时配置文件类
        - 记录QFileDialog上次选择路径，temp/envlt/config/file_dialog_last_choose.json
    - [x] 增加 检查场景存在功能
    - [x] 写入数据库
- [x] 增加自定义MessageBox
    - [x] 支持information, warning, error

***




   