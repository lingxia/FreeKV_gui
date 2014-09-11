
#*******************************************************************
#* Copyright (c) 2013 Freescale Semiconductor Inc.
#* All rights reserved.
#*
#* Use of Freescale code is governed by terms and conditions
#* stated in the accompanying licensing statement.
#* Description: FreeMV GUI
#*
#* Revision History:
#* -----------------
#* Code Version    YYYY-MM-DD    Author        Description
#* 0.1             2014-04-6    Armand Wang    Create this file
#*******************************************************************
import os, sys,shutil
import logging
import getopt
import datetime
import cPickle as pickle
import time
import subprocess


file_path = os.path.dirname(os.path.abspath(__file__))
main_path = os.path.join(file_path, '../')
lib_path = main_path + '/lib/'
win32_path = main_path + '/lib/win32api'
sys.path.append(lib_path)
sys.path.append(win32_path)


generator_file = main_path + '/generator/demo_gen.py'
freekv_demo_file = main_path + '/freekv_demo.py'
local_support_file = main_path + '/platform_list.py'
import_support_file = main_path + 'GUI/platform_list.py'
import wx
from get_local_config import Get_IDE_info,Get_serial_info,Get_TRACE32_info
from helper import Helper
from shot import basic_process,senior_process
from win32api import GetShortPathName
from specify_cases import Selector,Getapplist


frame_width = 500
frame_height = 410
pre_button_width = 350
af_button_width = 420
workflow_button_height = 260
static_line_height = 290
hint_width = 20
hint_height = 300

iar = ''
cw10 = ''
uv4 = ''
gcc_arm = ''
demo = ''
mingw = ''
jlink = ''
trace32 = ''

debugger = ''
platform = ''
serial = ''
target = ''
ide = ''
device_type = ''
debug_port = ''
task = ''

applist_file = ''
#*******************************************************************
#* DaPeng IDE selection Frame
#* 
#* 
#*******************************************************************


