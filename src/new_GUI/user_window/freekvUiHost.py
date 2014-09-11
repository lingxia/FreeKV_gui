from PyQt4 import QtCore, QtGui
import sys,os,datetime
import subprocess, threading

file_path = os.path.dirname(os.path.abspath("__file__"))
main_path = os.path.join(file_path,"../")
lib_path = main_path + "/lib/"
pic_path = main_path + "/pic/"
designer_path = main_path + "/designer_window/"
config_path = main_path +  "../" +"config/"
app_path = main_path + "../" + "app_info/"
appList_path = config_path + "/app_list/"

sys.path.append(lib_path)
sys.path.append(pic_path)
sys.path.append(designer_path)


from freekvUi import Ui_freekvUi
import platform_list
import yaml
from get_local_config import Get_IDE_info
import win32api
from getconfig import Getconfig

config_file = config_path + "config.xml"
config = Getconfig(config_file)

class freekvConfig(QtGui.QMainWindow):
    def __init__(self, parent = None):
        QtGui.QWidget.__init__(self, parent)
        self.freekvWin = Ui_freekvUi()
        self.freekvWin.setupUi(self)
        self.setFixedSize(self.width(),self.height())
        
#*********** MenuBar, ToolBar, StatusBar ************         
        self.menuBar = self.menuBar()
        self.toolBar = self.addToolBar("ToolBar")
        self.statuBar = self.statusBar()
        
#********************* Actions **********************        
        self.saveAct = QtGui.QAction(QtGui.QIcon(pic_path + "/save_icon.png"),"Save",self)
        self.saveAct.setShortcut("Ctrl+S")
        self.saveAct.setStatusTip("Save the Configuration File !")
        self.saveAct.whatsThis()
        self.connect(self.saveAct, QtCore.SIGNAL("triggered()"),self.saveConfig)
        self.connect(self.saveAct, QtCore.SIGNAL("triggered()"),self.saveEvent)
        
        self.quitAct = QtGui.QAction(QtGui.QIcon(pic_path + "/exit_icon.png"),"Quit",self)
        self.quitAct.setShortcut("Ctrl+Q")
        self.quitAct.setStatusTip("Quit the Configuration without saving the File !")
        self.quitAct.whatsThis()
        self.connect(self.quitAct, QtCore.SIGNAL("triggered()"),self.close)
               
#****************add Menus and Actions**************
        self.fileMenu = self.menuBar.addMenu("File")
        self.fileMenu.addAction(self.saveAct)
        self.fileMenu.addAction(self.quitAct)        
        self.toolBar.addAction(self.saveAct)
        self.toolBar.addAction(self.quitAct)
        
        
        self.platformApp = config.getValue("platform")
        self.freekvDir = config.getValue("psdk_kptk_dir")
        self.appList = []
        self.unify_data_file = self.freekvDir + "/generator_psdk/psdk_ide_project/" + "unify_data_" + self.platformApp + ".yml"
        self.unify_data = os.path.isfile(self.unify_data_file)
   
        self.saveFlag = True
        self.initCombobox()
        self.preConfig()        
        
        self.connect(self.freekvWin.buildCheckBox, QtCore.SIGNAL("stateChanged(int)"), self.selectBuild)
        self.connect(self.freekvWin.runCheckBox, QtCore.SIGNAL("stateChanged(int)"),self.selectRun)
        self.connect(self.freekvWin.ideComboBox, QtCore.SIGNAL("activated (int)"),self.initIde)
        self.connect(self.freekvWin.startButton, QtCore.SIGNAL("clicked()"),self.start)
        self.connect(self.freekvWin.platformComboBox, QtCore.SIGNAL("activated(int)"),self.appClean)
        
#***************some event with messagebox********                   
    def saveEvent(self):
        if self.saveFlag == True:
            QtGui.QMessageBox.information(self,"Information",\
                                        "The Configuration File has been Saved Successfully !", QtGui.QMessageBox.Ok)
        elif self.saveFlag == False:
            self.saveFlag = True



