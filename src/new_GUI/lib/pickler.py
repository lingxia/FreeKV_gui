#*******************************************************************
#* Copyright (c) 2013 Freescale Semiconductor Inc.
#* All rights reserved.
#*
#* Use of Freescale code is governed by terms and conditions
#* stated in the accompanying licensing statement.
#* Description: pickle operation
#*
#* Revision History:
#* -----------------
#* Code Version    YYYY-MM-DD    Author        Description
#* 0.1             2014-01-11    Armand Wang    Create this file
#*******************************************************************
import os,sys
import cPickle as pickle
import time
import shutil
file_path = os.path.dirname(os.path.abspath(__file__))
main_path = os.path.join(file_path, '..')
lib_path = main_path + '/lib/'
log_path = main_path + '/log/'
temp_path = main_path + '/temp/'
config_path = main_path + '/config/'
sys.path.append(main_path)
sys.path.append(lib_path)
sys.path.append(config_path)
pickle_file = temp_path + 'EnvRecord.pkl'

# {requestid:{plaform:{'app_info':'yes','pre_configure':'yes',ide_target:'yes'}}}

def AddEnvInfo(taskid,platform,ide,target,app_info,pre_configure,build_lib):
    if 'Debug' in target:
        target = 'Debug'
    if 'Release' in target:
        target = 'Release'
    try:
        if os.path.isfile(pickle_file):
            f = file(pickle_file,'rb')
            whole_info = pickle.load(f)
            f.close()
        else:
            whole_info = {}
            
        if whole_info.has_key(taskid):
            if whole_info[taskid].has_key(platform):
                pass
            else:
                whole_info[taskid][platform] = {}
            
        else:
            whole_info[taskid] = {}
            whole_info[taskid][platform] = {}
        
        if app_info == 'yes':
            whole_info[taskid][platform][ide] = 'yes'
        if pre_configure == 'yes':
            whole_info[taskid][platform]['pre_configure'] = 'yes'
        if build_lib == 'yes':
            whole_info[taskid][platform][ide+'_'+target] = 'yes'

        f = file(pickle_file,'wb')
        pickle.dump(whole_info,f,True)
        f.close()
    except Exception,e:
        print e
        return 1
    else:
        return 0
