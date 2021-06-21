from cx_Freeze import setup, Executable

setup(name='radioreport_import', version='1.0', executables=[Executable('rr_import.py', targetName='radioreport_import_v1.0.exe')])