#***************init of combo box*****************
    def initCombobox(self):
        ide = platform_list.ide_list
        target = platform_list.target_list
#        suite = platform_list.test_suite
        platform = platform_list.platform_list
        debugger = platform_list.debugger_list
        
        ide_len = len(ide)
        target_len = len(target)
#        suite_len = len(suite)
        platform_len = len(platform)
        debugger_len = len(debugger) 
        
        platformConfiged = config.getValue("platform")
        
        for num in range(0,ide_len):
            self.freekvWin.ideComboBox.addItem("")
            self.freekvWin.ideComboBox.setItemText(num, ide[num])
        
        for num in range(0,target_len):
            self.freekvWin.targetComboBox.addItem("")
            self.freekvWin.targetComboBox.setItemText(num,target[num])
        
#        for num in range(0,suite_len):
#            self.freekvWin.testsuiteComboBox.addItem("")
#            self.freekvWin.testsuiteComboBox.setItemText(num,suite[num])
            
        for num in range(0,platform_len):
            self.freekvWin.platformComboBox.addItem("")
            self.freekvWin.platformComboBox.setItemText(num,platform[num])
            
        for num in range(0,debugger_len):
            self.freekvWin.debuggerComboBox.addItem("")
            self.freekvWin.debuggerComboBox.setItemText(num,debugger[num])  

        if self.unify_data == False:
            pass
        elif self.unify_data == True:
            print "Parsing unify data,  waiting for about 5 to 20 seconds please ..."
            timeFileDir = appList_path + "time_" + platformConfiged + ".txt"
            appListDir =  appList_path + "applist_" + platformConfiged + ".yml"

            cdateCurrent = os.path.getmtime(self.unify_data_file)
            date = datetime.datetime.fromtimestamp(cdateCurrent)
            timeCurrent = date.strftime('%Y-%m-%d %H:%M:%S')

            if os.path.isfile(timeFileDir) == True:
                timefileR = open(timeFileDir,"r")
                timefileCom = timefileR.read()
                timefileR.close()
                if timefileCom == timeCurrent and os.path.isfile(appListDir) == True:
                    tfile = open(appListDir)
                    tout = yaml.load(tfile)
                    for item in tout:
                        self.appList.append(item)
                else:
                    funify = open(self.unify_data_file)
                    out = yaml.load(funify)
                    for item in out:
                        self.appList.append(item)
                    appListFile = file(appListDir,"w")
                    yaml.dump(self.appList, appListFile, default_flow_style=False)
                    appListFile.close()
                    timefileW = open(timeFileDir,"w")
                    timefileW.write(timeCurrent)
                    timefileW.close()
            elif os.path.isfile(timeFileDir) == False:
                funify = open(self.unify_data_file)
                out = yaml.load(funify)
                for item in out:
                    self.appList.append(item)
                appListFile = file(appListDir,"w")
                yaml.dump(self.appList, appListFile, default_flow_style=False)
                appListFile.close()
                timefileN = file(timeFileDir,"w")
                timefileN.write(timeCurrent)
                timefileN.close()
        
        self.appListLen = len(self.appList)
        for num in range(0,self.appListLen):
            self.freekvWin.appComboBox.addItem("")
            self.freekvWin.appComboBox.setItemText(num,self.appList[num])


