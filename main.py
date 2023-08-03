# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import json
import os
import time


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

path = 'D:\hhh'
'''
for dir in next(os.walk(path))[1]:
    print(dir)
    for root, dirs, file in os.walk(os.path.join(path, dir)):
        print(root)
        print(dirs)
        print(file)
        break
    break
'''


def check_json(file):
    if not file.endswith('.json'):
        return False

    with open(file, 'r+', encoding='utf-8') as f:
        try:
            json.loads(f.read())
            return True
        except:
            return False


for file in os.listdir(path):
    file_ = os.path.join(path, file)
    if check_json(file_):
        print(file_)
    # if os.path.isdir(file_):
    #     print(file_ + "  ddd")
    # if os.path.isfile(file_):
    #     print(file_ + "  fff")

with open(os.path.join("D:/", "hhh/", "wa.json"), 'rb') as f:
    data = json.loads(f.read())
    for small in data:
        print(small)
        print(data[small])

'''
"version = "
"for version"
    with open(os.path.join("ROOT", "lan", "version", "tag.json"), 'rb') as f:
        data = json.loads(f.read())
        for product in data:
            if product == "" and data["product"] == "":
                version = "version"

# python跳出双层for循环
for i in list:
    for j in list:
        print(i + j)
        break
    else:
        continue   # 如果走上面break，那么不会走这里的continue
    break

hh = "ZH/CMDB/3.10/AD/intro.md"
print(hh.split("/"))
print(hh.split("/")[0])  # ZH
print(hh.split("/")[1])  # CMDB
print(hh.split("/")[2])  # 3.10

print("1.0" == None)

i, j = hh.split("/")[1:3]  # CMDB 3.10

end_list = [[0, 1, 2, 3], ]
list = [1, 2, 3, 4, 5, 6]
end_list.append(list[-2:])  
print(end_list)  # [[0, 1, 2, 3], [5, 6]]

end_list = ["a", "b"]
list = [1, 2, 3]
from itertools import product
for re, io in product(end_list, list):
    print(re, io)
# a 1
# a 2
# a 3
# b 1
# b 2
# b 3


list0 = {
    "a": 1,
    "d": 2,
}
print(list0.keys())        # dict_keys(['a', 'd'])
print(list(list0.keys()))  # ['a', 'd']

from datetime import datetime
import time
from pytz import timezone
print(int(time.time()))

end_time = int(time.time())           # 时间戳取整（秒级）
start_time = end_time - 24 * 60 * 60  # 获取前一天的数据



from request_post import request_post
import time

buz_type = [20]
logtype_id = [5]
levelid = [5]
targets = ["sum_outtraffic"]
# 时间区间查询范围
end_time = int(time.time())  # 时间戳取整（秒级）
start_time = end_time - 24 * 60 * 60  # 获取前一天的数据
custom_config = {"interval": "1m"}
term_filter = {"AppName": "农牧场"}
range_filter = {"Gnow": {"start": start_time, "end": end_time}}


try:
    a = 1
    b = 0
    if a == b:
        print("hh")
    else:
        raise Exception
except:
    print(Exception)


import insight
from itertools import product

# TGW监控指标list
targets = list(insight.TGW_METRIC_LIST.keys())
# 取映射
# {tgw.TGW_name: tgw.bk_biz_id for tgw in BizTgwConfigModel.objects.filter(is_active=True)}

terms_filter = list(map.keys())

# 根据不同的TGW业务和TGW指标
for term, metric in product(terms_filter, targets):
    res = insight.get_tgw_monitor_info(term=term, target=metric)
    data = res["data"]
    data_list = data["sum_outtraffic"]["data_list"]

    date_list = []
    for item in data_list:
        date_list.append(item["date"])

    # date_list = []
    # date_list.append(item["date"] for item in data_list)
    # print(date_list)  # [<generator object <genexpr> at 0x000001F043307888>]
    print(date_list)  # ['2023-03-06 20:30', ... ]
    break

TGW_METRIC_LIST = {
    "sum_outtraffic": "出带宽",
    "sum_intraffic": "入带宽",
}
metric = "sum_outtraffic"
print(TGW_METRIC_LIST.get(metric, metric))
print(TGW_METRIC_LIST.get(metric))

# from insight import get_tgw_map
# model_data = get_tgw_map()
# print(model_data)
# data = model_data["data"]  # [{...},{...},{...}, ...]

busi_list = []
tgw_list = []
for item in object_:
    print(item)
    busi_list.append(item["busi_1st_name"])
    tgw_list.append(item["tgw_app_name"])

print(busi_list)
print(tgw_list)

import numpy as np
arr = np.zeros((5, 5))
for i in range(1, 5):
    for j in range(1, 5):
        arr[i][j] = 2 + int(arr[i][j])
        # print(arr[i][j])
print(arr)
print(arr[0][0])

print(data["data"]["data"])
print(data["data"]["data"][0]["bs1NameId"])

# 把元素为字典的列表，把列表中字典某key的value都取出来成一个列表
bs1Name_list = [item['bs1NameId'] for item in data["data"]["data"]]  # [54, 154]
print(bs1Name_list)

for item in data["data"]["data"]:
    if "bu" not in item.keys():
        print("我")
        print(item)
        continue
    if item["bu"] is "":
        print(item)


bu2_list = ["123", "", "23"]


def get(list):
    list_ = []
    for item in list:
        if item is not "":
            list_.append(item)
    return list_


q = []
q.append(3)
q.append(4)
print(q.pop())


def get(timestamp):
    print(timestamp and timestamp)
    if timestamp and timestamp // 10 ** 10 == 0:
        print(timestamp)
        timestamp *= 1000
    print(timestamp)


get(int(time.time()))
get(int(time.time()) * 1000)
print(1678844916 and 1678844916)
print(1678844916000 and 1678844916000)

print(1678844916000 // 10)
print(1678844916000 // 10 ** 10)  # 如果沒有到十位數，就会结果为0，到十位数就会去十位数之后的，比如这里的167


a = set()
a.add(1)
a.add(1)
a.add(12)
a.add(12)
a.add(32)
# print(a.pop())  # set的pop()方法：随机删除集合中的数据，并且将被删除的数据返回。
# print(a.pop())

while len(a) > 0:
    print(a.pop())

import time
now = int(time.time())
otherStyleTime = time.strftime("%Y-%m-%d %H:%M", time.localtime(now))

print(now)
print(otherStyleTime)


class DummyClient(tuple):

    def __getattr__(self, name):
        new = DummyClient(self + (name,))
        setattr(self, name, new)
        return new

    def __call__(self, *args, **kwargs):
        return {
            "result": False,
            "data": None,
            "message": ""
        }

get_client_by_user = lambda x: DummyClient()
client = get_client_by_user("admin")
resp = client.bk_cmdb.search_business()
print(resp)                        # {'result': False, 'data': None, 'message': ''}
print(resp["result"])              # False

# 第一次到client，会回调get_client_by_user = lambda x: DummyClient()
# client = () 因为继承的是tuple
# 然后到client.bk_cmdb.search_business()
# 会先调getattr去找bk_cmdb这个属性，找不到我们就会生成一个DummyClient(self + (name,))对象A给它，同时setattr把对象A作为默认值给这个属性
# 返回这个属性，对search_business也如此，最后()调call，把return的结果返回


import datetime

zen = float(datetime.datetime.now().strftime("%S"))
minute = datetime.datetime.now() - datetime.timedelta(seconds=zen + 1)
five_minutes_ago = minute - datetime.timedelta(minutes=2) + datetime.timedelta(seconds=1)
fifteen_minutes_ago = five_minutes_ago.strftime("%Y-%m-%d %H:%M:%S")

print(minute)
print(five_minutes_ago)
print(fifteen_minutes_ago)


for i in range(0, 179, 60):
    print(i)

s = "2023-03-22 16:27".rsplit(":", 1)[1]
print(s)  # 27

'''
from datetime import datetime, timedelta, date

