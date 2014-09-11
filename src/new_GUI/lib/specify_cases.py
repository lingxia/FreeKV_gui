#!/usr/bin/env python
# coding=utf-8
 
#*******************************************************************
#* Copyright (c) 2013 Freescale Semiconductor Inc.
#* All rights reserved.
#*
#* Use of Freescale code is governed by terms and conditions
#* stated in the accompanying licensing statement.
#* Description: parse applist.yml and specify case
#*
#* Revision History:
#* -----------------
#* Code Version    YYYY-MM-DD    Author        Description
#* 0.1             2013-12-07    Armand Wang    Create this file
#*******************************************************************
import os,sys
file_path = os.path.dirname(os.path.abspath(__file__))
main_path = os.path.join(file_path, '../')
lib_path = main_path + '/lib/'
sys.path.append(lib_path)
import yaml

def Selector(applist_file,cases_dict):
    '''
    useless function
    '''
    return 0
def Getapplist(applist_file):
    f = open(applist_file)
    app_list = yaml.load(f)
    f.close()
    case_list = []
    for app_item in app_list:
        for casename,value in app_item.items():
            case_list.append(casename)
    return case_list
