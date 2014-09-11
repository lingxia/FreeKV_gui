#!/usr/bin/env python
# coding=utf-8
 
#*******************************************************************
#* Copyright (c) 2013 Freescale Semiconductor Inc.
#* All rights reserved.
#*
#* Use of Freescale code is governed by terms and conditions
#* stated in the accompanying licensing statement.
#* Description: get local config
#*
#* Revision History:
#* -----------------
#* Code Version    YYYY-MM-DD    Author        Description
#* 0.1             2014-2-15    Armand Wang    Create this file
#*******************************************************************
import os, sys
import logging
import socket
import re
import subprocess

file_path = os.path.dirname(os.path.abspath(__file__))
main_path = os.path.join(file_path, '/../')
import _winreg


def Get_IDE_info():
    '''
    return ide info {keil:[{path:xxxxx,version:xxx,'short_path':xxx}],iar:[{path:xxxxx,version:xxx,'short_path':xxx}],cw10:[{path:xxxxx,version:xxx,'short_path':xxx}]}
    or {keil:['not found'],iar:['not found'],cw10:['not found']}
    '''
    # only one keil info on one PC
    ide_info = {}
    ide_info['keil']=[]
    ide_info['iar']=[]
    ide_info['cw10']=[]
    try:
        key = _winreg.OpenKey(_winreg.HKEY_LOCAL_MACHINE,r"SOFTWARE\Keil\Products\MDK")
        uv4_path,type = _winreg.QueryValueEx(key,"Path")
        uv4_version,type = _winreg.QueryValueEx(key,"Version")
        uv4_path = uv4_path.replace('\\','/')
        info_dic = {'path':uv4_path.replace('ARM','UV4'),'version':uv4_version}
    except Exception,e:
        pass
    else:
        ide_info['keil'].append(info_dic)

    # may more than one iar info on one PC
    try:
        key = _winreg.OpenKey(_winreg.HKEY_LOCAL_MACHINE,r"SOFTWARE\IAR Systems\Embedded Workbench\5.0\Locations")
        try:
            i=0
            while 1:
                subkey_name = r"SOFTWARE\IAR Systems\Embedded Workbench\5.0\Locations" + "\\" + _winreg.EnumKey(key,i)
                subkey = _winreg.OpenKey(_winreg.HKEY_LOCAL_MACHINE,subkey_name)
                iar_path,type = _winreg.QueryValueEx(subkey,"InstallPath")
                iar_path = iar_path.replace('\\','/')
                try:
                    subkey_name = r"SOFTWARE\IAR Systems\Embedded Workbench\5.0\Locations" + "\\" + _winreg.EnumKey(key,i) + r"\Product Families\ARM\10.EW"
                    subkey = _winreg.OpenKey(_winreg.HKEY_LOCAL_MACHINE,subkey_name)
                    iar_version,type = _winreg.QueryValueEx(subkey,"Version")
                except Exception,e:
                    iar_version = 'unknown'
                info_dic = {'path':iar_path,'version':iar_version}
                ide_info['iar'].append(info_dic)
                i+=1
        except WindowsError,e:
            pass
    except Exception,e:
        pass

    # may more than one cw10 info on one PC
    try:
        key = _winreg.OpenKey(_winreg.HKEY_LOCAL_MACHINE,r"SOFTWARE\Freescale\CodeWarrior\Product Versions")
        try:
            i=0
            while 1:
                subkey_name = r"SOFTWARE\Freescale\CodeWarrior\Product Versions" + "\\" + _winreg.EnumKey(key,i)
                subkey = _winreg.OpenKey(_winreg.HKEY_LOCAL_MACHINE,subkey_name)
                cw10_path,type = _winreg.QueryValueEx(subkey,"Path")
                cw10_path = cw10_path.replace('\\','/')
                cw10_version,type = _winreg.QueryValueEx(subkey,"Version")
                info_dic = {'path':cw10_path,'version':cw10_version}
                ide_info['cw10'].append(info_dic)
                i+=1
        except WindowsError,e:
            pass
    except Exception,e:
        pass
    # arm-gcc,ds5 land blank
    ide_info['gcc_arm'] = []
    return ide_info
def Get_TRACE32_info():
    '''
    return{'exist':'yes','path':xxx,'short_path':xxx}
    or {'exist':'no','path':xxx,'short_path':xxx}
    '''
    trace32_info = {}
    try:
        key = _winreg.OpenKey(_winreg.HKEY_LOCAL_MACHINE,r"SOFTWARE\Microsoft\Windows\CurrentVersion\App Paths\TRACE32")
        trace32_path,type = _winreg.QueryValueEx(key,"Path")
        trace32_info['path'] = trace32_path.replace('\\','/')
        trace32_info['exist'] = 'yes'
    except Exception,e:
        trace32_info['exist'] = 'no'
    return trace32_info

def Get_serial_info():
    '''
    return [COM1,COM2,...]
    '''
    serial_info = []
    try:
        key = _winreg.OpenKey(_winreg.HKEY_LOCAL_MACHINE,r"HARDWARE\DEVICEMAP\SERIALCOMM")
        try:
            i=0
            while 1:
                serial_info.append( _winreg.EnumValue(key,i)[1])
                i+=1
        except WindowsError,e:
            pass
    except Exception,e:
        pass
    return serial_info
    

#print Get_IDE_info()
#print Get_STAF_info()
#print Get_TRACE32_info()
#print Get_BasicSoftware_info()
#print Get_DP_info()
#print Get_Gcc_info('C:/GNUToolsARMEmbedded/4.72013q3')
