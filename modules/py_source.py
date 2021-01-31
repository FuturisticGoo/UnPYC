# -*- coding: utf-8 -*-
"""
Created on Tue Dec 22 03:06:32 2020

@author: FuturisticGoo
"""
import subprocess
import platform


def get_py():
    if(platform.system() == "Windows"):
        find_cmd = "where"
    else:
        find_cmd = "which"

    all_sources = {}

    for version in ("",
                    2, 2.6, 2.7,
                    3, 3.1, 3.2, 3.3, 3.4, 3.5, 3.6, 3.7, 3.8, 3.9, 3.10):
        try:
            temp_version = "python" + str(version)
            process = subprocess.Popen([temp_version, "-c",
                                       "import platform;print(platform.python_version())"],
                                       shell=True,
                                       stdout=subprocess.PIPE,
                                       stderr=subprocess.PIPE)
            process.wait()
            python_version, err = process.communicate()
            python_version = python_version.decode("UTF-8").strip()
            process = subprocess.Popen([find_cmd, f"python{version}"],
                                       stdout=subprocess.PIPE)
            python_path = process.communicate()[0].decode("UTF-8").strip()
            if(python_version == ""):
                continue
            all_sources[python_version] = python_path
        except:
            pass
    return all_sources


if __name__ == "__main__":
    print(get_py())