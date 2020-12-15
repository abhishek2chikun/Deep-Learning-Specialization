#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 16:45:17 2020

@author: dinesh
"""

import datetime as dt
import os
from subprocess import call

def get_file_name(year,day_of_year):
    x="_3H.2.1"
# =============================================================================
#     if int(day_of_year) < 183:
#         x="_3H.2.1"
#     else:
#         x="_3H_EP.2.1"  
# =============================================================================
    url =f"https://hydro1.sci.gsfc.nasa.gov/data/GLDAS/GLDAS_NOAH025{x}/{year}/{day_of_year}/"
    print(url)
    return url



def download(year,day_of_year,dir_raw,user,password,cookies_str):
    
    url_download = get_file_name(year, day_of_year)
    if os.path.exists(url_download):
        print("File exist")
        return
    else:
        url=url_download
       
        
       
        """cmd = "wget -L -nc --user=%s --password=%s %s %s -P %s"%(
                user, password, cookies_str, url_download, dir_raw)"""
        cmd=f"wget --load-cookies ~/.urs_cookies --save-cookies ~/.urs_cookies --auth-no-challenge=on --keep-session-cookies -np -r --content-disposition -P{dir_raw} --user={user} --password={password} {url}"
        call(cmd, shell=True)
        
#https://hydro1.sci.gsfc.nasa.gov/data/GLDAS/GLDAS_NOAH025_3H.2.1/
#https://hydro1.sci.gsfc.nasa.gov/data/GLDAS/GLDAS_NOAH025_3H_EP.2.1/2020/284/