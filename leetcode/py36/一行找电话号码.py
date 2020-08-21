import re

allstr = "quyuan-100000-33333,dqx-12344-23333333,zl-23454-999999"

print([i[0] for i in re.findall("-(\d+)(,|$)", allstr)])
