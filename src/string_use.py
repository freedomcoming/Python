"""
字符串操作
"""


text1 = '11/27/2012'
text2 = 'Nov 27, 2012'

import re
# Simple matching: \d+ means match one or more digits
datepat = re.compile(r'\d+/\d+/\d+')
if datepat.match(text1):
    print("匹配")
else:
    print("不匹配")

text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'
r = datepat.findall(text)
print(r)

# 文本替换
## replace
text = 'yeah, but no, but yeah, but no, but yeah'

print(text.replace('yeah', 'yep'))

# re.sub

text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'
import re
r = re.sub(r'(\d+)/(\d+)/(\d+)', r'\3-\1-\2', text)
print(r)


text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'
import re
r = re.sub(r'(?P<month>\d+)/(?P<day>\d+)/(?P<year>\d+)', r'\g<year>-\g<month>-\g<day>', text)
print(r)
