from posix import listdir
import cv2
import os
import numpy as np

def batch_showname(path):
    __doc__ = "顯示指定路徑下，該層的檔案及資料夾名稱"
    flist = []
    for f in os.listdir(path):
        # if f.endswith("map.png"):
        # if f.endswith("pstm.jpg"):
        if f.endswith(".docx"):
            flist.append(f)
    return flist

# def bathcRename(path, prefix):
#     __doc__ = "批次改檔名"
#     for fname in os.listdir(path):
#     new_fname = prefix+fname
#     os.rename(os.path.join(path, fname), os.path.join(path, new_fname))

def cpcCropProfile(path, imgName):
    __doc__ = "中油剖面削白邊"
    # 讀取圖檔
    img = cv2.imread(path + "/" + imgName)
    img_gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)

    img_rev = cv2.bitwise_not(img_gray)
    # print(img_rev.shape) # high y, width x

    im_x = img_rev.sum(axis = 0)
    im_y = img_rev.sum(axis = 1)

    imx = np.where(im_x != 0)[0] # tuple(,)
    imy = np.where(im_y != 0)[0]

    imxL = imx.min(0)-1
    imxR = imx.max(0)+1
    imyU = imy.min(0)-1
    imyD = imy.max(0)+1

    # print(imxL)
    # print(imxR)
    # print(imyU)
    # print(imyD)

    # 裁切圖片
    crop_img = img[imyU:imyD, imxL:imxR] # notice: first is y, then is x

    # 顯示圖片
    # cv2.imshow("cropped", crop_img)
    # cv2.waitKey(0) # 按下任意鍵則關閉所有視窗
    # cv2.destroyAllWindows()

    # 寫入圖檔
    cv2.imwrite("./imgNewOut/new-" + imgName, crop_img)

def mapResize(path, imgName):
    __doc__ = "調整大小"
    # 讀取圖檔
    img = cv2.imread(path + "/" + imgName)

    #resize
    # scale_percent = 60       # percent of original size
    # width = int(img.shape[1] * scale_percent / 100)
    # height = int(img.shape[0] * scale_percent / 100)
    # dim = (width, height)    
    # img_resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
    
    # 寫入圖檔
    cv2.imwrite("./imgNewOut/new-" + imgName, img)

myPath = "./imgInput"
imgNamelist = batch_showname(myPath)
print(imgNamelist)

# # 裁切
# for imgName in imgNamelist:
#     cpcCropProfile(myPath, imgName)

# 調整大小
for imgName in imgNamelist:
    mapResize(myPath, imgName)

# 批次rename
for imgName in imgNamelist:
    mapResize(myPath, imgName)    