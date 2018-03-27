#coding=utf-8
import os
import pylab as plb
import PIL.Image 
from tkinter import *
import tkFileDialog
from tkinter.filedialog import askdirectory
import tkinter.messagebox




def writeToTxt(list_name):
    try:
        fp = open('list.txt',"w+")
        for item in list_name:
            fp.write(str(item)+"\n") #list中一项占一行
        fp.close()
    except IOError:
        print("fail to open file")


def getAllImages(path):
    #f.endswith（）  限制文件类型
    #f.endswith('.jpg')|f.endswith('.png')  读取jpg/png格式的文件
    #注意 返回的是绝对路径
   return [os.path.join(path,f) for f in os.listdir(path) if f.endswith('.jpg')|f.endswith('.png')]
#将当前路径下的所有图片path存放进数组

def selectPath():
    path_ = askdirectory()    
    path.set(path_)
    
    
def var_states():
   print("png: %d,\njpg: %d" % (path.get(), var2.get()))
#   print("path1: %d,\npath2: %d" % (path1.get(), path2.get()))

def cut_all():
    sel_path = path.get()
    while len(sel_path) == 0:
        tkinter.messagebox.showwarning(None,"请选择待处理图片所在文件夹！")
        break
    else:
        cur_path = sel_path #获取当前路径
        #print (cur_path)
        filelist = [i for i in getAllImages(cur_path)]  
        # print (filelist[0])
        writeToTxt(filelist)
        #打开第一张图片 
        pic =  PIL.Image.open(filelist[0])  
        plb.imshow(pic)        
        #设置裁剪点（2个）
        cood = plb.ginput(2)
        #取点确定裁切坐标
        left = cood[0][0] 
        top =  cood[0][1]
        right = cood[1][0]
        bottom = cood[1][1]
        box = [int(left),int(top),int(right),int(bottom)]
        plb.close()
        for pic in filelist:
            img = PIL.Image.open(pic)
            #裁剪
            img2 = img.crop(box)
            #储存为原来路径覆盖原文件
            img2.save(pic)

            # new_image = img.resize((width,height),Image.BILINEAR)
            # new_image.save(os.path.join(path_save,os.path.basename(img_file)))
            
            
root = Tk()


# Label(root, text="图片类型:").grid(row=0, column = 0, sticky=W)
# var1 = IntVar()
# Checkbutton(root, text="png", variable=var1).grid(row=0, column = 1, sticky=W)
# var2 = IntVar()
# Checkbutton(root, text="jpg", variable=var2).grid(row=0, column = 2, sticky=W)

path = StringVar()
Label(root,text = "图片路径:").grid(row = 0, column = 0)
Entry(root, textvariable = path).grid(row = 0, column = 1)
Button(root, text = "Browser", command = selectPath).grid(row = 0, column = 2)


Button(root, text='开始裁剪', command=cut_all).grid(row=1, column = 1, sticky = E)
root.title("批量裁剪")
# tmp = open("tmp.ico","wb+")
# tmp.write(base64.b64decode(img))
# tmp.close()
# root.iconbitmap("tmp.ico")
# os.remove("tmp.ico")
root.mainloop()