class IDEFrame(wx.Frame): 
    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent, id, 'FreeKV_demo Configuration Guide  :  Path',size=(frame_width,frame_height),pos=(600,300),style=wx.DEFAULT_FRAME_STYLE)
        panel = wx.Panel(self)
        self.staticLine1 = wx.StaticLine(panel,pos=(20,20),size=(450,1))
        self.staticLine2 = wx.StaticLine(panel,pos=(20,static_line_height),size=(450,1))
        font = wx.Font(12,wx.NORMAL,wx.NORMAL, wx.NORMAL)
        ide_info=Get_IDE_info()
        
        # IAR(checkbox,text,choice,select)
        self.iar_checkbox = wx.CheckBox(panel, -1, 'IAR',pos=(25,40),size=(90,45))
        self.iar_checkbox.SetFont(font)
        self.Bind(wx.EVT_CHECKBOX, self.iar_checkbox_event, self.iar_checkbox)
        self.iar_text=wx.TextCtrl(panel,pos=(120,52),size=(210,25))
        self.iar_text.Enable(False)
        if len(ide_info['iar'])!= 0:
            self.iar_version_dir = {}
            self.iar_version_list = []
            for info in ide_info['iar']:
                self.iar_version_list.append(info['version'])
                self.iar_version_dir[info['version']] = info['path']
            self.iar_choice = wx.Choice(panel, -1, (335, 53), choices=self.iar_version_list)
            self.Bind(wx.EVT_CHOICE, self.iar_choice_event, self.iar_choice)
        self.iar_button_choose = wx.Button(panel, label='select', pos=(420, 50), size=(50, 25))
        self.Bind(wx.EVT_BUTTON, self.iar_choosedir, self.iar_button_choose)


        # uv4(checkbox,text,choice,select)
        self.uv4_checkbox = wx.CheckBox(panel, -1, 'uv4',pos=(25,80),size=(90,45))
        self.uv4_checkbox.SetFont(font)
        self.Bind(wx.EVT_CHECKBOX, self.uv4_checkbox_event, self.uv4_checkbox)
        self.uv4_text=wx.TextCtrl(panel,pos=(120,92),size=(210,25))
        self.uv4_text.Enable(False)
        if len(ide_info['keil'])!= 0:
            self.uv4_version_dir = {}
            self.uv4_version_list = []
            for info in ide_info['keil']:
                self.uv4_version_list.append(info['version'])
                self.uv4_version_dir[info['version']] = info['path']
            self.uv4_choice = wx.Choice(panel, -1, (335, 93), choices=self.uv4_version_list)
            self.Bind(wx.EVT_CHOICE, self.uv4_choice_event, self.uv4_choice)
        self.uv4_button_choose = wx.Button(panel, label='select', pos=(420, 90), size=(50, 25))
        self.Bind(wx.EVT_BUTTON, self.uv4_choosedir, self.uv4_button_choose)

        # cw10(checkbox,text,choice,select)
        self.cw10_checkbox = wx.CheckBox(panel, -1, 'cw10',pos=(25,120),size=(90,45))
        self.cw10_checkbox.SetFont(font)
        self.Bind(wx.EVT_CHECKBOX, self.cw10_checkbox_event, self.cw10_checkbox)
        self.cw10_text=wx.TextCtrl(panel,pos=(120,132),size=(210,25))
        self.cw10_text.Enable(False)
        if len(ide_info['cw10'])!= 0:
            self.cw10_version_dir = {}
            self.cw10_version_list = []
            for info in ide_info['cw10']:
                self.cw10_version_list.append(info['version'])
                self.cw10_version_dir[info['version']] = info['path']
            self.cw10_choice = wx.Choice(panel, -1, (335, 133), choices=self.cw10_version_list)
            self.Bind(wx.EVT_CHOICE, self.cw10_choice_event, self.cw10_choice)
        self.cw10_button_choose = wx.Button(panel, label='select', pos=(420, 130), size=(50, 25))
        self.Bind(wx.EVT_BUTTON, self.cw10_choosedir, self.cw10_button_choose)

        # gcc_arm(checkbox,text,choice,select)
        self.gcc_arm_checkbox = wx.CheckBox(panel, -1, 'gcc_arm',pos=(25,160),size=(90,45))
        self.gcc_arm_checkbox.SetFont(font)
        self.Bind(wx.EVT_CHECKBOX, self.gcc_arm_checkbox_event, self.gcc_arm_checkbox)
        self.gcc_arm_text=wx.TextCtrl(panel,pos=(120,172),size=(210,25))
        self.gcc_arm_text.Enable(False)
        self.gcc_arm_button_choose = wx.Button(panel, label='select', pos=(420, 170), size=(50, 25))
        self.Bind(wx.EVT_BUTTON, self.gcc_arm_choosedir, self.gcc_arm_button_choose)



        # next button
        self.button = wx.Button(panel, label='>>', pos=(af_button_width, workflow_button_height), size=(50, 25))
        self.Bind(wx.EVT_BUTTON, self.gonext, self.button)

        # hint message
        hint=wx.TextCtrl(panel,pos=(hint_width,hint_height),size=(450,70),style=wx.TE_MULTILINE|wx.HSCROLL)
        content = 'Prompt Message:\n'
        content += '** IDE infomation may not complete.\n'
        content += '** Overwrite configuration of last time.\n'
        content += '** Left blank means do nothing.\n'
        content += '** IAR directory e.g. C:/IARSystems/EmbeddedWorkbench6.5.\n'
        content += '** UV4 directory e.g. C:/Keil/UV4.\n'
        content += '** CW10 directory e.g. C:/devsoft/CWMCUv10.5.\n'
        content += '** gcc directory e.g. C:/GNUToolsARMEmbedded/4.72013q3.\n'
        hint.SetValue(content)
        



    def iar_choice_event(self,event):
        self.iar_text.SetValue(self.iar_version_dir[self.iar_version_list[self.iar_choice.GetSelection()]])
        self.iar_version = self.iar_version_list[self.iar_choice.GetSelection()]
    def iar_checkbox_event(self,event):
        if self.iar_checkbox.GetValue():
            self.iar_text.Enable(True)
        else:
            self.iar_text.Enable(False)
    def iar_choosedir(self,event):
        dialog = wx.DirDialog(None, 'Choose iar dir:',style=wx.DD_DEFAULT_STYLE | wx.DD_NEW_DIR_BUTTON)
        if dialog.ShowModal() == wx.ID_OK:
            self.iar_text.SetValue(dialog.GetPath().replace('\\','/'))
            dialog.Destroy()

            
    def uv4_choice_event(self,event):
        self.uv4_text.SetValue(self.uv4_version_dir[self.uv4_version_list[self.uv4_choice.GetSelection()]])
        self.uv4_version = self.uv4_version_list[self.uv4_choice.GetSelection()]
    def uv4_checkbox_event(self,event):
        if self.uv4_checkbox.GetValue():
            self.uv4_text.Enable(True)
        else:
            self.uv4_text.Enable(False)
    def uv4_choosedir(self,event):
        dialog = wx.DirDialog(None, 'Choose uv4 dir:',style=wx.DD_DEFAULT_STYLE | wx.DD_NEW_DIR_BUTTON)
        if dialog.ShowModal() == wx.ID_OK:
            self.uv4_text.SetValue(dialog.GetPath().replace('\\','/'))
            dialog.Destroy()  

    def cw10_choice_event(self,event):
        self.cw10_text.SetValue(self.cw10_version_dir[self.cw10_version_list[self.cw10_choice.GetSelection()]])
        self.cw10_version = self.cw10_version_list[self.cw10_choice.GetSelection()]
    def cw10_checkbox_event(self,event):
        if self.cw10_checkbox.GetValue():
            self.cw10_text.Enable(True)
        else:
            self.cw10_text.Enable(False)
    def cw10_choosedir(self,event):
        dialog = wx.DirDialog(None, 'Choose cw10 dir:',style=wx.DD_DEFAULT_STYLE | wx.DD_NEW_DIR_BUTTON)
        if dialog.ShowModal() == wx.ID_OK:
            self.cw10_text.SetValue(dialog.GetPath().replace('\\','/'))
            dialog.Destroy()  

    def gcc_arm_checkbox_event(self,event):
        if self.gcc_arm_checkbox.GetValue():
            self.gcc_arm_text.Enable(True)
        else:
            self.gcc_arm_text.Enable(False)
    def gcc_arm_choosedir(self,event):
        dialog = wx.DirDialog(None, 'Choose arm-gcc dir:',style=wx.DD_DEFAULT_STYLE | wx.DD_NEW_DIR_BUTTON)
        if dialog.ShowModal() == wx.ID_OK:
            self.gcc_arm_text.SetValue(dialog.GetPath().replace('\\','/'))
            dialog.Destroy()  

    def gonext(self, event):
        if self.iar_text.IsEnabled() and self.iar_text.GetValue()!='':
            global iar
            iar = GetShortPathName(self.iar_text.GetValue())

            
        if self.uv4_text.IsEnabled() and self.uv4_text.GetValue()!='':
            global uv4
            uv4 = GetShortPathName(self.uv4_text.GetValue())


            
        if self.cw10_text.IsEnabled() and self.cw10_text.GetValue()!='':
            global cw10
            cw10 = GetShortPathName(self.cw10_text.GetValue())

            
        if self.gcc_arm_text.IsEnabled() and self.gcc_arm_text.GetValue()!='':
            global gcc_arm
            gcc_arm = GetShortPathName(self.gcc_arm_text.GetValue())
            
        frame2 = RepoFrame(parent=None, id=-1)
        frame2.Show()
        self.Close(True)
        
