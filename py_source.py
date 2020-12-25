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

    try:
        process = subprocess.Popen(["python3", "--version"],
                                   stdout=subprocess.PIPE)
        python3_version = process.communicate()[0].strip().decode("utf-8")[7:]
        process = subprocess.Popen([find_cmd, "python3"],
                                   stdout=subprocess.PIPE)
        python3_path = process.communicate()[0].strip().decode("utf-8")
        all_sources[python3_version] = python3_path

    except FileNotFoundError:
        pass

    try:
        process = subprocess.Popen('python2 -c "import platform;\
                                   print platform.python_version()"',
                                   shell=True,
                                   stderr=subprocess.PIPE,
                                   stdout=subprocess.PIPE)
        python2_version, err = process.communicate()
        if(err):
            raise FileNotFoundError
        python2_version = python2_version.decode("utf-8").strip()
        process = subprocess.Popen([find_cmd, "python2"],
                                   stdout=subprocess.PIPE)
        python2_path = process.communicate()[0].strip().decode("utf-8")
        all_sources[python2_version] = python2_path
    except FileNotFoundError:
        pass

    try:
        process = subprocess.Popen('python -c "import platform;\
                                   print platform.python_version()"',
                                   shell=True,
                                   stdout=subprocess.PIPE,
                                   stderr=subprocess.PIPE)
        python_version, err = process.communicate()
        if(err):
            raise FileNotFoundError
        else:
            python_version.strip().decode("utf-8")
            process = subprocess.Popen([find_cmd, "python"],
                                       stdout=subprocess.PIPE)
            python_path = process.communicate()[0].strip().decode("utf-8")
            all_sources[python_version] = python_path
    except FileNotFoundError:
        pass

    try:
        process = subprocess.Popen('python -c "import platform;\
                                   print(platform.python_version())"',
                                   shell=True,
                                   stdout=subprocess.PIPE)

        python_version = process.communicate()[0].strip().decode("utf-8")
        process = subprocess.Popen([find_cmd, "python"],
                                   stdout=subprocess.PIPE)
        python_path = process.communicate()[0].strip().decode("utf-8")
        all_sources[python_version] = python_path
    except FileNotFoundError:
        pass

    return all_sources


if __name__ == "__main__":
    print(get_py())
