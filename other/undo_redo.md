# 简介
undo/redo设计方案。

# 设计模式
## 命令模式
![命令模式]("F:/books/other/res/command_design.png")

## 备忘录模式
![备忘录模式]("")

# 可持久化数据结构
## 部分可持久化（partial persisten）
在版本轴中，每次只能修改最近的版本（lastest version），每个版本的node可由以下部分组成，
degree_pointer: 与这个数据块相关的指针
field: node本身
value: 数据块的值

版本控制算法过程：
if not 存在field
    创建节点。
else
    更新节点。
    递归处理。

## 全部可持久化（full persisten）
## 可合并持久化（combine persisten）
## 功能函数


# 撤销还原系统设计思路
数据的操作可以抽象为四种，分别是增、删、查、改。其中查是不影响到数据，所以不考虑查这一操作。对于其他三个操作，分别对应的undo、redo如下:

+ 增：
   + undo: del obj
   + redo: add obj

+ 删:
  + undo: add obj
  + redo: del obj

+ 改:
  + undo: change obj old new
  + redo: change obj new old

归纳以下，其实就只涉及三个操作：

+ add obj
+ del obj
+ change obj value1 value2

其中，只要保证add obj在del obj之后，操作都是安全的。

# Python实现撤销还原思路

例子：

```python
class A():
    def __init__():
        self.a = 1
        self.b = 2

t = A()
t.a = obj1()
t.b = obj2()
t.a = t.b
```

version构建：

```text
1. add A
2. add obj1
3. change t.a obj1 1
4. add obj2
5. change t.b obj2 2
6. change t.a obj2 obj1
7. del obj1
```

undo序列：

```text
1. del A
2. del obj1
3. change t.a 1 obj1
4. del obj2
5. change t.b 2 obj2
6. change t.a obj1 obj2
7. add obj1
```



