#!/bin/python3

#批量改檔名
#作者：scbmark
#日期：2021/9/13
#版本：7.0(python)

import os
import sys
from tkinter import Tk
from tkinter import filedialog as fd
from pathlib import Path

path = Path.cwd()

root = Tk()
root.withdraw()
files = fd.askopenfilenames(
    title = '選擇檔案...',
    initialdir = Path.cwd(),
    filetypes=
    [("All file","*.*"),
    ("video mode","*.jpg"),("video mode","*.jpeg"),("video mode","*.JPG"),("video mode","*.mp4"),("video mode","*.MP4"),
    ("jpg file","*.jpg"),("jpg file","*.jpeg"),("jpg file","*.JPG"),
    ("png file","*.png"),("png file","*.PNG"),
    ("mp4 file","*.mp4"),("mp4 file","*.MP4"),
    ("txt file","*.txt"),("txt file","*.TXT"),]
    )

#印出操作檔名
files = list(files)
if files == []:
    print('無選中檔案')
    sys.exit(0)
else:
    for file in files:
        print(Path(file).name)


## 改名模式選擇
rename_type = int(input('輸入改名模式\n1.首字大寫   2.大小寫互換\n3.全轉大寫    4.全轉小寫\n5.插入字串  6.刪除字串\n7.字串替換  8.副檔名更改\n9.產生序列\n10.時間戳記   \n\n選擇模式：'))

#####

##首字大寫
if rename_type == 1:
    for file in files:
        oldName = Path(file).name
        newName = Path(file).name.capitalize()
        print(f'{oldName} → {newName}')
    
    conduct = int(input('是否執行命名\n(y=1/n=2)'))
    
    if conduct == 1:
        for file in files:
            oldName = Path(file).name
            newName = Path(file).name.capitalize()
            os.rename(oldName,newName)
        print('命名完畢')
    else:
        print('命名取消')
        sys.exit(0)
##大小寫轉換
elif rename_type == 2:
    issub = int(input('是否包括副檔名\n(y=1/n=2)'))
    if issub == 2:
        for file in files:
            oldName = Path(file).name
            newName = Path(file).stem.swapcase() + Path(file).suffix
            print(f'{oldName} → {newName}')
        
        conduct = int(input('是否執行命名\n(y=1/n=2)'))

        if conduct == 1:
            for file in files:
                oldName = Path(file).name
                newName = Path(file).stem.swapcase() + Path(file).suffix
                os.rename(oldName,newName)
            print('命名完畢')
        else:
            print('命名取消')
            sys.exit(0)
    elif issub == 1:
        for file in files:
            oldName = Path(file).name
            newName = Path(file).name.swapcase()
            print(f'{oldName} → {newName}')

        conduct = int(input('是否執行命名\n(y=1/n=2)'))

        if conduct == 1:
            for file in files:
                oldName = Path(file).name
                newName = Path(file).name.swapcase()
                os.rename(oldName,newName)
            print('命名完畢')
        else:
            print('命名取消')
            sys.exit(0)
    else:
        print('輸入錯誤')
        sys.exit(0)
##全轉大寫
elif rename_type == 3:
    issub = int(input('是否包括副檔名\n(y=1/n=2)'))
    if issub == 2:
        for file in files:
            oldName = Path(file).name
            newName = Path(file).stem.upper() + Path(file).suffix
            print(f'{oldName} → {newName}')

        conduct = int(input('是否執行命名\n(y=1/n=2)'))

        if conduct == 1:
            for file in files:
                oldName = Path(file).name
                newName = Path(file).stem.upper() + Path(file).suffix
                os.rename(oldName,newName)
            print('命名完畢')
        else:
            print('命名取消')
            sys.exit(0)
    elif issub == 1:
        for file in files:
            oldName = Path(file).name
            newName = Path(file).name.upper()
            print(f'{oldName} → {newName}')
        
        conduct = int(input('是否執行命名\n(y=1/n=2)'))

        if conduct == 1:
            for file in files:
                oldName = Path(file).name
                newName = Path(file).name.upper()
                os.rename(oldName,newName)
            print('命名完畢')
        else:
            print('命名取消')
            sys.exit(0)

    else:
            print('輸入錯誤')
            sys.exit(0)
