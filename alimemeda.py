 # -*- coding:utf-8 -*-

import os
import json
from subprocess import Popen,PIPE
import cv2
api_key="sYVKydxGakOqX0tL-pw99CFI4WB1523s"
api_secret="gCdp_hIlgdbnUhcvCv61znzOF53-32hA"
path='./data/log'
def detect(image_file,return_landmark=0):
    result=Popen('curl -X POST "https://api-cn.faceplusplus.com/facepp/v3/detect" -F \
        "api_key={api_key}" -F \
        "api_secret={api_secret}" -F \
        "image_file=@{image_file}" -F \
        "return_landmark={return_landmark}"'
        .format(api_key=api_key,api_secret=api_secret,image_file=image_file,
          return_landmark=return_landmark),shell=True,stdout=PIPE)
    wait=""
    result=(result.stdout.read())
    with open("{path}/detect.json".format(path=path),"w+") as f:
        f.write(result)
    with open("{path}/detect.json".format(path=path)) as f:
        result=json.load(f)
    os.remove('{path}/detect.json'.format(path=path))
    return result

def compareTtoT(face_token_1,face_token_2):
    result=Popen('curl -X POST "https://api-cn.faceplusplus.com/facepp/v3/compare" -F \
        "api_key={api_key}" -F \
        "api_secret={api_secret}" -F \
        "face_token1={face_token_1}" -F \
        "face_token2={face_token_2}"'
        .format(api_key=api_key,api_secret=api_secret,face_token_1=face_token_1,
          face_token_2=face_token_2),shell=True,stdout=PIPE)  
    wait="" 
    result=(result.stdout.read())
    with open("{path}/compare.json".format(path=path),"w+") as f:   
        f.write(result)
    with open("{path}/compare.json".format(path=path)) as f:
        result=json.load(f)
    os.remove('{path}/compare.json'.format(path=path))
    return result 

def get_img(dir,topdown=True):
  global name
  fileList = [] 
  for root, dirs, files in os.walk(dir, topdown):
    for PicName in files:
      fileList.append(os.path.join(root,PicName)) 
    for f in sorted(fileList):
      imagedir=f
      return imagedir
if __name__ == '__main__':
  imagedir=get_img("./img")
  confidence=[]
  A_locals=[]
  result_detect=detect(image_file=imagedir,return_landmark=0)
  img = cv2.imread(imagedir)
  ft=cv2.freetype.createFreeType2()
  ft.loadFontData(fontFileName='./data/font/simhei.ttf',id =0)

  for i in range(0,len(result_detect["faces"])):
    A_locals.append(result_detect["faces"][i]["face_rectangle"]["top"])
  index1=A_locals.index(min(A_locals))
  A_face=result_detect["faces"][index1]["face_token"]


  A_face_rectangle=result_detect["faces"][index1]["face_rectangle"]
  x=A_face_rectangle["left"]
  y=A_face_rectangle["top"]
  w=A_face_rectangle["width"]
  h=A_face_rectangle["height"]
  img =cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,245),4)
  ft.putText(img=img,text="支付宝", org=(x, y - 10), fontHeight=60,line_type=cv2.LINE_AA, 
    color=(205,0,0), thickness=2, bottomLeftOrigin=True)
  cv2.imwrite(imagedir,img)

  result_detect["faces"].remove(result_detect["faces"][index1])


  for i in range(1,len(result_detect["faces"])):
    other_face=result_detect["faces"][i]["face_token"]
    result_compare=compareTtoT(face_token_1=A_face,face_token_2=other_face)
    confidence.append(result_compare["confidence"])
  index=confidence.index(max(confidence))  
  B_face_rectangle=result_detect["faces"][index]["face_rectangle"]
  x= B_face_rectangle["left"]
  y= B_face_rectangle["top"]
  w= B_face_rectangle["width"]
  h= B_face_rectangle["height"]
  img =cv2.rectangle(img,(x,y),(x+w,y+h),(0,245,255),4)
  ft.putText(img=img,text="支付婊", org=(x, y - 10), fontHeight=60,line_type=cv2.LINE_AA, 
    color=(205,0,0), thickness=2, bottomLeftOrigin=True)
  cv2.imwrite(imagedir,img)


  # 
  # print result

