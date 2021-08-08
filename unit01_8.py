import os
import shutil

if os.path.exists('files'):
    shutil.rmtree('files')

os.mkdir('files')
os.chdir("files")
n = int(input())
for i in range(n):
    os.mkdir("f"+str(i+1))
print(sorted(os.listdir()))
a=input("any botton to continue: ")

os.rename("f1","folder1")
print(sorted(os.listdir()))
a=input("any botton to continue: ")

os.rmdir("folder1")
print(sorted(os.listdir()))

os.chdir("../")
shutil.rmtree('files')



