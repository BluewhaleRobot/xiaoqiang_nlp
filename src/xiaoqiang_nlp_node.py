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
from std_msgs.msg import String
from engines.tuling import Tuling
import time

if __name__ == "__main__":
    rospy.init_node("xiaoqiang_nlp", anonymous=False)
    result_pub = rospy.Publisher("~talk", String, queue_size=10)
    engine = rospy.get_param("~engine", "tuling")

    # init client
    client = None
    if engine == "tuling":
        client = Tuling()

    if client is None:
        rospy.logerr("Unknown engine {engine}".format(engine=engine))

    # set listen sub
    processing_flag = False

    def listen_cb(words):
        global processing_flag
        if processing_flag:
            return
        if words.data == "":
            return
        processing_flag = True
        result_msg = String()
        result_msg.data = client.talk(words.data)
        result_pub.publish(result_msg)
        processing_flag = False

    listen_sub = rospy.Subscriber("~listen", String, listen_cb)
    while not rospy.is_shutdown():
        time.sleep(1)
