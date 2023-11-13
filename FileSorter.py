def filesorter():
    while True:

        import os
        import shutil
        path="/Users/akshatgoud/Downloads/"
        l=os.listdir(path)

        destination_for_img="/Users/akshatgoud/Desktop/test/lk"
        destination_for_dmg="/Users/akshatgoud/Desktop/dmg files"

        jpg=["jpg"]
        gif=["gif"]
        png=['png']
        dmg=["dmg"]

        for i in l:
            kind=i.split('.')[1:3]
            filepath=path+i

            if kind==dmg:
                shutil.move(filepath,destination_for_dmg)
            elif kind== jpg or gif or png:
                shutil.move(filepath,destination_for_img)

    !=