class RepoFrame(wx.Frame): 
    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent, id, 'FreeKV_demo Configuration Guide  :  Path',size=(frame_width,frame_height),pos=(600,300),style=wx.DEFAULT_FRAME_STYLE)
        panel = wx.Panel(self)
        self.staticLine1 = wx.StaticLine(panel,pos=(20,20),size=(450,1))
        self.staticLine2 = wx.StaticLine(panel,pos=(20,static_line_height),size=(450,1))
        
        # repo label
        repo_label = wx.StaticText(panel, -1, "DEMO ",(20,40))
        font = wx.Font(12,wx.NORMAL,wx.NORMAL, wx.NORMAL)
        repo_label.SetFont(font)
        repo_label2 = wx.StaticText(panel, -1, "MINGW",(20,70))
        repo_label2.SetFont(font)
        repo_label3 = wx.StaticText(panel, -1, "JLINK ",(20,100))
        repo_label3.SetFont(font)
        repo_label4 = wx.StaticText(panel, -1, "TRACE32 ",(20,130))
        repo_label4.SetFont(font)
        

        # repo dir
        self.repo_dir=wx.TextCtrl(panel,pos=(165,40),size=(210,25))
        self.repo_dir2=wx.TextCtrl(panel,pos=(165,70),size=(210,25))
        self.repo_dir3=wx.TextCtrl(panel,pos=(165,100),size=(210,25))
        self.repo_dir4=wx.TextCtrl(panel,pos=(165,130),size=(210,25))
        
        # select buttoon
        self.button = wx.Button(panel, label='select', pos=(380, 40), size=(50, 25))
        self.Bind(wx.EVT_BUTTON, self.choosedir, self.button)
        self.button4 = wx.Button(panel, label='select', pos=(380, 70), size=(50, 25))
        self.Bind(wx.EVT_BUTTON, self.choosedir2, self.button4)
        self.button5 = wx.Button(panel, label='select', pos=(380, 100), size=(50, 25))
        self.Bind(wx.EVT_BUTTON, self.choosedir3, self.button5)
        self.button6 = wx.Button(panel, label='select', pos=(380, 130), size=(50, 25))
        self.Bind(wx.EVT_BUTTON, self.choosedir4, self.button6)

        # next button
        self.button2 = wx.Button(panel, label='>>', pos=(af_button_width, workflow_button_height), size=(50, 25))
        self.Bind(wx.EVT_BUTTON, self.gonext, self.button2)
        # pre button
        self.button3 = wx.Button(panel, label='<<', pos=(pre_button_width, workflow_button_height), size=(50, 25))
        self.Bind(wx.EVT_BUTTON, self.gopre, self.button3)

        # hint message
        hint=wx.TextCtrl(panel,pos=(hint_width,hint_height),size=(450,70),style=wx.TE_MULTILINE|wx.HSCROLL)
        content = 'Prompt Message:\n'
        content += '** Make sure generator_new in MQX dir.\n'
        content += '** Overwrite configuration of last time.\n'
        content += '** Left blank means do nothing.\n'
        content += '** Trace32 is required when use lauterbach.\n'
        content += '** Skip not-need item.\n'
        hint.SetValue(content)

    def gopre(self,event):
        frame_pre_repo = IDEFrame(parent=None, id=-1)
        frame_pre_repo.Show()
        self.Close(True)

    def choosedir(self, event):
        # dialog
        dialog = wx.DirDialog(None, 'Choose MQX dir:',style=wx.DD_DEFAULT_STYLE | wx.DD_NEW_DIR_BUTTON)
        if dialog.ShowModal() == wx.ID_OK:
            self.repo_dir.SetValue(dialog.GetPath().replace('\\','/'))
            dialog.Destroy()
    def choosedir2(self, event):
        # dialog
        dialog = wx.DirDialog(None, 'Choose Mingw dir:',style=wx.DD_DEFAULT_STYLE | wx.DD_NEW_DIR_BUTTON)
        if dialog.ShowModal() == wx.ID_OK:
            self.repo_dir2.SetValue(dialog.GetPath().replace('\\','/'))
            dialog.Destroy()
    def choosedir3(self, event):
        # dialog
        dialog = wx.DirDialog(None, 'Choose Jlink dir:',style=wx.DD_DEFAULT_STYLE | wx.DD_NEW_DIR_BUTTON)
        if dialog.ShowModal() == wx.ID_OK:
            self.repo_dir3.SetValue(dialog.GetPath().replace('\\','/'))
            dialog.Destroy()

    def choosedir4(self, event):
        # dialog
        dialog = wx.DirDialog(None, 'Choose Trace32 dir:',style=wx.DD_DEFAULT_STYLE | wx.DD_NEW_DIR_BUTTON)
        if dialog.ShowModal() == wx.ID_OK:
            self.repo_dir4.SetValue(dialog.GetPath().replace('\\','/'))
            dialog.Destroy()

    def gonext(self, event):
        if self.repo_dir.GetValue() != '':
            global demo
            demo = GetShortPathName(self.repo_dir.GetValue())
        if self.repo_dir2.GetValue() != '':
            global mingw
            mingw = GetShortPathName(self.repo_dir2.GetValue())
        if self.repo_dir3.GetValue() != '':
            global jlink
            jlink = GetShortPathName(self.repo_dir3.GetValue())
        if self.repo_dir4.GetValue() != '':
            global trace32
            trace32 = GetShortPathName(self.repo_dir4.GetValue())

        # store path info
        frame3 = RUNFrame(parent=None, id=-1)
        frame3.Show()
        self.Close(True)