#************************app clean***************************
    def appClean(self):
        platform = self.freekvWin.platformComboBox.currentText()
        platformStr = platform.__str__()
        unifyFile = self.freekvDir + "/generator_psdk/psdk_ide_project/" + "unify_data_" + platformStr + ".yml"
        appFile = appList_path + "applist_" + platformStr + ".yml"
        timeFile = appList_path + "time_" + platformStr + ".txt"
        
        if os.path.isfile(unifyFile) == True and os.path.isfile(appFile) == True and os.path.isfile(timeFile) == True:
            cdateCurrent = os.path.getmtime(unifyFile)
            date = datetime.datetime.fromtimestamp(cdateCurrent)
            timeCurrent = date.strftime('%Y-%m-%d %H:%M:%S')
                        
            timefileR = open(timeFile,"r")
            timefileCom = timefileR.read()
            timefileR.close()
            
            if timeCurrent == timefileCom:
                for num in range(0,self.appListLen):
                    self.freekvWin.appComboBox.removeItem(num)
                del self.appList[:]

                tfile = open(appFile)
                tout = yaml.load(tfile)
                for item in tout:
                    self.appList.append(item)
                self.appListLen = len(self.appList)
                for num in range(0,self.appListLen):
                    self.freekvWin.appComboBox.addItem("")
                    self.freekvWin.appComboBox.setItemText(num,self.appList[num])
            else:
                self.freekvWin.appComboBox.clear()
        else:
            self.freekvWin.appComboBox.clear()


#****************select test type: build or run*************
    def selectBuild(self):
        buildCheckStatus = self.freekvWin.buildCheckBox.checkState()
        if buildCheckStatus == QtCore.Qt.Checked:
            config.setValue("build", "yes")
            config.setValue("run","no")
            config.setValue("build_and_run","no")
            config.setValue("sync_enable","no")
            self.freekvWin.runCheckBox.setCheckable(False)
            self.freekvWin.freekvTabWidget.setTabEnabled(2,False)            
        elif buildCheckStatus != QtCore.Qt.Checked:
            self.freekvWin.runCheckBox.setCheckable(True)
            self.freekvWin.freekvTabWidget.setTabEnabled(2,True)

            
    def selectRun(self):
        runCheckStatus = self.freekvWin.runCheckBox.checkState()
        if runCheckStatus == QtCore.Qt.Checked:
            config.setValue("build", "no")
            config.setValue("run","yes")
            config.setValue("build_and_run","no")
            config.setValue("build_lib","no")
            config.setValue("pre_configure", "no")
            config.setValue("sync_enable","no")
            config.setValue("app_info", "no")
            self.freekvWin.buildCheckBox.setCheckable(False)
            self.freekvWin.freekvTabWidget.setTabEnabled(1,False)
            
            binDir = config.getValue("binary")
            self.freekvWin.binaryLineEdit.setText(binDir)
            
        elif runCheckStatus != QtCore.Qt.Checked:
            self.freekvWin.buildCheckBox.setCheckable(True)
            self.freekvWin.freekvTabWidget.setTabEnabled(1,True) 
    
#************************ide init*********************
    def initIde(self):
            ideSelect = self.freekvWin.ideComboBox.currentText()
            ide_info = Get_IDE_info()
#            print ide_info
            
            if ideSelect.__str__() == "uv4":
                ideSelected = "keil"
                ideList = ide_info[ideSelected]
            elif ideSelect.__str__() == "kds":
                self.freekvWin.ideVersionComboBox.clear()
                self.freekvWin.ideLineEdit.clear()
                return
            else:
                ideSelected = ideSelect.__str__()
                ideList = ide_info[ideSelected]
            
            ideLen = len(ideList)
            if ideLen == 0:
                self.freekvWin.ideVersionComboBox.clear()
                self.freekvWin.ideLineEdit.clear()
            elif ideLen !=0 :
                for num in range(0, ideLen):
                    self.freekvWin.ideVersionComboBox.removeItem(num)
                    self.freekvWin.ideVersionComboBox.addItem("")
                    self.freekvWin.ideVersionComboBox.setItemText(num,ideList[num]["version"])
                
                ideIndex = self.freekvWin.ideVersionComboBox.currentIndex()
                idePath = ideList[ideIndex]["path"]
                self.freekvWin.ideLineEdit.setText(idePath)    
                    
#*******************get pre configuration*************
    def preConfig(self):       
        ide = platform_list.ide_list
        target = platform_list.target_list
#        suite = platform_list.test_suite
        platform = platform_list.platform_list
        debugger = platform_list.debugger_list
        
