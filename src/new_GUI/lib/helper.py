#!/usr/bin/env python
# coding=utf-8

#*******************************************************************
#* Copyright (c) 2013 Freescale Semiconductor Inc.
#* All rights reserved.
#*
#* Use of Freescale code is governed by terms and conditions
#* stated in the accompanying licensing statement.
#* Description: helper function.
#*
#* Revision History:
#* -----------------
#* Code Version    YYYY-MM-DD    Author        Description
#* 0.1             2013-06-08    Larry Shen    Create this file
#*******************************************************************
import os, sys
file_path = os.path.dirname(os.path.abspath(__file__))
main_path = os.path.join(file_path, '..')
win32_path = main_path + '/lib/win32api_local'
sys.path.append(win32_path)


from win32api import GetShortPathName
import os, sys
import subprocess
import time
import threading
import socket
import logging

killed = 0
class Helper:
    @staticmethod
    def run(cmd, timeout=30):
        global killed
        killed = 0
        def timeout_trigger(sub_process):
            global killed
            killed = 1
            logging.info('timeout function trigger')
            os.system('taskkill /T /F /pid '+ str(sub_process.pid))

        timeout = float(timeout)
        logging.info(cmd)
        p = subprocess.Popen(cmd, 0, None, None, None, None, shell=True)
        t = threading.Timer(timeout*60, timeout_trigger, args=(p,))
        t.start()
        p.wait()
        t.cancel()

        ret_val = p.returncode
        if killed:
            return 'TIMEOUT'
        return ret_val

    @staticmethod
    def interact_run(cmd, timeout):
        def timeout_trigger(sub_process):
            logging.info('timeout function trigger')
            os.system('taskkill /T /F /pid '+ str(sub_process.pid))

        logging.info(cmd)
        p = subprocess.Popen(cmd, 0, None, None, None, subprocess.PIPE,shell=True)
        t = threading.Timer(timeout*60, timeout_trigger, args=(p,))
        t.start()
        p.wait()
        t.cancel()

        ret_val = p.returncode
        ret_info = p.stderr.readline()

        return (ret_val, ret_info)
    @staticmethod
    def thread_run(cmd):
        p = subprocess.Popen(cmd)
        return p.pid

    @staticmethod
    def win_process_kill(exe_name):
        Helper.system('taskkill /F /IM ' + '"' + exe_name + '"')

    @staticmethod
    def is_port_open(port, ip='127.0.0.1'):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            s.connect((ip, int(port)))
            s.shutdown(2)
            return True
        except:
            return False

    @staticmethod
    def system(cmd):
        logging.info(cmd)
        sys.stdout.flush()
        ret_val = os.system('call ' + cmd)
        return ret_val
    @staticmethod
    def Format_change(origin_string):
        return origin_string.replace('\\','/')
    @staticmethod
    def get_short_path(path):
        return GetShortPathName(path)
    @staticmethod
    def halt_device_cmd(net_port):
        halt_script = main_path + "/auto_handle/dummy_binary/gdb.init"
        content = open(halt_script).read().replace('2331',net_port)
        specify_halt_script = main_path + "/temp/"+net_port
        f = open(specify_halt_script,'w')
        f.write(content)
        f.close()
        return "\"" + '%gdb_run' + "\" -x \"" + specify_halt_script + "\""
    @staticmethod
    def download_k70_cmd(k70_net_port,binary,k70_debug_port):
        k70_script = main_path + "/auto_handle/dummy_binary/k70_gdb.init"
        content = open(k70_script).read().replace('k70_binary',binary)
        content = content.replace('2331',k70_net_port)
        # use jlink s/n num as gdb script name for parallel run
        k70_execute_script = main_path + "/temp/"+k70_debug_port
        f = open(k70_execute_script,'w')
        f.write(content)
        f.close()
        return "\"" + '%gdb_run' + "\" -x \"" + k70_execute_script + "\""
    @staticmethod
    def start_gdb_server(gdb_server_exe,debug_port,jlink_interface,net_port):
        pid = Helper.thread_run(gdb_server_exe + ' -select usb=' + debug_port + ' -if ' + jlink_interface + ' -port ' + net_port  + ' -singlerun' + ' -speed 100' )
        time.sleep(2)
        return pid,0
    @staticmethod
    def get_cmd_output(cmd):
        r = os.popen(cmd).read()
        return r
    @staticmethod
    def win_pid_kill(pid):
        Helper.system('taskkill /T /F /pid ' + '"' + pid + '"')