class RUNFrame(wx.Frame): 
    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent, id, 'FreeKV_demo Configuration Guide  :  Settings',size=(frame_width,frame_height),pos=(600,300),style=wx.DEFAULT_FRAME_STYLE)
        panel = wx.Panel(self)
        self.staticLine1 = wx.StaticLine(panel,pos=(20,20),size=(450,1))
        self.staticLine2 = wx.StaticLine(panel,pos=(20,static_line_height),size=(450,1))
        font = wx.Font(12,wx.NORMAL,wx.NORMAL, wx.NORMAL)

        shutil.copyfile(local_support_file,import_support_file)

        # debugger
        debugger_label = wx.StaticText(panel, -1, "debugger ",(20,40))
        debugger_label.SetFont(font)
       
        self.debugger=wx.TextCtrl(panel,pos=(105,40),size=(140,25))
        settings = __import__('platform_list')
        self.debugger_list = settings.debugger_list
        self.debugger_choice = wx.Choice(panel, -1, (260, 40),choices=self.debugger_list)
        self.Bind(wx.EVT_CHOICE, self.debugger_choice_event, self.debugger_choice)


        # platform selection
        platform_label = wx.StaticText(panel, -1, "Platform ",(20,70))
        font = wx.Font(12,wx.NORMAL,wx.NORMAL, wx.NORMAL)
        platform_label.SetFont(font)
       
        self.platform=wx.TextCtrl(panel,pos=(105,70),size=(140,25))
        self.whole_platform_list = []
        try:
            settings = __import__('platform_list')
            self.whole_platform_list = settings.platform_list
        except Exception,e:
            print e
        if len(self.whole_platform_list)!= 0:
            self.platform_choice = wx.Choice(panel, -1, (260, 70), choices=self.whole_platform_list)
            self.Bind(wx.EVT_CHOICE, self.platform_choice_event, self.platform_choice)
        else:
            pass

        # serial port selection
        port_label = wx.StaticText(panel, -1, "SerialPort ",(20,100))
        port_label.SetFont(font)
       
        self.port=wx.TextCtrl(panel,pos=(105,100),size=(140,25))
        self.serial_port_list = Get_serial_info()
        if len(self.serial_port_list)!=0:
            self.serial_choice = wx.Choice(panel, -1, (260, 100), choices=self.serial_port_list)
            self.Bind(wx.EVT_CHOICE, self.serial_choice_event, self.serial_choice)
        else:
            info_label2 = wx.StaticText(panel, -1, "Active serial port not found! ",(20,workflow_button_height))

        # target selection
        target_label = wx.StaticText(panel, -1, "Target ",(20,130))
        target_label.SetFont(font)
       
        self.target=wx.TextCtrl(panel,pos=(105,130),size=(140,25))
        self.whole_target_list = []
        try:
            settings = __import__('platform_list')
            self.target_list = settings.target_list
        except Exception,e:
            print e
        self.target_choice = wx.Choice(panel, -1, (260, 130), choices=self.target_list)
        self.Bind(wx.EVT_CHOICE, self.target_choice_event, self.target_choice)

        # ide selection
        ide_label = wx.StaticText(panel, -1, "IDE ",(20,160))
        ide_label.SetFont(font)
       
        self.ide=wx.TextCtrl(panel,pos=(105,160),size=(140,25))
        self.ide_list = []
        settings = __import__('platform_list')
        self.ide_list = settings.ide_list
        self.ide_choice = wx.Choice(panel, -1, (260, 160), choices=self.ide_list)
        self.Bind(wx.EVT_CHOICE, self.ide_choice_event, self.ide_choice)

        # device type
        dev_label = wx.StaticText(panel, -1, "dev_type ",(20,190))
        dev_label.SetFont(font)
        self.dev=wx.TextCtrl(panel,pos=(105,190),size=(140,25))
        self.dev_list = ['MK64FN1M0xxx12','MK22FN512xxx12','MK22FN128xx10','MK22FN256xxx12','MKV31F512xxx12','MKV31F128xxx10']
        self.dev_choice = wx.Choice(panel, -1, (260, 190), choices=self.dev_list)
        self.Bind(wx.EVT_CHOICE, self.dev_choice_event, self.dev_choice)

        # debug port
        debug_port_label = wx.StaticText(panel, -1, "debug_port ",(20,220))
        debug_port_label.SetFont(font)
        self.debug_port=wx.TextCtrl(panel,pos=(105,220),size=(140,25))
            

        # next button
        self.button = wx.Button(panel, label='>>', pos=(af_button_width, workflow_button_height), size=(50, 25))
        self.Bind(wx.EVT_BUTTON, self.gonext, self.button)
        # pre button
        self.button2 = wx.Button(panel, label='<<', pos=(pre_button_width, workflow_button_height), size=(50, 25))
        self.Bind(wx.EVT_BUTTON, self.gopre, self.button2)

        # hint message
        hint=wx.TextCtrl(panel,pos=(hint_width,hint_height),size=(450,70),style=wx.TE_MULTILINE|wx.HSCROLL)
        content = 'Prompt Message:\n'
        content += '** If no platform checkbox,please check FreeMV/FreeKV directory.\n'
        content += '** If no serial port checkbox,please check board connection.\n'
        content += '** You can add platform out of list for build task.\n'
        content += '** pne may include OpenSDA.\n'
        hint.SetValue(content)


    def platform_choice_event(self,event):
        self.platform.SetValue(self.whole_platform_list[self.platform_choice.GetSelection()])
    def serial_choice_event(self,event):
        self.port.SetValue(self.serial_port_list[self.serial_choice.GetSelection()][3:])
    def debugger_choice_event(self,event):
        self.debugger.SetValue(self.debugger_list[self.debugger_choice.GetSelection()])
    def target_choice_event(self,event):
        self.target.SetValue(self.target_list[self.target_choice.GetSelection()])
    def ide_choice_event(self,event):
        self.ide.SetValue(self.ide_list[self.ide_choice.GetSelection()])
    def dev_choice_event(self,event):
        self.dev.SetValue(self.dev_list[self.dev_choice.GetSelection()])


    def gopre(self,event):
        frame_pre_run = RepoFrame(parent=None, id=-1)
        frame_pre_run.Show()
        self.Close(True)
    def gonext(self, event):
        
        global debugger
        if self.debugger.GetValue()!='':
            debugger = self.debugger.GetValue()
            
        global platform
        if self.platform.GetValue()!='':
            platform = self.platform.GetValue()

        global serial
        if self.port.GetValue()!='':
            serial = self.port.GetValue()
            
        global target
        if self.target.GetValue()!='':
            target = self.target.GetValue()
            
        global ide
        if self.ide.GetValue()!='':
            ide = self.ide.GetValue()
        global device_type
        if self.dev.GetValue()!='':
            device_type = self.dev.GetValue()
        global debug_port
        if self.debug_port.GetValue()!='':
            debug_port = self.debug_port.GetValue()

        basic_process(platform,target,ide,debugger,serial,device_type,debug_port,iar,uv4,cw10,gcc_arm,demo,mingw,jlink)
        
        try:
            os.remove(import_support_file)
        except Exception,e:
            pass
            
        print 'Generating app info,Please wait!'
        try:
            cmd = 'python ' + generator_file + ' ' + platform + ' ' + ide
            Helper.run(cmd)
        except Exception,e:
            print e
        else:
            global applist_file
            applist_file = main_path+'/app_info/'+ platform + '/'+ ide + '/app_list.yml'

        frame4 = GoFrame(parent=None, id=-1)
        frame4.Show()

