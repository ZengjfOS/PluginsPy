# 一、README

以Plugin的形式集成命令行脚本，便于脚本的集中管理

**所有的插件放在项目Plugins目录，或者指定插件目录，才能被检查到**

## 二、安装

* pypi
  * `pip3 install PluginsPy`
* 手动安装
  * `pip3 uninstall PluginsPy`
  * `pip3 install PluginsPy-0.0.5-py3-none-any.whl --force-reinstall`
  * `python3 -m pip show PluginsPy`

## 三、使用示例

### 3.1 插件自动生成run方法

* `0.0.*`版本，使用Decorator添加run()方法
  ```python
  import PluginsPy as PluginsPy

  @PluginsPy.addRun
  class PluginExample:
  ```
* `0.1.*`版本不需要以上操作，只需要将类放在插件目录即可，兼容`0.0.*`版本

### 3.2 插件参数声明

* 第一行是类说明，在帮助中显示
* @开头并且以:分开的是参数及其说明
* 之外的是普通说明，可以自行添加，譬如以*号开始列表
* `0.0.*`版本
  ```python
  @PluginsPy.addRun
  class PluginExample:
      """
      PluginExample类是一个编写LogTools插件的示例

      @id: 唯一码
      @name: 唯一码别名
      """
  ```
* `0.1.*`版本
  ```python
  class PluginExample:
      """
      PluginExample类是一个编写LogTools插件的示例

      @id: 唯一码
      @name: 唯一码别名
      """
  ```

### 3.3 插件使用

```python
from PluginsPy import PluginsPy

if __name__ == '__main__':
    PluginsPy(__file__)
```

## 四、示例输出

test_PluginsPy.py PluginExample

```
>>> start call Plugin run or CmdMaps method
>>> enter plugin run method
实例输出：id: 123456, name: zengjf
>>> enter plugin start method
>>> in plugin start method
{'id': '123456', 'name': 'zengjf', 'func': <bound method addRun.<locals>.run of <class 'Plugins.PluginExample.PluginExample'>>}
<<< out plugin start method
<<< end plugin start method
<<< end plugin run method
<<< end call Plugin run or CmdMaps method
```

## 五、快捷键

* j：选择上一个
* k：选择下一个
* /：进入首字母快速选择模式，边框会变成绿色
  * a-z，0-9：跳转到首字母为该字符的插件位置，便于快速选择，目前支持一个字符

## 六、发行PyPi处理流程

* pip3 install twine
* https://pypi.org/
  * 注册帐号
* python3 setup.py sdist bdist_wheel
* twine upload dist/*
  ```
  Uploading distributions to https://upload.pypi.org/legacy/
  Enter your username: zengjf
  Enter your password:
  Uploading PluginsPy-0.0.1-py3-none-any.whl
  100% ---------------------------------------- 8.4/8.4 kB • 00:00 • ?
  Uploading PluginsPy-0.0.1.tar.gz
  100% ---------------------------------------- 6.6/6.6 kB • 00:00 • ?
  
  View at:
  https://pypi.org/project/PluginsPy/0.0.1/
  ```
