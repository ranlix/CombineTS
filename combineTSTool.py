# -*- coding: utf-8 -*-

import os
import sys


target_dir = sys.argv[1]
save_dir = os.path.abspath(target_dir)
savedTS = save_dir + "/all.ts"  # 拼接完成后新文件的路径


class TsParser(object):
    def __init__(self, tsdir):
        self.tsdir = tsdir
        self.tslist = []

    def tsfliter(self):
        original_files = os.listdir(self.tsdir)
        for i in original_files:
            if i.endswith(".ts"):
                self.tslist.append(i)
            else:
                pass

    def ts_file_parser(self):
        """Analysize the ts files in target directory,
        if they are unabridged, will not do the conbine operation."""
        tsnum = len(self.tslist)
        # first_item = int((self.tslist[0].split('.'))[0].split('-')[-1])
        # last_item = int((self.tslist[-1].split('.'))[0].split('-')[-1])
        num_list = [int((x.split('.'))[0].split('-')[-1]) for x in self.tslist]
        if tsnum == max(num_list) + 1 - min(num_list):  # 判断ts文件编号是否连续
            print "文件完整，可以接着完成拼接！"
            return True
        else:
            print "矮油! 貌似文件不完整呢！"
            return False

    def combiner(self):
        """Combine all the ts files in current directory into a new ts file"""
        if self.ts_file_parser():
            os.popen("touch " + savedTS)
            for each_ts in self.tslist:
                each_ts_path = os.path.join(save_dir, each_ts)
                command = "cat " + each_ts_path + ">> " + savedTS  # 开始拼接
                try:
                    os.popen(command)
                except Exception as e:
                    print e
                    break
        else:
            print "拼接未完成."


def run():
    try:
        os.popen("rm " + savedTS)  # 如果当前目录有all.ts 删除之
    except Exception as e:
        print e
    myTS = TsParser(target_dir)
    myTS.tsfliter()
    myTS.combiner()

if __name__ == '__main__':
    run()