today = datetime.today().date()
print(today)  # 2023-04-25
today = today - timedelta(days=1)
print(today)  # 2023-04-24
w = datetime.today().date()
ttoday = today - timedelta(days=31)

if "2023-04-24" == str(today) and ttoday < w:  # 日期类型比较是ok的
    print("hjhh")
else:
    print("jjj")  # 直接的"2023-04-24"==today会到这里来

print(w - today)  # 1 day, 0:00:00
print(w - ttoday)
print(str(w - today).split(' ')[0])
print(int(str(w - ttoday).split(' ')[0]))  # 获取时间差

date(*map(int, "2023-04-24".split('-')))  # 字符串转换为日期

if date(*map(int, str("2023-06-01").split('-'))) > date(*map(int, "2023-05-24".split('-'))) - timedelta(days=1):
    print("wadadadwadadwadasdascsfsfvsdf")

print(date(*map(int, "2023-05-24".split('-'))) - timedelta(days=-1))

for i in range(1):
    print(i)

import datetime
from datetime import timedelta

now = datetime.datetime.now().replace(hour=0, minute=0, second=0, microsecond=0)  # 把datetime对象的时分秒都装换为0
time = now
print(time)
last_week_start = now - timedelta(days=now.weekday() + 7)
last_week_end = now - timedelta(days=now.weekday() + 1)
print('--- last_week_start = {} last_week_end = {}'.format(last_week_start, last_week_start + timedelta(days=7)))

