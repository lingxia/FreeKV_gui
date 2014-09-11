# coding=utf-8
 
#*******************************************************************
#* Copyright (c) 2013 Freescale Semiconductor Inc.
#* All rights reserved.
#*
#* Use of Freescale code is governed by terms and conditions
#* stated in the accompanying licensing statement.
#* Description: Plugin Map
#*
#* Revision History:
#* -----------------
#* Code Version    YYYY-MM-DD    Author        Description
#* 0.1             2014-03-27    Armand Wang    Create this file
#*******************************************************************

task_map ={

    'build'               :[{'builder':3}],
    'run'                 :[{'auto_runner':4}],
    'build_and_run'       :[{'builder':3},{'auto_runner':4}],
    }
extension_map={
    'sync'                :{'sync':0},
    'app_info'            :{'app_info':2},
    'pre_configure'       :{'pre_configure':1}
    }

lib_keypath_map={
    'twrk64f120m'         :'K64F12',
    'frdmk64f120m'        :'K64F12',
    'twrk22f120m'         :'K22F51212',
    'frdmk22f120m'        :'K22F51212',
    'twrk22f120m128r'     :'K22F12810',
    'twrk22f120m256r'     :'K22F25612',
    'twrkv31f120m'        :'KV31F51212',
    'twrkv31f120m128r'    :'KV31F12810',
    'twrkv31f120m256r'    :'KV31F25612',
    'twrk24f120m'         :'K24F25612',
    'frdmkl03z48m'        :'KL03Z4',
    'twrkv30f100m'        :'KV30F12810',
    'twrkl43z48m'         :'KL43Z4',
    'frdmkl43z48m'        :'KL43Z4',
    'frdmk22f120mk02'     :'K02F12810',
    'twrk22f120mk02'      :'K02F12810',
    'twrkv30f100mk02'     :'K02F12810',
    'twrkv31f120mkv30'    :'KV30F12810',
    'twrkv30f100mk0264'   :'K02F12810',
    
    }
# 1:key plugin 
# value 1 plugin executed failed ,will inspact other key plugin.
plugin_sync_map = {
    
    'app_info'            : '1',# update code
    'sync'                : '1',# update code
    'pre_configure'       : '1',# generate project file
    'builder'             : '1',# build single app
    'auto_runner'         : '1',# download app and judge reault automatically
    'builder_runner'      : '1',# for build and autorun(call builder and auto_runner)
    }