#        preTestsuite = config.getValue("test_type")
#        self.freekvWin.testsuiteComboBox.setCurrentIndex(suite.index(preTestsuite))
        
        preApp = config.getValue("app")
        if preApp in self.appList:
            self.freekvWin.appComboBox.setCurrentIndex(self.appList.index(preApp))
        else:
            self.freekvWin.appComboBox.clearEditText()
        
                
        prePlatform = config.getValue("platform")
        self.freekvWin.platformComboBox.setCurrentIndex(platform.index(prePlatform))
        
#        preMinGW = config.getValue("mingw")
#        self.freekvWin.mingwLineEdit.setText(preMinGW)
#        self.freekvWin.mingwLineEdit.setCursorPosition(0)
        
        preTestDir = config.getValue("psdk_kptk_dir")
        self.freekvWin.testLineEdit.setText(preTestDir)
        self.freekvWin.testLineEdit.setCursorPosition(0)
        
        preTarget = config.getValue("target")
        self.freekvWin.targetComboBox.setCurrentIndex(target.index(preTarget))
        
        preIde = config.getValue("IDE")
        self.freekvWin.ideComboBox.setCurrentIndex(ide.index(preIde))
        preIdeDir = config.getValue(preIde)
        self.freekvWin.ideLineEdit.setText(preIdeDir)
        self.freekvWin.ideLineEdit.setCursorPosition(0)
        preIdeVer = config.getAttr(preIde, "version")
        self.freekvWin.ideVersionComboBox.setEditText(preIdeVer)
        
        preDebugger = config.getValue("debugger")
        self.freekvWin.debuggerComboBox.setCurrentIndex(debugger.index(preDebugger))
        preDebuggerDir = config.getValue(preDebugger)
        if preDebuggerDir == None:
            pass
        else: 
            self.freekvWin.debuggerLineEdit.setText(preDebuggerDir)
            self.freekvWin.debuggerLineEdit.setCursorPosition(0)
            
        preBinary = config.getValue("binary")
        self.freekvWin.binaryLineEdit.setText(preBinary)
        self.freekvWin.binaryLineEdit.setCursorPosition(0)
        
        preSerialPort = config.getAttr(prePlatform, "serial_port")
        preDebugPort = config.getAttr(prePlatform, "debug_port")
        self.freekvWin.serialLineEdit.setText(preSerialPort)
        self.freekvWin.debugPortLineEdit.setText(preDebugPort)

#************************save build*******************
    def saveConfig(self):
#        testtype = self.freekvWin.testsuiteComboBox.currentText()
#        config.setValue("test_type", testtype.__str__())
        
        app = self.freekvWin.appComboBox.currentText()
        if app != "":
            config.setValue("app", app.__str__())
        elif app == "":
            pass        
        
        currentPlatform = self.freekvWin.platformComboBox.currentText()
        platform = currentPlatform.__str__()
        config.setValue("platform", platform)
        
