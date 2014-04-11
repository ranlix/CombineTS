# -*- coding: utf-8 -*-

import os
import sys


target_dir = sys.argv[1]
save_dir = os.path.abspath(target_dir)
savedTS = save_dir + "/all.ts"


class TsParser(object):
    def __init__(self, tsdir):
        self.tsdir = tsdir
        self.tslist = []

    def tsfliter(self):
        original_files = os.listdir(self.tsdir)
        for i in original_files:
            if i.endswith(".ts"):
                if i != "all.ts":
                    self.tslist.append(i)
                else:
                    os.popen
            else:
                pass

    def ts_file_parser(self):
        """Analysize the ts files in target directory,
        if they are unabridged, will not do the conbine operation."""
        tsnum = len(self.tslist)
        # print tsnum
        first_item = int((self.tslist[0].split('.'))[0].split('-')[-1])
        last_item = int((self.tslist[-1].split('.'))[0].split('-')[-1])
        if tsnum == last_item + 1 - first_item:
            print "文件完整，可以接着完成拼接！"
            return True
        else:
            print "矮油,貌似文件不完整呢！"
            return False

    def combiner(self):
        """Combine all the ts files in current directory into a new ts file"""
        if self.ts_file_parser():
            os.popen("touch " + savedTS)
            for each_ts in self.tslist:
                # print each_ts
                each_ts_path = os.path.join(save_dir, each_ts)
                # print each_ts_path

                command = "cat " + each_ts_path + ">> " + savedTS
                try:
                    os.popen(command)
                except Exception as e:
                    print e
                    break
            # print "Done!"
        else:
            print "拼接未完成."


def run():
    try:
        os.popen("rm " + savedTS)
    except Exception as e:
        print e
    myTS = TsParser(target_dir)
    myTS.tsfliter()
    myTS.combiner()

if __name__ == '__main__':
    run()
