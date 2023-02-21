import os
import pprint
import json

files = os.listdir(path='.')
#pprint.pprint(files)

with open("formatted.txt",mode="w",encoding="utf-8") as fw:
    for jsonfile in files:
        if jsonfile.endswith(".json"):
            with open(jsonfile,encoding="utf-8") as f:
                contentjson = json.load(f)
                #pprint.pprint(contentjson)
                for message in contentjson:
                    username =""
                    if "user_profile" in message:
                        if "real_name" in message["user_profile"]:
                            username = message["user_profile"]["real_name"]

                    msg = message["text"]
                    #print(username)
                    #print(msg)
                    fw.write("{}:{}\r\n".format(username,msg))
                    fw.write("------------------------------------------------------------------------\r\n")