from zipfile import ZipFile

current = 0
total = 0

with ZipFile(r"C:\Users\FuturisticGoo\Downloads\Python all\Zips\python_3.8_wu6.zip") as zf:
    for i in zf.filelist:
        total += i.file_size
    
    for member in zf.namelist():
        try:
            if(current != 0):
                back = "\b \b"*3
            else:
                back = ""
            current += (zf.getinfo(member).file_size)

            print(back+str(int((current/total)*100))+r"%", flush=True, end="")
            zf.extract(
                member, r"C:\Users\FuturisticGoo\Documents\Python\Unpyc\py")
        except Exception as err:
            print(err)

print("\n"+str(round((total/(1024*1024)), 2))+" mb")
