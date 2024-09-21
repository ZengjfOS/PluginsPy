#!/usr/bin/env python3

import importlib
import re
import os
import inspect
import json
from datetime import datetime
import subprocess

from PluginsPy.MainUI import *
from PluginsPy.Config import Config

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class Plugin:

    PlotType = ["normal", "key"]
    RegexTemplate = ["null", "logcat", "kernel"]

    def __init__(self, ui: Ui_MainWindow, MainWindow: QMainWindow):
        self.ui               = ui
        self.gridLayout       = ui.PSGridLayout
        self.MainWindow       = MainWindow
        self.config           = Config()

        # Plugins
        ui.PSPluginsComboBox.currentIndexChanged.connect(self.PSPluginsChanged)
        ui.PSRunPushButton.clicked.connect(self.PSRunClick)
        ui.PSRegexPushButton.clicked.connect(self.PSRegexClick)
        ui.PSVisualLogPushButton.clicked.connect(self.PSVisualLogClick)
        ui.PSTempPushButton.clicked.connect(self.PSTempClick)
        ui.PSPlotTypeComboBox.addItems(Plugin.PlotType)
        ui.PSPlotTypeComboBox.setCurrentIndex(0)
        ui.PSRegexTemplateComboBox.currentIndexChanged.connect(self.PSRegexTemplateChanged)
        ui.PSRegexTemplateComboBox.addItems(Plugin.RegexTemplate)

        self.initPlugins()

        self.lineInfosOfFiles = []

    def getPluginsIndex(self, pluginsDir="Plugins") :

        filenames = []
        for file in os.listdir(pluginsDir):
            full_path = os.path.join(pluginsDir, file)
            if os.path.isfile(full_path):
                filenames.append(file)

        fileIndex = 0
        for file in filenames:
            if file == "__init__.py":
                continue

            moduleString = file.split(".")[0]
            matchObj = re.match(r'\d{4}[_]?', moduleString)
            if matchObj:
                currentIndex = int(matchObj.group(0).replace("_", ""))
                if currentIndex > fileIndex:
                    fileIndex = currentIndex

        print("current file index: " + str(fileIndex))

        return fileIndex

    def getVisualLogData(self):
        data = {}

        data["xAxis"]     = eval("[" + self.ui.PSXAxisLineEdit.text() + "]")
        data["dataIndex"] = eval("[" + self.ui.PSDataIndexLineEdit.text() + "]")
        data["plotType"]  = self.ui.PSPlotTypeComboBox.currentText()

        for i in range(len(data["xAxis"])):
            if data["xAxis"][i] < 0:
                data["xAxis"][i] = 0

        if len(data["dataIndex"]) == 0:
            data["dataIndex"].append(0)

        return data

    def PSVisualLogClick(self):

        '''
        利用反射处理绘图才不会导致当前UI异常
        '''

        print("PSVisualLogClick")

        self.visualLogData = self.getVisualLogData()

        moduleString = "VisualLogPlot"
        args = self.visualLogData
        args["lineInfosFiles"] = self.lineInfosOfFiles

        # import file
        module = importlib.import_module("PluginsPy." + moduleString)
        # get class
        clazz  = getattr(module, moduleString)
        # new class
        obj = clazz(args)

        ret = None
        invert_op = getattr(obj, "start", None)
        if callable(invert_op):
            print(">>> enter plugin start method")
            if len(inspect.signature(invert_op).parameters) > 0:
                ret = invert_op(args)
            else:
                ret = invert_op()
            print("<<< end plugin start method")

        if ret == None:
            return ""
        elif isinstance(ret, list):
            return "\n".join(ret)
        elif isinstance(ret, int) or isinstance(ret, float):
            return str(ret)
        else:
            return ret

    def PSRegexClick(self):
        print("PSRegexClick")

        self.lineInfosOfFiles = []

        regexArray = self.ui.PSRegexPlainTextEdit.toPlainText().strip().splitlines()
        print(regexArray)

        if os.path.exists("output"):
            self.config.setKeyValues(self.getVisualLogData())
            self.config.setKeyValue("pluginIndex", self.ui.PSPluginsComboBox.currentIndex())
            self.config.setKeyValue("regex", "\n".join(regexArray))
            self.config.saveConfig()

        if len(regexArray) > 0:
            keyValues = self.getKeyValues()
            '''
            这里每个文件调一次解析

            for key in keyValues.keys():
                if "\\" in keyValues[key] or "/" in keyValues[key]:
                    print(regexArray)
                    print(key + " -> " + keyValues[key])

                    if os.path.exists(keyValues[key]):
                        print(keyValues[key])
                        # r"(\d{2}-\d{2}\s+\d{2}:\d{2}:\d{2}\.\d*)\s+\d+\s+\d+\s+\w+\s+.*: In wakeup_callback: resumed from suspend"

                        moduleString = "VisualLogPlot"
                        # import file
                        module = importlib.import_module("PluginsPy." + moduleString)
                        # get class, file list to parse
                        clazz  = getattr(module, moduleString)
                        method = getattr(clazz, "parseData")
                        lineInfos, filenames = method(keyValues[key], regexArray)

                        self.lineInfosOfFiles.append(lineInfos)
                    else:
                        print("can't file path:" + keyValues[key])
            '''

            # 整体调一次解析
            parseFiles = []
            for key in keyValues.keys():
                if "\\" in keyValues[key] or "/" in keyValues[key]:
                    print(key + " -> " + keyValues[key])

                    if os.path.exists(keyValues[key]):
                        print(keyValues[key])
                        # r"(\d{2}-\d{2}\s+\d{2}:\d{2}:\d{2}\.\d*)\s+\d+\s+\d+\s+\w+\s+.*: In wakeup_callback: resumed from suspend"
                        parseFiles.append(keyValues[key])

                    else:
                        print("can't file path:" + keyValues[key])

            moduleString = "VisualLogPlot"
            # import file
            module = importlib.import_module("PluginsPy." + moduleString)
            # get class, file list to parse
            clazz  = getattr(module, moduleString)
            method = getattr(clazz, "parseData")
            print(parseFiles)
            self.lineInfosOfFiles, filenames = method(parseFiles, regexArray)

        for lineInfos in self.lineInfosOfFiles:
            print("file data: ")
            for info in lineInfos:
                print(info)

    def PSTempClick(self):
        print("PSTempClick")

        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        filePath, _ = QFileDialog.getSaveFileName(None,
                                              "Save File",
                                              os.getcwd() + "/Plugins",
                                              "All Files (*);;Text Files (*.txt)",
                                              options=options)
        if filePath.strip() == "":
            print("please input file name")
            return

        # Windows，os.getcwd path with "\"，QFileDialog get path with "/"
        relFilePath = filePath.replace(os.getcwd().replace("\\", "/"), "").replace("\\", "/")[1:]
        relFileDir = os.path.dirname(relFilePath)
        fileName = os.path.basename(relFilePath)
        fileName = fileName[0].upper() + fileName[1:]
        if not fileName.endswith(".py"):
            fileName += ".py"

        print(relFileDir)
        print(fileName)

        regexArray = self.ui.PSRegexPlainTextEdit.toPlainText().strip().replace("'", "\\'").splitlines()
        visualLogData = self.getVisualLogData()

        plotType = self.ui.PSPlotTypeComboBox.currentText()

        keyValues = self.getKeyValues()
        moduleArgs = ""
        clazzArgs  = ""
        # parseFilenameArgs = "        parseFilenames = ["
        parseFilenameArgs = []
        for key in keyValues.keys():
            if "/" in keyValues[key]:
                pathValue: str = keyValues[key]
                if os.getcwd() in pathValue:
                    pathValue = pathValue.replace(os.getcwd(), "").replace("\\", "/")[1:]

                moduleArgs += "    @" + key + "(" + pathValue + "): None\n"
                clazzArgs  += "        " + key + " = kwargs[\"" + key + "\"]\n"

                parseFilenameArgs.append(key)

        parseFilenameArgs = "parseFilenames = [" + ", ".join(parseFilenameArgs) + "]"

        res = subprocess.run(["git", "config", "user.name"], stdout=subprocess.PIPE)
        authorName = res.stdout.strip().decode()
        if len(authorName) == 0:
            authorName = os.getlogin()

        clazzName = fileName
        currentPluginIndex = self.getPluginsIndex() + 1
        matchObj = re.match(r'\d{4}[_]?', fileName)
        if matchObj:
            clazzName = fileName.replace(matchObj.group(0), "").replace(".py", "")
        else:
            clazzName = fileName.replace(".py", "")
            fileName = ("%04d" % currentPluginIndex) + "_" + fileName

        with open(relFileDir + "/" + fileName, mode="w", encoding="utf-8") as f:
            outputArray = [
                    "#!/usr/bin/env python3",
                    "# -*- coding: utf-8 -*-",
                    "",
                    "\"\"\"",
                    "Author: " + authorName,
                    "Date: "   + datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    "License: MIT License",
                    "\"\"\"",
                    "",
                    "import datetime",
                    "",
                    "from PluginsPy.VisualLogPlot import VisualLogPlot",
                    "",
                    "import VisualLog.LogParser as LogParser",
                    "import VisualLog.MatplotlibZoom as MatplotlibZoom",
                    "",
                    "import matplotlib.pyplot as plot",
                    "from matplotlib.figure import Figure",
                    "from matplotlib.axes import Axes",
                    "",
                    "class " + clazzName + ":",
                    "",
                    "    \"\"\"",
                    moduleArgs.rstrip(),
                    "    \"\"\"",
                    "",
                    "    def __init__(self, kwargs):",
                    "",
                    "        print(\"" + fileName.replace(".py", "") + " args:\")",
                    "        print(kwargs)",
                    "",
                    clazzArgs.rstrip(),
                    "",
                    "        " + parseFilenameArgs,
                    "        regex = [\n            '" + "',\n            '".join(regexArray) + "'\n            ]",
                    "        kwargs[\"lineInfosFiles\"], filenames = LogParser.logFileParser(",
                    "                parseFilenames,",
                    "                regex,",
                    "            )",
                    "",
                    "        plotType               = \"" + plotType + "\"",
                    "        kwargs[\"xAxis\"]      = [" + (", ".join([str(i) for i in visualLogData["xAxis"]])) + "]",
                    "        kwargs[\"dataIndex\"]  = [" + (", ".join([str(i) for i in visualLogData["dataIndex"]])) + "]",
                    "",
                    "        if plotType == \"normal\":",
                    "            MatplotlibZoom.Show(callback=VisualLogPlot.defaultShowCallback, rows = 1, cols = 1, args=kwargs)",
                    "        elif plotType == \"key\":",
                    "            MatplotlibZoom.Show(callback=VisualLogPlot.defaultKeyShowCallback, rows = 1, cols = 1, args=kwargs)",
                    "        else:",
                    "            print(\"unsupport plot type\")",
                    ""
                ]

            f.write("\n".join(outputArray))

        self.initPlugins()

    def initPlugins(self):
        self.plugins     = {}
        self.firstPlugin = ""

        for f in self.getPluginFiles("Plugins"):
            moduleFile   = f.split(".")[0]
            moduleString = moduleFile

            if moduleFile == "__init__":
                continue

            matchObj     = re.match(r'\d{4}[_]?', moduleFile)
            if matchObj:
                moduleString = moduleFile.replace(matchObj.group(0), "")

            self.plugins[moduleString] = moduleFile

            if self.firstPlugin == "":
                self.firstPlugin = moduleString
 
        self.pluginsKeys = list(self.plugins.keys())
        # self.ui.PSPluginsComboBox.addItems(self.pluginsKeys)
        self.ui.PSPluginsComboBox.clear()
        self.ui.PSPluginsComboBox.addItems(self.plugins.values())
        # 下面这句会导致重复加载界面
        # self.fillePSGridLayout(self.ui.PSGridLayout, self.getClazzArgs(self.firstPlugin))

        self.setSavedConfig()

    def setSavedConfig(self):
        configData = self.config.keyValues

        if "regex" in configData.keys():
            self.ui.PSRegexPlainTextEdit.setPlainText(configData["regex"])
        else:
            self.ui.PSRegexPlainTextEdit.setPlainText("(\\d{2}-\\d{2}\\s+\\d{2}:\\d{2}:\\d{2}\\.\\d*)\\s+\\d+\\s+\\d+\\s+\\w+\\s+.*: In wakeup_callback: resumed from suspend (\\d+)")

        if "xAxis" in configData.keys():
            self.ui.PSXAxisLineEdit.setText(",".join([str(i) for i in configData["xAxis"]]))
        else:
            self.ui.PSXAxisLineEdit.setText("0")

        if "dataIndex" in configData.keys():
            self.ui.PSDataIndexLineEdit.setText(",".join([str(i) for i in configData["dataIndex"]]))
        else:
            self.ui.PSDataIndexLineEdit.setText("0, 1")

        if "pluginIndex" in configData.keys() and configData["pluginIndex"] < len(self.plugins.values()):
            self.ui.PSPluginsComboBox.setCurrentIndex(configData["pluginIndex"])

        if "plotType" in configData.keys():
            self.ui.PSPlotTypeComboBox.setCurrentText(configData["plotType"])

    def fillePSGridLayout(self, gridLayout: QGridLayout, keyValues: dict):
        i = 0
        if len(keyValues) == 0:
            '''
            blank labels just to take up space
            '''
            label = QLabel("")
            value = QLabel("")
            gridLayout.addWidget(label, i, 0, 1, 1)
            gridLayout.addWidget(value, i, 1, 1, 1)
        else:
            for key in keyValues.keys():
                label = QLabel(key)
                if isinstance(keyValues[key], str):
                    value = QLineEdit(keyValues[key])
                    gridLayout.addWidget(label, i, 0, 1, 1)
                    gridLayout.addWidget(value, i, 1, 1, 1)

                    if "/" in keyValues[key] or "\\" in keyValues[key]:
                        button = QPushButton("Select File ...")
                        button.clicked.connect(self.PSPluginsArgsClicked)
                        gridLayout.addWidget(button, i, 2, 1, 1)
                else:
                    value = QComboBox()
                    comboxValue = (list)(keyValues[key][1])
                    value.addItems(comboxValue)

                    gridLayout.addWidget(label, i, 0, 1, 1)
                    gridLayout.addWidget(value, i, 1, 1, 1)

                    value.currentIndexChanged.connect(self.PSArgsComboxChanged)
                    value.setCurrentIndex(comboxValue.index(keyValues[key][0]))

                i += 1

    def PSPluginsArgsClicked(self):
        print("PSPluginsClicked")
        row, col = self.findWidgetPosition(self.ui.PSGridLayout)

        fileName,fileType = QFileDialog.getOpenFileName(None, "select file", os.getcwd(), "All Files(*);;Text Files(*.txt)")
        if (len(fileName) > 0):
            print(fileName)
            print(fileType)

            edit: QLineEdit = self.ui.PSGridLayout.itemAtPosition(row, col - 1).widget()
            edit.setText(fileName)


    def findWidgetPosition(self, gridLayout):
        print("row, col: " + str(gridLayout.rowCount()) + ", " + str(gridLayout.columnCount()))
        for i in range(gridLayout.rowCount()):
            for j in range(gridLayout.columnCount()):
                if gridLayout.itemAtPosition(i, j) != None and (gridLayout.itemAtPosition(i, j).widget() == self.MainWindow.sender()):
                    return (i, j)

        return (-1, -1)

    def getClazzArgs(self, moduleString):
        # import file
        module   = importlib.import_module("Plugins." + self.plugins[moduleString])
        # get class
        clazz    = getattr(module, moduleString)
        # get class doc
        clazzDoc = clazz.__doc__

        # 从类注释中获取类参数及参数说明，格式@argument: argument doc
        keyValues = {}
        keyValueSelect = []
        if clazzDoc != None:
            for arg in clazzDoc.split("\n"):
                keyValue = arg.strip().split(":")
                if len(keyValue) == 2 and keyValue[0].strip().startswith("@"):
                    if "|" in keyValue[1]:
                        for item in keyValue[1].strip().split("|"):
                            if len(item.strip()) != 0:
                                keyValueSelect.append(item.strip())

                    key = keyValue[0].strip().replace("@", "")
                    matchObj     = re.match(r'(.*)\((.*)\)', key)
                    if matchObj:
                        keyValue = matchObj.groups()

                        if len(keyValueSelect) != 0:
                            keyValues[keyValue[0]] = [keyValue[1], keyValueSelect]
                        else:
                            keyValues[keyValue[0]] = keyValue[1]
        return keyValues

    def PSRunClick(self):
        print("PSRunClick")

        keyValues = self.getKeyValues()
        ret = self.getClazzWithRun(self.pluginsKeys[self.ui.PSPluginsComboBox.currentIndex()], keyValues)

        if len(ret) > 0:
            self.ui.PSInfoPlainTextEdit.setPlainText(ret)

        self.config.setKeyValue("pluginIndex", self.ui.PSPluginsComboBox.currentIndex())
        self.config.saveConfig()

    def getKeyValues(self):
        keyValues = {}
        for i in range(self.ui.PSGridLayout.rowCount()):
            if self.ui.PSGridLayout.itemAtPosition(i, 0) == None:
                continue

            key = self.ui.PSGridLayout.itemAtPosition(i, 0).widget().text()
            # skip blank labels just to take up space
            if len(key) != 0:
                valueWidget = self.ui.PSGridLayout.itemAtPosition(i, 1).widget()
                if isinstance(valueWidget, QLineEdit):
                    value = valueWidget.text()
                    if not os.path.exists(value):
                        if "/" in value or "\\" in value:
                            print("can't find: " + value)
                            value = os.getcwd() + "/" + value
                elif isinstance(valueWidget, QComboBox):
                    value = valueWidget.currentText()
                
                keyValues[key] = value

        print(keyValues)

        return keyValues

    def getClazzWithRun(self, moduleString, args):
        # import file
        module = importlib.import_module("Plugins." + self.plugins[moduleString])
        # get class
        clazz  = getattr(module, moduleString)
        # new class
        obj = clazz(args)

        ret = None
        invert_op = getattr(obj, "start", None)
        if callable(invert_op):
            print(">>> enter plugin start method")
            if len(inspect.signature(invert_op).parameters) > 0:
                ret = invert_op(args)
            else:
                ret = invert_op()
            print("<<< end plugin start method")

        if ret == None:
            return ""
        elif isinstance(ret, list):
            return "\n".join(ret)
        elif isinstance(ret, int) or isinstance(ret, float):
            return str(ret)
        else:
            return ret

    def PSRegexTemplateChanged(self):
        print("PSRegexTemplateChanged")
        regIndex = self.ui.PSRegexTemplateComboBox.currentIndex()

        if Plugin.RegexTemplate[regIndex] == "null":
            print("null")
            self.ui.PSRegexPlainTextEdit.setPlainText("")
        elif Plugin.RegexTemplate[regIndex] == "logcat":
            print("logcat")
            self.ui.PSRegexPlainTextEdit.setPlainText("(\d{2}-\d{2}\s+\d{2}:\d{2}:\d{2}\.\d*)\s+\d+\s+\d+\s+\w+\s+.*: In wakeup_callback: resumed from suspend (\d+)")
        elif Plugin.RegexTemplate[regIndex] == "kernel":
            print("kernel")
            self.ui.PSRegexPlainTextEdit.setPlainText("(\d*\.\d*)\s+:.*(Kernel_init_done)\n(\d*\.\d*)\s+:.*(INIT:late-init)\n(\d*\.\d*)\s+:.*(vold:fbeEnable:START)\n(\d*\.\d*)\s+:.*(INIT:post-fs-data)")
        else:
            print("unsupport regex template")


    def PSPluginsChanged(self):
        pluginsIndex = self.ui.PSPluginsComboBox.currentIndex()

        # clear
        item_list = list(range(self.ui.PSGridLayout.count()))
        item_list.reverse()# 倒序删除，避免影响布局顺序

        for i in item_list:
            item = self.ui.PSGridLayout.itemAt(i)
            self.ui.PSGridLayout.removeItem(item)
            if item.widget():
                item.widget().deleteLater()

        # fill gridlayout
        self.fillePSGridLayout(self.ui.PSGridLayout, self.getClazzArgs(self.pluginsKeys[pluginsIndex]))

        print(self.pluginsKeys[pluginsIndex])

    def PSArgsComboxChanged(self):
        print("PSArgsComboxChanged")
        row, col = self.findWidgetPosition(self.ui.PSGridLayout)
        print("select: %d, %d" % (row, col))

        comboBox: QComboBox = self.ui.PSGridLayout.itemAtPosition(row, col).widget()
        print(comboBox.currentText())

    def getFiles(self, path) :
        for (dirpath, dirnames, filenames) in os.walk(path) :
            dirpath   = dirpath
            dirnames  = dirnames
            filenames = filenames
            return filenames

        return []

    def getPluginFiles(self, dirpath):
        plugins = self.getFiles(dirpath)
        print(plugins)
        # plugins.remove("__init__.py")
        plugins.sort()

        return plugins
