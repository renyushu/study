from airtest.core.api import *
from airtest.core.api import connect_device
from airtest.core.android.android import Android


dev = Android()
print(dev.list_app())

# for p in dev.list_app():
# #     print(p)

print(shell('ls'))