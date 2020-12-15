"""
GLDAS

"""
import getpass
import requests
import datetime as dt
import download_gldas
import datetime as dt
import os
import subprocess
import glob


username = getpass.getuser()
if username == "satyukt":
    dir_vaari = "/media/satyukt/vaari/Projects/1000/gldas/"
    
    
dir_project = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
dir_raw = os.path.join(dir_vaari, "raw_data")
dir_nc = os.path.join(dir_vaari, "nc")
nc_tif_file = os.path.join(dir_project, 'src', 'convert_nc.R')


user="abhi2chikun"
password="123@Chikun"

cookies_str = "--load-cookies ~/.urs_cookies --save-cookies ~/.urs_cookies --auth-no-challenge=on --keep-session-cookies -np -r --content-disposition --user={user} --password={password} {url}"
#Enter the Start date
now = dt.datetime.now()
start_date = dt.datetime(2015, 1,1)
curr = start_date
curr_date=now

while start_date<=curr_date:
    year=start_date.year
    month=start_date.month
    day=start_date.day
    curr=dt.datetime(year,month,day)
    day_of_year = str((curr - dt.datetime(curr.year, 1, 1)).days + 1)
    day_of_year=day_of_year.zfill(3)
    yyyymmdd=str(year)+str(month)+str(day).zfill(2)
    check_files =f"{dir_nc}/sm/0_10cm/{yyyymmdd}.nc"
    if os.path.exists(check_files):
        print(f"File exist:{yyyymmdd}")
    else:
        download_gldas.download(year,day_of_year,dir_raw,user,password,cookies_str)
    
        subprocess.call('Rscript --vanilla %s %s %s %s %s' %(nc_tif_file, dir_raw, dir_nc, year,day_of_year), shell=True)

    start_date=start_date+dt.timedelta(days=1)
    
    