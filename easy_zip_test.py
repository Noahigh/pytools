import zipfile
def zip(file,mode,**args):
 #unix适配
 try:
  if args['unix']==True:
   zipmode=zipfile.ZIP_STORED
  else:
   zipmode=zipfile.ZIP_DEFLATED
 except KeyError:
  zipmode=zipfile.ZIP_DEFLATED
 #创建对象
 zp=zipfile.zipfile(file,mode,zipmode)
 #写zip
 if mode=='w':
  try:
   zp.write(args['file'])
  except KeyError:
   return 'use write mode and did\'t enter zipthings'
 #读zip
 if mode=='r':
  #获取文件列表
  zpl=zp.namelist()
  #设置输出目录
  try:
   outpath=args['out']
  except KeyError:
   return 'use read mode and not give ouput path'
  #解压
  for f in zpl:
   zp.extract(f,outpath)
 zp.close()