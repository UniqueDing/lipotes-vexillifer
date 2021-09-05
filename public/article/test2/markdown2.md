# markdown

![logo](img.png)

## markdown简介

Markdown是一种可以使用普通文本编辑器编写的标记语言，通过简单的标记语法，它可以使普通文本内容具有一定的格式。

创始人为 **约翰·格鲁伯**[^john]（英语：John Gruber）

---

## python

```python
    def a(x):
        return x + 1
```

## markdown语法

### 区块元素

#### 标题

```
This is an H1
=============

This is an H2
-------------
```

```
# 这是 H1

## 这是 H2

###### 这是 H6
```


#### 区块引用

```
> This is the first level of quoting.
>
> > This is nested blockquote.
>
> Back to the first level.
```

> This is the first level of quoting.
>
> > This is nested blockquote.
>
> Back to the first level.

#### 列表

##### 无序列表

```
*   Red
*   Green
*   Blue
+   Red
+   Green
+   Blue
-   Red
-   Green
-   Blue
```

- Red
- Green
- Blue

##### 有序列表

```
1.   Red
2.   Green
3.   Blue
```

1. Red
2. Green
3. Blue

#### 代码区块

支持高亮代码

```

 ```python
    def hello:
        print('hello world!')
 ```

```

```python
    def hello:
        print('hello world!')
```

#### 分隔线

```
* * *

***

*****

- - -

---------------------------------------
```

---

### 区块元素2

#### 链接

```
This is [an example](http://example.com/ "Optional Title Here") inline link.

This is [an example] [id] reference-style link.
[id]: http://example.com/  "Optional Title Here"
```

This is [an example] [id]

[id]: http://example.com/  "Optional Title Here"

#### 强调

```
*single asterisks*

_single underscores_

**double asterisks**

__double underscores__
```

*single asterisks*
_single underscores_
**double asterisks**
__double underscores__

#### 代码

```
Use the `printf()` function.
```

Use the `printf()` function.

#### 图片

```
![Alt text](img.png "Optional title")

![Alt text][id]
[id]: url/to/image  "Optional title attribute"
```

![Alt text](img.png "Optional title")

### 其它

#### 流程图

```flow
st=>start: Start
op=>operation: Your Operation
cond=>condition: Yes or No?
e=>end

st->op->cond
cond(yes)->e
cond(no)->op
```

#### 序列图

```seq
Alice->Bob: Hello Bob, how are you?
Note right of Bob: Bob thinks
Bob-->Alice: I am good thanks!
```

#### 甘特图

```gantt
    title 项目开发流程
    section 项目确定
        需求分析       :a1, 2016-06-22, 3d
        可行性报告     :after a1, 5d
        概念验证       : 5d
    section 项目实施
        概要设计      :2016-07-05  , 5d
        详细设计      :2016-07-08, 10d
        编码          :2016-07-15, 10d
        测试          :2016-07-22, 5d
    section 发布验收
        发布: 2d
        验收: 3d
```

#### 表格

| 项目        | 价格   |  数量  |
| --------   | :-----:  | :----:  |
| 计算机     | 1600 |   5     |
| 手机        |   12   |   12   |
| 管线        |    1    |  234  |

#### 公式（LaTeX）

$$E=mc^2$$

#### 标记

```
    stam[^stam]
    [^stam]:This is a stam
```

stam [^stam]

[^stam]:This is a stam

[^john]: [约翰·格鲁伯][1]（英语：John Gruber，1973－）是一名来自美国宾夕凡尼亚州的作家、网志编者、用户介面设计师及Markdown发布格式的发明者。

[1]:https://zh.wikipedia.org/wiki/約翰·格魯伯