##全轉小寫
elif rename_type == 4:
    issub = int(input('是否包括副檔名\n(y=1/n=2)'))
    if issub == 2:
        for file in files:
            oldName = Path(file).name
            newName = Path(file).stem.lower() + Path(file).suffix
            print(f'{oldName} → {newName}')

        conduct = int(input('是否執行命名\n(y=1/n=2)'))

        if conduct == 1:
            for file in files:
                oldName = Path(file).name
                newName = Path(file).stem.lower() + Path(file).suffix
                os.rename(oldName,newName)
            print('命名完畢')
        else:
            print('命名取消')
            sys.exit(0)
    elif issub == 1:
        for file in files:
            oldName = Path(file).name
            newName = Path(file).name.lower()
            print(f'{oldName} → {newName}')
        
        conduct = int(input('是否執行命名\n(y=1/n=2)'))

        if conduct == 1:
            for file in files:
                oldName = Path(file).name
                newName = Path(file).name.lower()
                os.rename(oldName,newName)
            print('命名完畢')
        else:
            print('命名取消')
            sys.exit(0)

    else:
        print('輸入錯誤')
        sys.exit(0)
##插入字串
elif rename_type == 5:
    addtion = input('輸入要插入的字串\n字串：')
    location = int(input('輸入要插入的位置\n0是第一個位置，-1是最後一個位置\n位置：'))
    if location == 0:
        for file in files:
            oldName = Path(file).name
            newName = addtion + Path(file).name
            print(f'{oldName} → {newName}')
        
        conduct = int(input('是否執行命名\n(y=1/n=2)'))
    
        if conduct == 1:
            for file in files:
                oldName = Path(file).name
                newName = addtion + Path(file).name
                os.rename(oldName,newName)
            print('命名完畢')
        else:
            print('命名取消')
            sys.exit(0)
    else:
        for file in files:
            oldName = Path(file).name
            newName = Path(file).name[0:location] + addtion + Path(file).name[location:]
            print(f'{oldName} → {newName}')
        
        conduct = int(input('是否執行命名\n(y=1/n=2)'))
    
        if conduct == 1:
            for file in files:
                oldName = Path(file).name
                newName = Path(file).name[0:location] + addtion + Path(file).name[location:]
                os.rename(oldName,newName)
            print('命名完畢')
        else:
            print('命名取消')
            sys.exit(0)
##刪除字串
elif rename_type == 6:
    location_head = int(input('輸入要刪除的位置 頭\n0是第一個位置，-1是最後一個位置\n位置：'))
    location_end = int(input('輸入要刪除的位置 尾\n0是第一個位置，-1是最後一個位置\n位置：'))+1
    for file in files:
        oldName = Path(file).name
        newName = Path(file).name[0:location_head] + Path(file).name[location_end:]
        print(f'{oldName} → {newName}')

    conduct = int(input('是否執行命名\n(y=1/n=2)'))
    
    if conduct == 1:
        for file in files:
            oldName = Path(file).name
            newName = Path(file).name[0:location_head] + Path(file).name[location_end:]
            os.rename(oldName,newName)
        print('命名完畢')
    else:
        print('命名取消')
        sys.exit(0)
##字串替換
elif rename_type == 7:
    oldstr = (input('輸入要換掉的字串\n字串：'))
    newstr = (input('輸入要換上的字串\n字串：'))
    for file in files:
        oldName = Path(file).name
        newName = Path(file).name.replace(oldstr,newstr)
        print(f'{oldName} → {newName}')
    
    conduct = int(input('是否執行命名\n(y=1/n=2)'))
    
    if conduct == 1:
        for file in files:
            oldName = Path(file).name
            newName = Path(file).name.replace(oldstr,newstr)
            os.rename(oldName,newName)
        print('命名完畢')
    else:
        print('命名取消')
        sys.exit(0)
