import codecs
import json

with open(r"C:\Users\894\Desktop\毕业设计\KGQA_HLM-master\spider\json\data.json", encoding='utf-8') as f:
    data = json.load(f)


def get_profile(name):
    s = ''

    # for i in data[name]:
    #     st = "<dt class = \"basicInfo-item name\" >" + str(i) + " \
    #     <dd class = \"basicInfo-item value\" >" + str(data[name][i]) + "</dd >"
    #     s += st
   # return s
    return '123'
