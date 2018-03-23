#coding=utf-8
import os
import pylab as plb
import PIL.Image as Image

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
 

if __name__ == "__main__":
    cur_path = os.getcwd() #获取当前路径
    filelist = [i for i in getAllImages(cur_path)]  
    writeToTxt(filelist)
    #打开第一张图片 
    pic =  Image.open(filelist[0])  
    plb.imshow(pic)        
    # 设置裁剪点（2个）
    cood = plb.ginput(2)
    # 取点确定裁切坐标
    left = cood[0][0] 
    top =  cood[0][1]
    right = cood[1][0]
    bottom = cood[1][1]
    box = [int(left),int(top),int(right),int(bottom)]
    plb.close()
    for pic in filelist:
        img = Image.open(pic)
        #裁剪
        img2 = img.crop(box)
        #储存为原来路径覆盖原文件
        img2.save(pic)
# plb.show()