#副檔名更改
elif rename_type == 8:
    newsub = input('輸入新的副檔名\n副檔名：')
    for file in files:
        oldName = Path(file).name
        newName = Path(file).stem + newsub
        print(f'{oldName} → {newName}')
    
    conduct = int(input('是否執行命名\n(y=1/n=2)'))
    
    if conduct == 1:
        for file in files:
            oldName = Path(file).name
            newName = Path(file).stem + newsub
            os.rename(oldName,newName)
        print('命名完畢')
    else:
        print('命名取消')
        sys.exit(0)
#產生序列
elif rename_type == 9:
    numtype = int(input('名稱全換=1/加上=2\n模式：'))
    orders = int(input('輸入序列起始值\n起始值：'))
    if numtype == 1:
        orders2 = orders
        for file in files:
            oldName = Path(file).name
            newName = str(orders2) + Path(file).suffix
            print(f'{oldName} → {newName}')
            orders2 += 1
        
        conduct = int(input('是否執行命名\n(y=1/n=2)'))
        
        if conduct == 1:
            orders3 = orders
            for file in files:
                oldName = Path(file).name
                newName = str(orders3) + Path(file).suffix
                os.rename(oldName,newName)
                orders3 += 1
            print('命名完畢')
        else:
            print('命名取消')
            sys.exit(0)
    
    elif numtype == 2:
        location = int(input('輸入要插入的位置\n0是第一個位置，-1是最後一個位置\n位置：'))
        if location == 0:
            orders2 = orders
            for file in files:
                oldName = Path(file).name
                newName = str(orders2) + Path(file).name
                print(f'{oldName} → {newName}')
                orders2 += 1
                
            conduct = int(input('是否執行命名\n(y=1/n=2)'))
            
            if conduct == 1:
                orders3 = orders
                for file in files:
                    oldName = Path(file).name
                    newName = str(orders3) + Path(file).name
                    os.rename(oldName,newName)
                    orders3 += 1
                print('命名完畢')
            else:
                print('命名取消')
                sys.exit(0)
        else:
            orders2 = orders
            for file in files:
                oldName = Path(file).name
                newName = Path(file).name[0:location] + str(orders2) + Path(file).name[location:]
                print(f'{oldName} → {newName}')
                orders2 += 1
            
            conduct = int(input('是否執行命名\n(y=1/n=2)'))
        
            if conduct == 1:
                orders3 = orders
                for file in files:
                    oldName = Path(file).name
                    newName = Path(file).name[0:location] + str(orders3) + Path(file).name[location:]
                    os.rename(oldName,newName)
                    orders3 += 1
                print('命名完畢')
            else:
                print('命名取消')
                sys.exit(0)
    
    else:
        print('輸入錯誤')
        sys.exit(0)
#時間戳記
elif rename_type == 10:
    import time
    location = int(input('輸入要插入的位置\n0是第一個位置，-1是最後一個位置\n位置：'))
    timestr = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    if location == 0:
        for file in files:
            oldName = Path(file).name
            newName = timestr + Path(file).name
            print(f'{oldName} → {newName}')
    
        conduct = int(input('是否執行命名\n(y=1/n=2)'))
    
        if conduct == 1:
            for file in files:
                oldName = Path(file).name
                newName = timestr + Path(file).name
                os.rename(oldName,newName)
            print('命名完畢')
        else:
            print('命名取消')
            sys.exit(0)
    
    else:
        for file in files:
            oldName = Path(file).name
            newName = Path(file).name[0:location] + timestr + Path(file).name[location:]
            print(f'{oldName} → {newName}')
        
        conduct = int(input('是否執行命名\n(y=1/n=2)'))
    
        if conduct == 1:
            for file in files:
                oldName = Path(file).name
                newName = Path(file).name[0:location] + timestr + Path(file).name[location:]
                os.rename(oldName,newName)
            print('命名完畢')
        else:
            print('命名取消')
            sys.exit(0)
##輸入錯誤
else:
    print('輸入錯誤')
    sys.exit(0)

######