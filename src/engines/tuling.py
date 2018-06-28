#!/usr/bin/env python
# encoding=utf-8
# The MIT License (MIT)
#
# Copyright (c) 2018 Bluewhale Robot
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
#
# Author: Randoms
#

import rospy
import requests
import json

class Tuling:

    def __init__(self):
        self.apikey = rospy.get_param(
            "~apikey", "48729e91db1549669dc305fdf3efa6c5")
        self.userid = rospy.get_param("~userid", "284385")

    def talk(self, words):
        res = requests.post("http://openapi.tuling123.com/openapi/api/v2", json={
            "reqType": 0,
            "perception": {
                "inputText": {
                    "text": words,
                },
            },
            "userInfo": {
                "apiKey": self.apikey,
                "userId": self.userid
            }
        })
        if res.status_code != 200:
            return ""
        res = json.loads(res.content.decode("utf-8"))
        if res["intent"]["code"] < 10000:
            rospy.logerr(res["results"][0]["values"]["text"])
            return ""
        return res["results"][0]["values"]["text"]
        
