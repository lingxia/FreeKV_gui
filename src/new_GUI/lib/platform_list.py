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

platform_list = ['frdmk64f120m',
                 'twrk22f120m',
                 'twrk64f120m',
                 'twrk22f120m128r',
                 'twrk22f120m256r',
                 'twrkv31f120m',
                 'twrkv31f120m128r',
                 'frdmk22f120m',
                 'twrk24f120m',
                 'twrkv31f120m256r',
                 'frdmkl03z48m',
                 'twrkv30f100m',
                 'twrkl43z48m',
                 'frdmkl43z48m',
                 'frdmk22f120mk02',
                 'twrk22f120mk02',
                 'twrkv30f100mk02',
                 'twrkv31f120mkv30',
                 'twrkv30f100mk0264',
                 
    ]

target_list = ['Debug',
               'Release',
               'Flash_Debug',
               'Flash_Release',
               'Ram_Debug',
               'Ram_Release',
    ]

debugger_list = ['jlink',
				 'pne',
    ]

ide_list = ['iar',
            'uv4',
	]

test_suite = ['ksv',
	]