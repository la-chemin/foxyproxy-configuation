## 前言
个人觉得最好的PAC软件是Chrome上的SwitchyOmega，Firefox上虽然也有类似的插件——FoxyProxy，但是却不支持规则订阅；
本文档是解决这个问题过程的一个记录，权当参考。

## 关于和谐列表
在Github上的[和谐列表](https://github.com/gfwlist/gfwlist)，是一个用base64编码的URL规则文件，分析这个文件，发现以下几个特点：
- 所有以 感叹号 ! 开始的都是注释
- 符合URL规则的单行是一个有效的URL规则
- 单行含有@或者|符号的也也是有效的URL规则
- 如果单行含有@或者|符号，那么URL前面最后一个符号一定是|
- 和谐列表包含几个块，被和谐的和白名单块，和谐块以含有"General List End"的注释行结束，我们只需要这个块就够了

## 关于FoxyProxy
FoxyProxy支持配置的导入和导出，结合上面关于和谐列表的描述，只需要将FoxyProxy的空配置导出，填充和谐列表后， 再重新导入配置
这样，FoxyProxy就可以根据和谐列表的内容为浏览请求作代理切换了。

## 关于脚本
转换流程已经写在了脚本里，执行后可以得到一个新的FoxyProxy配置文件，再导入到插件内就可以使用

你可以在[Github](https://github.com/la-chemin/foxyproxy-configuation)找到我的代码
