# -*- encoding=utf8 -*-
__author__ = "yushufeng"

from airtest.core.api import *
import time

auto_setup(__file__)

from poco.drivers.android.uiautomation import AndroidUiautomationPoco
poco = AndroidUiautomationPoco(use_airtest_input=True, screenshot_each_action=False)

poco("android.widget.LinearLayout").offspring("com.movies.hydq:id/bottomTab").child("android.widget.LinearLayout").child("androidx.appcompat.app.ActionBar$Tab")[0].offspring("com.movies.hydq:id/tab_content_image").click()
poco("android.widget.LinearLayout").offspring("com.movies.hydq:id/bottomTab").child("android.widget.LinearLayout").child("androidx.appcompat.app.ActionBar$Tab")[3].child("com.movies.hydq:id/tab").click()
poco(text="设置").click()

poco(npoco(zOrders="{'global': 0, 'local': 6}").click()
