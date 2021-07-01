#!/usr/bin/env python3

from os import listdir
from os.path import join
import csv

def export(dirname):
  dirpath = "weibo/"+dirname
  filename = listdir(dirpath)[0]
  fp = join(dirpath, filename)
  with open("txt/"+dirname+".txt","w") as out:
    with open(fp) as f:
      for line in csv.reader(f):
        line = line[2].strip()
        stop = False
        for skip in ("的微博视频","网页链接"):
          if line.endswith(skip):
            stop = True
        if line and not stop:
          out.write(line+"\n")


def main():
  for pos,i in enumerate(listdir('weibo'),1):
    if i!="users.csv":
      print(pos,i)
      export(i)

main()

