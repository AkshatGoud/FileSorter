import os 
import shutil

def file_type(files):
    reversedfilename=files[::-1]
    kind=reversedfilename.split('.')[0:1]
    stringedkind=''.join((kind))
    filetype=stringedkind[::-1]
    return filetype

def redundancy (files):
    if os.path.isfile(files):
        newfile=files
        while files==newfile:
            for i in range(9):
                x=str(i)
                newfile=files+x
                return newfile
    else:
        pass



while True:

    downloads_path="/Users/akshatgoud/Desktop/Images/"
    source_path="/Users/akshatgoud/Desktop/test/"
    os.chdir(downloads_path)


    for root, dirs, filenames in os.walk(downloads_path):

        for files in filenames:
            foldername= file_type(files)
            files = redundancy(files)
            filepath=downloads_path+files
            destination=source_path+foldername


            if foldername=="DS_Store":
                pass

            elif os.path.isdir(destination):
                shutil.copy(filepath,destination)
                os.remove(filepath)
                
            else :
                os.mkdir(destination)
                shutil.copy(filepath,destination)    
                os.remove(filepath)
"""
except :
    print("Error found contact the creator of the code")"""