class GoFrame(wx.Frame): 
    def __init__(self, parent, id):
        wx.Frame.__init__(self, parent, id, 'FreeKV_demo Configuration Guide  :  Select',size=(frame_width+70,frame_height),pos=(600,300),style=wx.DEFAULT_FRAME_STYLE)
        panel = wx.Panel(self)
        self.staticLine1 = wx.StaticLine(panel,pos=(20,20),size=(450,1))
        self.staticLine2 = wx.StaticLine(panel,pos=(20,static_line_height),size=(450,1))
        # hint message
        hint=wx.TextCtrl(panel,pos=(hint_width,hint_height),size=(450,70),style=wx.TE_MULTILINE|wx.HSCROLL)
        content = 'Prompt Message:\n'
        content += '** log directory: [FreeKV_demo]/log\n'
        content += '** Please make sure last task finished before starting a new task.\n'
        content += '** If you want to change configuraiton,Close this window,generate app info again\n'
        hint.SetValue(content)
        self.applist = Getapplist(applist_file)
        
        self.listBox = wx.ListBox(panel, -1, (20, 40), (200, 250), self.applist,wx.LB_SINGLE)
        font = wx.Font(10,wx.NORMAL,wx.NORMAL, wx.NORMAL)
        self.listBox.SetFont(font)
        self.Bind(wx.EVT_LISTBOX, self.selectcase,self.listBox)
        font = wx.Font(12,wx.NORMAL,wx.NORMAL, wx.NORMAL)

        self.build_lib_checkbox = wx.CheckBox(panel, -1, 'build lib',pos=(240,30),size=(80,30))
        self.build_lib_checkbox.SetFont(font)

        self.staticLine3 = wx.StaticLine(panel,pos=(240,70),size=(200,1))
        self.radio1 = wx.RadioButton(panel,-1,'build',pos = (240, 80),size=(160,30)) 
        self.radio2 = wx.RadioButton(panel,-1,'build and run',pos = (240, 110),size=(160,30))
        self.radio3 = wx.RadioButton(panel,-1,'run',pos = (240, 140),size=(160,30))
        self.staticLine4 = wx.StaticLine(panel,pos=(240,170),size=(200,1))
        self.radio1.SetFont(font)
        self.radio2.SetFont(font)
        self.radio3.SetFont(font)
        

        self.app=wx.TextCtrl(panel,pos=(240,190),size=(210,25))

        self.run_button = wx.Button(panel, label='start', pos=(240, 220), size=(70, 40))
        self.Bind(wx.EVT_BUTTON, self.run, self.run_button)

        
    def selectcase(self,event):
        self.app.SetValue(self.applist[self.listBox.GetSelection()])
    def run(self,event):
        if self.app.GetValue()!='':
            if self.build_lib_checkbox.GetValue():
                build_lib = 'yes'
            else:
                build_lib = 'no'
            if self.radio1.GetValue():
                build = 'yes'
                run = 'no'
                build_and_run = 'no'
            elif self.radio2.GetValue():
                build = 'no'
                build_and_run = 'yes'
                run = 'no'
            else:
                build = 'no'
                build_and_run = 'no'
                run = 'yes'
            senior_process(build_lib,build,build_and_run,run,self.app.GetValue())
            
                
            cmd = 'python ' + freekv_demo_file
            subprocess.Popen(cmd)
            

            
        
            
    

    
app = wx.App()
frame = IDEFrame(parent=None, id=-1)
frame.Show()
app.MainLoop()

