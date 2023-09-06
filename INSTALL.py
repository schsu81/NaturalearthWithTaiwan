#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 26 09:37:13 2023

@author: schsu
"""
import os, sys
#import cartopy as crt
#import cartopy.crs as ccrs
import shutil
from glob import glob
from cartopy import config
dir_NE10wTW = os.path.dirname(__file__)
dir_backup = f'ne_ori'
names = ['coastline','ocean','land']
#%%============================================================================
def _printhelp():
  print('INSTALL.py [opts] [command]')
  print('  command:')
  print('      install   - install Natural Earth 10m with Taiwan outline.')
  print('      uninstall - uninstall Natural Earth 10m with Taiwan outline.')
  print('  opts:')
  print('      -h - print this helps.')
  print('      --prefix - specific path to install or uninstall.')
  print('      --help   - print this helps.')
  exit()
#%%----------------------------------------------------------------------------
def _install(dir_data):
  if not os.path.isdir(dir_data):
    os.makedirs(dir_data)
  os.chdir(dir_data)  

  for name in names:
    fns = glob(f'ne_10m_{name}.*')
    if len(fns)>0:
      if not os.path.isdir(dir_backup):
        os.makedirs(dir_backup)
      for fn in fns:
        if os.path.isfile(os.path.join(dir_backup,fn)):
          os.remove(fn)
        else:
          shutil.move(fn,dir_backup)
  fns = glob(os.path.join(dir_NE10wTW,'ne_10m_*'))
  for fn in fns:
    shutil.copy2(fn,'.')
#%%----------------------------------------------------------------------------
def _uninstall(dir_data):
  if not os.path.isdir(dir_data):
    print("Can't found installed path.") 
    exit()
  os.chdir(dir_data)  

  for name in names:
    fns = glob(f'ne_10m_{name}.*')
    if len(fns)>0:
      for fn in fns:
        os.remove(fn)

  if os.path.isdir(dir_backup):
    fns = glob(os.path.join(dir_backup,'ne_10m_*'))
    for fn in fns:
      shutil.move(fn,'.')
    os.rmdir(dir_backup)
#%%----------------------------------------------------------------------------
if __name__ == '__main__':

  isInstall = True
  isPrefix  = False
  countArg  = 0
  if len(sys.argv)<=1:
    _printhelp()
  for arg in sys.argv[1:]:
    if arg[:2]=='--':
      varn,value = arg.split('=',1)
      match varn:
        case '--prefix':
          isPrefix = True
          prefix = value 
        case _:
          _printhelp()
    elif arg[1]=='-':
      _printhelp()
    else:
      countArg += 1
      match arg:
        case 'install':
          isInstall = True
          command   = arg
        case 'uninstall':
          isInstall = False
          command   = arg
        case _:
          _printhelp()

  if isPrefix:
    dir_data = prefix
  else:
    #if config['pre_existing_data_dir'] is not None and os.path.isdir(config['pre_existing_data_dir']):
    #  dir_data = config['pre_existing_data_dir']
    #else:
    dir_data = config['data_dir']
    dir_data = os.path.join(dir_data,'shapefiles','natural_earth','physical')
  
  print()
  print(f'NE10wTW path = {dir_NE10wTW}')
  print(f'{command} path = {dir_data}')
  print()
  input("Press Enter to continue...")
  if isInstall:
    _install(dir_data)
  else:
    _uninstall(dir_data)
  print('done')
#%%