#        try:
#            mingwDir = self.freekvWin.mingwLineEdit.text()
#            if mingwDir != "":
#                mingwShrot = win32api.GetShortPathName(mingwDir.__str__())
#                config.setValue("mingw", mingwShrot)
#            elif mingwDir == "":
#                pass
#        except Exception:
#            pass
        
        buildCheckStatus = self.freekvWin.buildCheckBox.checkState()
        runCheckStatus = self.freekvWin.runCheckBox.checkState()
        if buildCheckStatus == QtCore.Qt.Checked:
            testDir = self.freekvWin.testLineEdit.text()
            if testDir != "":
                config.setValue("psdk_kptk_dir", testDir.__str__())
            elif testDir == "":
                pass
            
            buildLib = self.freekvWin.libComboBox.currentText()
            config.setValue("build_lib", buildLib.__str__())
            
            target = self.freekvWin.targetComboBox.currentText()
            config.setValue("target", target.__str__())
            
            ideSelect = self.freekvWin.ideComboBox.currentText()
            config.setValue("IDE", ideSelect.__str__())
            
            ideDir = self.freekvWin.ideLineEdit.text()
            if ideDir == "":
                pass
            else:
                try:
                    ideDirShort = win32api.GetShortPathName(ideDir.__str__())
                    config.setValue(ideSelect.__str__(), ideDirShort)
                except:
                    QtGui.QMessageBox.warning(self,"Warning",\
                                        "NO such IDE path, make sure the IDE version and path right !", QtGui.QMessageBox.Ok)
                    self.saveFlag = False
            
            ideVer = self.freekvWin.ideVersionComboBox.currentText()
            config.setAttr(ideSelect.__str__(), "version", ideVer.__str__())
            
            project = self.freekvWin.projectComboBox.currentText()
            projectStr = project.__str__()
            unify_data = os.path.isfile(testDir.__str__() + "/generator_psdk/psdk_ide_project/" + "unify_data_" + platform + ".yml")
                    
            if projectStr == "no" and unify_data == False:                  
                reply = QtGui.QMessageBox.warning(self, 'Warning', \
                                          'The project was not be detected ! Do you want to generate a new project ?',\
                                                  QtGui.QMessageBox.Yes, QtGui.QMessageBox.No)
                self.saveFlag = False
                if reply == QtGui.QMessageBox.Yes:
                    config.setValue("pre_configure", "yes")
                    self.freekvWin.projectComboBox.setCurrentIndex(0)
                elif reply == QtGui.QMessageBox.No:
                    config.setValue("pre_configure", "no")
            else:
                config.setValue("pre_configure", projectStr)
                
            
            app_info = os.path.isfile(app_path + "/" + platform + "/" + ideSelect.__str__() + "/app_list.yml" )
#            print app_info
            if app_info == True:
                config.setValue("app_info", "no")
            elif app_info == False:
                config.setValue("app_info", "yes")                       
                
        elif runCheckStatus == QtCore.Qt.Checked:
            debugger = self.freekvWin.debuggerComboBox.currentText()
            config.setValue("debugger", debugger.__str__())
            debuggerDir = self.freekvWin.debuggerLineEdit.text()
            if debuggerDir != "":
                try:
                    debuggerShort = win32api.GetShortPathName(debuggerDir.__str__())
                    config.setValue(debugger.__str__(), debuggerShort)
                except:
                    QtGui.QMessageBox.warning(self,"Warning",\
                                        "NO such Debugger path, make sure the Debugger path right !", QtGui.QMessageBox.Ok)
                    self.saveFlag = False
                    
            elif debuggerDir == "":
                pass
                        
            serialPort = self.freekvWin.serialLineEdit.text()
            debugPort = self.freekvWin.debugPortLineEdit.text()
            
            config.setAttr(platform, "serial_port", serialPort.__str__())
            config.setAttr(platform, "debug_port", debugPort.__str__())
            
            binaryDir = self.freekvWin.binaryLineEdit.text()
            if binaryDir != "":
                try:
                    binaryShort = win32api.GetShortPathName(binaryDir.__str__())
                    config.setValue("binary", binaryShort)
                except:
                    QtGui.QMessageBox.warning(self,"Warning",\
                                        "NO such Binary path, make sure the Binary path right !", QtGui.QMessageBox.Ok)
                    self.saveFlag = False                    
            elif binaryDir == "":
                pass
        else:
            pass
        
    def start(self):
        start_path = win32api.GetShortPathName(main_path + "../")
        command = "python " + start_path + "freekv.py"   
        def startPro():
            sub = subprocess.Popen(command)
            result = sub.wait()
            if result == 0:
#                self.setEnabled(True)
                self.setVisible(True)
#                self.setWindowFlags(QtCore.Qt.WindowFlags()|QtCore.Qt.FramelessWindowHint|QtCore.Qt.WindowTitleHint)                       
        tStart = threading.Thread(target = startPro)
        tStart.start()
#        self.setEnabled(False)
#        self.setDisabled(True)        
        self.setVisible(False)

        
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    testWin = freekvConfig()
    testWin.show()
    sys.exit(app.exec_())