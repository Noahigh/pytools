import shutil
def zip(out,file,mode):
 todir=shutil.make_archive(out,mode,file)
def unzip(zipname,out):
  shutil.unpack_archive(zipname,out)
