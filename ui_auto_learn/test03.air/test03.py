# -*- encoding=utf8 -*-
__author__ = "yushufeng"

from airtest.core.api import *

auto_setup(__file__)

start_app('com.movies.hydq')

from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)


touch(Template(r"tpl1565789090297.png", record_pos=(0.369, 0.846), resolution=(1440, 2960)))







