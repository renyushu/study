import json
from poco.drivers.android.uiautomation import AndroidUiautomationPoco


poco = AndroidUiautomationPoco()
ui = poco.agent.hierarchy.dump()
print(json.dumps(ui, indent=4))