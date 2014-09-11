#!/usr/bin/env python
# coding=utf-8

#*******************************************************************
#* Copyright (c) 2013 Freescale Semiconductor Inc.
#* All rights reserved.
#*
#* Use of Freescale code is governed by terms and conditions
#* stated in the accompanying licensing statement.
#* Description: serial helper function.
#*
#* Revision History:
#* -----------------
#* Code Version    YYYY-MM-DD    Author        Description
#* 0.1             2013-07-15    Larry Shen    Create this file
#*******************************************************************

import os, sys
file_path = os.path.dirname(os.path.abspath(__file__))
main_path = os.path.join(file_path, '..')
lib_path = main_path + '/lib/'
log_path = main_path + '/log/'
temp_path = main_path + '/temp/'
sys.path.append(main_path)
sys.path.append(lib_path)

import serial
import string
import logging

class SerialHelper:
    def __init__(self,app,platform):
        self.ser = None
        if platform == 'frdmkl03z48m':
            self.baud = 9600
        else:
            self.baud = 115200

    def open(self, port):
        logging.info('-- open serial port COM%s --' % port)
        serial_port = string.atoi(port) - 1
        self.ser = serial.Serial(port=serial_port, baudrate=self.baud, timeout=90)

    def close(self):
        logging.info('-- close serial port --')
        if self.ser:
            if self.ser.isOpen():
                self.ser.close()

    def getAll(self):
        n = self.ser.inWaiting()
        serContent = self.ser.read(n)
        return serContent

    def write(self, str):
        logging.info('-- write string to serial --')
        logging.info('%s' % str)
        logging.info('-- end write --')
        self.ser.write(str)
