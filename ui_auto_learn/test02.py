# -*- encoding=utf8 -*-
__author__ = "yushufeng"

from airtest.core.api import *
from airtest.cli.parser import cli_setup

if not cli_setup():
    auto_setup(__file__, logdir=True, devices=[
            "Android:///",
    ])


# script content
print("start...")


# generate html report
# from airtest.report.report import simple_report
# simple_report(__file__, logpath=True)
swipe(Template(r"tpl1565787657655.png", record_pos=(0.323, 0.56), resolution=(1440, 2960)), vector=[-0.6017, 0.0057])
swipe(Template(r"tpl1565787694814.png", record_pos=(0.319, 0.594), resolution=(1440, 2960)), vector=[-0.6515, -0.0095])
touch(Template(r"tpl1565787712026.png", record_pos=(-0.197, 0.101), resolution=(1440, 2960)))
touch(Template(r"tpl1565787828480.png", record_pos=(0.195, 0.094), resolution=(1440, 2960)))
touch(Template(r"tpl1565787960938.png", record_pos=(0.26, -0.513), resolution=(1440, 2960)))
touch(Template(r"tpl1565788021899.png", record_pos=(0.008, 0.124), resolution=(1440, 2960)))




