# -*- encoding=utf8 -*-
__author__ = "yushufeng"

from airtest.core.api import *
from airtest.core.api import connect_device
from airtest.cli.parser import cli_setup
from poco.drivers.android.uiautomation import AndroidUiautomationPoco


# if not cli_setup():
#     auto_setup(__file__, logdir=True, devices=[
#             "Android://127.0.0.1:5037/271cc935e1217ece",
#     ])

dev = connect_device('Android://127.0.0.1:5037/271cc935e1217ece')
poco = AndroidUiautomationPoco(dev)
# script content
print("start...")

start_app('com.movies.hydq')

# generate html report
# from airtest.report.report import simple_report
# simple_report(__file__, logpath=True)
poco(text="首页").click()
poco("android.widget.LinearLayout").offspring("com.movies.hydq:id/bottomTab").child("android.widget.LinearLayout").child("androidx.appcompat.app.ActionBar$Tab")[2].offspring("com.movies.hydq:id/tab_content_image").click()
poco(text="美食").click()
poco(text="吃播").click()
poco(text="爱豆").click()
poco(text="高颜值").click()
poco(text="高颜值").click()
