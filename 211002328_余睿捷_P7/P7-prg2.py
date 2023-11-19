#将同一文件夹下的所有文本文件（.txt文件）合并为一个，合并后的文件名为all.txt。
import glob
with open("all.txt", "wb") as outfile:
    for filename in glob.glob("*.txt"):
        with open(filename,"rb") as infile:
            outfile.write(infile.read())