#!/usr/bin/env python3

class GuangDong:
    """
    Shenzhen类是一个编写LogTools插件的示例

    @name(zengjf): 唯一码别名
    @path(input/AndroidSystemWakeup.curf): 唯一码别名
    """

    def __init__(self, kwargs):
        print(">>> in plugin init method")

        print("GuangDong")

        print("<<< out plugin init method")

    # 装饰@PluginsPy.addRun自动添加run方法参考
    # @classmethod
    # def run(clazz, kwargs):
    #     print(">>> enter plugin run method")
    #     print(kwargs)
    #     clazz(kwargs)
    #     print("<<< end plugin run method")

    def start(self, kwargs):
        print(">>> in plugin start method")
        print(kwargs)
        print("<<< out plugin start method")

        return kwargs["name"]

if __name__ == "__main__" :
    GuangDong({})
