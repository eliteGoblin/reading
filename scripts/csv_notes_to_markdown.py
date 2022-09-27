#!/usr/bin/python
# -*- coding: utf-8 -*-

import re
import csv

note_regex = "标注 "

def is_highlight(text):
    res=re.findall(note_regex, text)
    if res:
        return True
    return False

def csv_notes_to_strings(file_path):
    """
    kindle csv每行4 column, comma 分割
    实际批注开始于'标注 '
    ['', '', '', '']
    ['批注类型', '位置', '已加星标？', '批注']
    ['标注 (黄)', '位置 21', '', '每天都感觉没有干劲？！这可不太妙
    """
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            if is_highlight(row[0].strip()):
                if row[3].strip() != "":
                    print(row[3].strip())


if __name__ == "__main__":
    print("Hello")
    csv_notes_to_strings("./poop_came_adrian_schulte.md.csv")