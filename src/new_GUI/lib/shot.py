
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
import re


file_path = os.path.dirname(os.path.abspath(__file__))
main_path = os.path.join(file_path, '../')
lib_path = main_path + '/lib/'
sys.path.append(lib_path)

config_file = main_path + '/config/config.xml'

from getconfig import Getconfig
config = Getconfig(config_file)

def basic_process(platform,target,ide,debugger,serial,device_type,debug_port,iar,uv4,cw10,gcc_arm,demo,mingw,jlink):
    if platform!='':
        config.setValue('platform',platform)
    if target!='':
        config.setValue('target',target)
    if ide!='':
        config.setValue('IDE',ide)
    if debugger!='':
        config.setValue('debugger',debugger)
    if mingw!='':
        config.setValue('mingw',mingw)
    if jlink!='':
        config.setValue('jlink',jlink)

    config.setValue('sync','no')
    config.setValue('pre_configure','no')
    config.setValue('app_info','yes')
    if demo!='':
        config.setValue('psdk_demo_dir',demo)
    if iar!='':
        config.setValue('iar',iar)
    if gcc_arm!='':
        config.setValue('gcc_arm',gcc_arm)
    try:
        if uv4!='':
            config.setValue('uv4',uv4)
        if cw10!='':
            config.setValue('cw10',cw10)
    except Exception,e:
        pass
    if platform!='' and device_type!='' and debug_port!='':
        config.setAttr(platform,'serial_port',serial)
        config.setAttr(platform,'device_type',device_type)
        config.setAttr(platform,'debug_port',debug_port)



    

def senior_process(build_lib,build,build_and_run,run,app):
    config.setValue('build_lib',build_lib)
    config.setValue('build',build)
    config.setValue('build_and_run',build_and_run)
    config.setValue('run',run)
    config.setValue('app',app)
