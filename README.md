# mac_dot_config

mac 下 jetbrains 常用操作，如遇到快捷键不生效，goland是最全的，可照此进行配置。

# 终端打开方式

Tools--Create Command-line Launcher，然后就可以用对应命令打开ide，可跟文件或文件夹参数.

- `charm xxx`
- `golang xxx`

# jetbrains快捷键

已经取消双击 shift 打开搜索窗口的设置。

## 移动与选择

| 快捷键                   | 说明                  |
|-----------------------|---------------------|
| control + a/e/f/b/n/h | 光标移动，可同时按shift进行选择  |
| control + [/]         | 屏幕上下滚动单行            |
| control + shift + []  | 屏幕上下滚动一屏            |
| control + l           | 当前行屏幕居中             |
| cmd + l               | 选中整行                |
| cmd + g               | 跳到指定的行列             |
| control + m           | 跳到匹配括号              |
| cmd + 左/右             | 按单词移动               |
| control + ;           | 插件快捷跳到想去的地方         |
| control + q           | 当前部分多光标选择           |
| cmd + shift + 上/下     | 拉出多光标               |

## 编辑操作

| 快捷键                     | 说明                         |
|-------------------------|----------------------------|
| cmd + d                 | 重复一行                       |
| cmd + y                 | 删除一行                       |
| cmd + j                 | 合并下一行                      |
| shift + enter           | 插入空行                       |
| control + u/k           | 删除到行首/尾                    |
| control + h             | 退格                         |
| cmd + delete            | 删除到行首                      |
| cmd + 上/下               | 当前行上移/下移                   |
| cmd + [/]               | 代码段折叠/展开，加上shift折叠/展开所有    |
| cmd + .                 | 展开/折叠切换，仅限括号               |
| cmd + c                 | 复制操作，如果没有选择则复制当前行          |
| cmd + shift + c         | 复制当前路径                     |
| control + j             | 查看文档、签名                    |
| cmd + shift + u         | 大小写转换                      |
| cmd + u                 | 翻译                         |
| control + t             | 重构                         |
| control + enter         | 自动生成子类/重写/单测等等             |
| opt + enter             | 快速自动修错                     |
| control + shift + enter | 同上                         |
| cmd + shift + enter     | 自动补全并跳转光标                  |
| xxx.for/len/nil         | 代码片段补全                     |
| control + g             | 去到定义，相当于鼠标左击               |
| cmd + opt + l           | 自动格式化，pycharm将默认行为改为了blank |

## 界面与窗口操作

| 快捷键                             | 说明                 |
|---------------------------------|--------------------|
| cmd + +/-                       | 放大缩小字体             |
| cmd + shift + +                 | 左右分屏               |
| cmd + shift + \                 | 同上                 |
| control + w，v                   | 同上                 |
| cmd + shift + -                 | 上下分屏               |
| control + w，h                   | 同上                 |
| control + w，上下左右/fbnp           | 窗口切换               |
| control + +/-                   | 窗口宽度增加/减小(x轴增加/缩小) |
| control + shift + +/-           | 窗口高度增加/减小(y轴增加/缩小) |
| control + w，control + w         | 切换到下一个窗口           |
| control + w，control + shift + w | 切换到上一个窗口           |
| cmd + t                         | 打开终端               |
| cmd + w                         | 关闭窗口               |
| cmd + shift + t                 | 重新打开关闭的窗口          |
| cmd + n                         | 创建文件               |
| cmd + `                         | 打开文件窗口             |
| cmd + b                         | 打开书签窗口             |
| cmd + shift + b                 | 添加/取消书签            |
| control + w， 0-9                | 添加0-9号书签           |
| control + 0-9                   | 跳转到0-9号书签          |
| cmd + 1-9                       | 跳转到1-9号打开tab       |
| cmd + s                         | 打开代码结构窗口           |
| cmd + ,                         | 打开配置窗口             |
| cmd + tab                       | 可带shift，切换打开的窗口    |
| shift + Esc                     | 书签/代码结构/目录栏关闭      |
| cmd + ``                        | 切换同任务窗口，系统快捷键      |
| cmd + m                         | 最小化，系统快捷键          | 
| cmd + h                         | 隐藏，系统快捷键           | 
| cmd + q                         | 完全退出，系统快捷键         |


## 搜索与替换操作

| 快捷键             | 说明        |
|-----------------|-----------|
| cmd + p         | 文件/变量模糊搜索 |
| cmd + f         | 当前文件搜索    |
| cmd + shift + f | 所有文件搜索    |
| cmd + r         | 当前文件替换    |
| cmd + shift + r | 所有文件替换    |

## 调试与运行
| 快捷键                 | 说明   |
|---------------------|------|
| control + shift + d | 调试当前 |
| control + shift + r | 运行当前 |

## todo
- 断点调试
- 目录/书签展开折叠快捷键不生效bug
- control + shift + - 向下分屏总是多出一个bug



# iterm2 快捷键
https://www.cnblogs.com/liqiangchn/p/14280203.html

| 快捷键             | 说明        |
|-----------------|-----------|
| cmd + n         | 新的终端 |
| cmd + t         | 新的tab页    |
| cmd + w | 关闭当前页    |
| cmd + 数字         | 指定tab    |
| cmd + shift + r | 所有文件替换    |
| cmd + 上/下 | 上下屏幕滚动    |
| cmd + 左/右 |  前后tab滚动  |
| cmd + home/end | 上下tab到顶/底    |
| cmd + pageUp/pageDown | 上下屏幕翻页    |
| cmd + d         | 垂直分屏 |
| cmd + shift + d        | 水平分屏    |
| cmd + [/] | 切换窗口 |
| cmd + shift + h | 历史剪切板 |
| cmd + ; | 历史命令提示 |
| cmd + opt + b | 历史窗口回放 |