str = "菜鸟教程"
str_utf8 = str.encode("UTF-8")
str_gbk = str.encode("GBK")

print(str)
print("UTF-8 编码：", str_utf8)
print("GBK 编码：", str_gbk)
import base64

re = base64.b64decode(str.encode('utf8')).decode('utf8')

print(str.encode('utf8'))
print(base64.b64decode(str.encode('utf8')))
print(re)

aa = {"a": 1}
aa["b"] = 2

print("img1.png")

"""

python manage.py shell

连续天数
from django_redis import get_redis_connection
client = get_redis_connection()
continue_punch_key = "xuandonglai_continue_punch"
last_day = str(client.lindex(continue_punch_key, 0), encoding='utf-8')
days = client.llen(continue_punch_key)  # 连续天数

抽奖
from django_redis import get_redis_connection
from datetime import datetime
day = str(datetime.today().date())
key = f"PRIZE_SPORTS_TEAM_{day}"
con = get_redis_connection()
con.hgetall(key)

组队打卡
from django_redis import get_redis_connection
from datetime import datetime
team_id = "HH187597"
key = f"{team_id}_{datetime.now().date()}_punch_members"
con = get_redis_connection()
punch_user = con.smembers(key)
con.spop()

from django_redis import get_redis_connection
con = get_redis_connection()
con.get(lock_punch_v_daoqgong)


from django_redis import get_redis_connection
from home_application.utils import get_user_select_activity
con = get_redis_connection()
get_user_select_activity(con, 'katshao')


from django_redis import get_redis_connection
con = get_redis_connection()
from common import constants
con.get(constants.PunchTotalNumCache.PUNCH_TOTAL_NUM)


from django_redis import get_redis_connection
con = get_redis_connection()
from common import constants
count_punch_num_config = con.get(constants.PunchTotalNumCache.PUNCH_TOTAL_NUM)
count_punch_num_config

from django_redis import get_redis_connection
con = get_redis_connection()
from common import constants
con.delete(constants.PunchTotalNumCache.PUNCH_TOTAL_NUM)

from django_redis import get_redis_connection
con = get_redis_connection()
from common import constants
con.delete(constants.PersonalTypePunch.PERSONAL_PUNCH_NUM)
con.delete(constants.PersonalTypePunch.PERSONAL_PUNCH_DAYS_NUM)
con.delete("HH889456_members")

# 了连续打卡天数 {username}_continue_punch
from django_redis import get_redis_connection
con = get_redis_connection()
username = 'xx'
con.delete(f'{username}_continue_punch')

from django.core.cache import cache
from common import constants
count_punch_num_config = cache.get(constants.PunchTotalNumCache.PUNCH_TOTAL_NUM)
count_punch_num_config["count_punch_num"]
count_punch_num_config["count_personal_punch_num"]

from home_application.models import Punch, SubscribeNews, TeamMember, Person, SelectActivity, IegUsersImages
count_punch_num = TeamMember.objects.all().count()
count_personal_punch_num = Person.objects.all().count()

# 删除首页配置时间缓存
from django.core.cache import cache
from common import constants
from common.constants import ActivityType
cache.delete(constants.ActivityDateCache.PUNCH_DATE_RANGE_CONFIG)

# 删除永久缓存
from django_redis import get_redis_connection
con = get_redis_connection()
team_id = xxx
con.delete(f"{team_id}_members")

# 组队信息
from django_redis import get_redis_connection
con = get_redis_connection()
team_id = "HH603963"
from datetime import datetime
team_punch_members_key = f"{team_id}_{datetime.today().date()}_punch_members"
con.sadd(team_punch_members_key, request.user.username)

# 改为未确认状态，改数据库状态
team_id = 'HH501258'
key = f'{team_id}_members'
from django_redis import get_redis_connection
con = get_redis_connection()
con.srem(f"{team_id}_members")
# 查一下他们的队伍状态
from datetime import datetime
con.smembers(f"{team_id}_{datetime.now().date()}_punch_members")


from django_redis import get_redis_connection
con = get_redis_connection()
team_id = 'HH751206'
from datetime import datetime
team_punch_members_key = f"{team_id}_{datetime.now().date()}_punch_members"
con.smembers(team_punch_members_key)

con.smembers(f"{team_id}_members")

from home_application.models import TeamMember

from django_redis import get_redis_connection
con = get_redis_connection()
from common.constants import ActivityType, PRIZE_POOL_KEY_MAP
con.lrange(PRIZE_POOL_KEY_MAP[ActivityType.SPORTS_TEAM], 0, -1)
con.lrange(PRIZE_POOL_KEY_MAP[ActivityType.SPORTS_PERSONAL], 0, -1)

from django_redis import get_redis_connection
con = get_redis_connection()
team_id = 'HH575753'
from datetime import datetime
datetime.today().date()  # 手动改为要加的那一天
str = '2023-05-23'
key = f"{team_id}_{str}_punch_members"
con.sadd(key, 'shangli')
"""

