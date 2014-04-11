# -*- coding: utf-8 -*-

import os.path
import sys
import re


target_dir = sys.argv[1]


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
        # print self.tslist

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
            print "文件不完整！"
            return False

    def combiner(self):
        """Combine all the ts files in current directory into a new ts file"""
        if self.ts_file_parser():
            os.popen("touch all.ts")
            for each_ts in self.tslist:
                print each_ts
                each_ts_path = os.path.join(os.path.abspath, each_ts)
                print each_ts_path
                command = "cat " + each_ts_path + ">> all.ts"
                try:
                    os.popen(command)
                except Exception as e:
                    print e
                    break
            # print "Done!"
        else:
            print "Sorry, the local ts files are abridged."


def run():
    myTS = TsParser(target_dir)
    myTS.tsfliter()
    if myTS.ts_file_parser():
        myTS.combiner()

if __name__ == '__main__':
    run()
