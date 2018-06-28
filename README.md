# xiaoqiang_nlp

小强自然语言处理程序，后端采用图灵机器人api。配合xiaoqiang_tts包可以实现和人聊天的功能。

启动

```bash
roslaunch xiaoqiang_nlp tuling.launch
```

|输入话题|话题类型|
|:--|:--|
|~listen|std_msgs/String|


|输出话题|话题类型|
|:--|:--|
|~talk|std_msgs/String|

详细参数可以参照launch文件