a = "{}{}".format("awda", "_is_ieg_user")
print(a)

from datetime import datetime

print(datetime.now().date())


def isalnum(name):
    import re
    return re.compile(r'^[0-9a-zA-Z_\u4e00-\u9fa5]+$').match(name)


print(isalnum("211dsw"))
print(isalnum("211"))
print(isalnum("我代打"))
print(isalnum("21带我玩的1"))
print(isalnum("我代dwad打"))
print(isalnum("我代dwad打12312"))
print(isalnum("∫"))
print(isalnum("饕鬄"))
print(isalnum("饕鬄____"))
print(isalnum("213___waej"))
print(isalnum("__"))
print(isalnum("__ "))
print(isalnum("😃"))

'''
con = get_redis_connection()
user_img = con.get(f"{username}_ieg_user_img")
if not user_img:
    # ...
    # user_img = ...
    con.set(f"{username}_ieg_user_img", user_img, 24*60*60)

return img 

logger.info(f"图片获取URL请求成功")


'''

for i in range(2):
    print(i)

if date(*map(int, '2023-5-22'.split('-'))) == datetime.today().date():
    print("dswaddadwfvbvgbfgbbf")

print(json.loads(
    '{"code":0,"data":{"list":null,"top_list":null,"total":0,"sum":0,"top_sum":0,"all_dimension_sum":0},"msg":"succ"}'))

monitor_infos = {"data": {"list": None}}
for instance_dict in monitor_infos["data"]["list"] or []:
    print(":awdad")

'''
import psutil

# 获取当前进程ID
pid = os.getpid()

# 获取当前进程对象
p = psutil.Process(pid)

# 获取CPU使用情况
cpu_percent = p.cpu_percent(interval=1)
print(f"CPU使用率: {cpu_percent}%")  # CPU使用率: 0.0%

# 获取内存使用情况
mem_info = p.memory_info()
mem_rss = mem_info.rss / 1024 / 1024
mem_vms = mem_info.vms / 1024 / 1024
print(f"内存占用: {mem_rss:.2f} MB (物理内存), {mem_vms:.2f} MB (虚拟内存)")  # 内存占用: 16.48 MB (物理内存), 8.59 MB (虚拟内存)
'''

# class CharField(Field):
# def __init__(self, *args, **kwargs):
#     super().__init__(*args, **kwargs)
#     self.validators.append(validators.MaxLengthValidator(self.max_length))
#
# def check(self, **kwargs):
#
# def _check_max_length_attribute(self, **kwargs):
#
# def cast_db_type(self, connection):
#
# def get_internal_type(self):
#
# def to_python(self, value):
#
# def get_prep_value(self, value):
#
# def formfield(self, **kwargs):


# from multiprocessing import Pool
#
#
# def square(x):
#     return x * x
#
#
# with Pool(processes=4) as pool:
#     numbers = [1, 2, 3, 4, 5]
#     results = pool.map(square, numbers)
#     print("Results:", results)  # Results: [1, 4, 9, 16, 25]


'''
def list_of_groups(init_list, childern_list_len):
    """
    将长列表切分成指定长度
    """
    if not init_list:
        return []
    list_of_group = zip(*(iter(init_list),) * childern_list_len)
    end_list = [list(i) for i in list_of_group]
    count = len(init_list) % childern_list_len
    end_list.append(init_list[-count:]) if count != 0 else end_list
    return end_list


print(list_of_groups([1,2,3,4,5], 2))  # [[1, 2], [3, 4], [5]]
metric_list = ["hh", "xix"]
A = [[1,2],[3,4],[5]]

from itertools import product
for metric_name, clb_list in product(metric_list, A):
    print(metric_name, clb_list)
'''

# # 输出结果
# for x, y, result in zip(input_values_x, input_values_y, results):
#     print(f"{x} * {y} = {result}")
