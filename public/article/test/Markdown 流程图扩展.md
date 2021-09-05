# Markdown 流程图扩展

## 元素

元素|说明|图例
-|-|-
start|开始|圆角矩形
end|结束|圆角矩形
operation|操作|矩形
subroutine|预定义(子程序)|两个上下边重合的嵌套矩形
condition|判断(条件)|菱形
inputoutput|输入输出|平行四边形
(content)|图例上显示的文本内容(不是可自定义的图例类型)，可以换行|
(url)|图例文本上的超链接(不是可定义的图例类型)，可选添加|

## 示例

```text
\```flow
fstart=>start: 开始
foperation=>operation: 操作,链接:>http://uniqueding.cn
fsubroutine=>subroutine: 子系统
fcondition=>condition: 判断
finputoutput=>inputoutput: 输入输出
fend=>end: 结束

fstart->foperation->fcondition
fcondition(yes)->finputoutput->fend
fcondition(no)->fsubroutine->finputoutput
\```
```

```flow
fstart=>start: 开始
foperation=>operation: 操作,链接:>http://uniqueding.cn
fsubroutine=>subroutine: 子系统
fcondition=>condition: 判断
finputoutput=>inputoutput: 输入输出
fend=>end: 结束

fstart->foperation->fcondition
fcondition(yes)->finputoutput->fend
fcondition(no)->fsubroutine->finputoutput
```

### 参考文献

[https://blog.csdn.net/wilson1068/article/details/86708610][1]

[1]: https://blog.csdn.net/wilson1068/article/details/86708610
