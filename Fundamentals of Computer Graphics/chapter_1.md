# 第一章 介绍

## 图形学领域

最核心有三部分：

* 模型
* 渲染
* 动画

其他重要的部分：

* 用户交互（UI）
* 虚拟现实
* 可视化
* 图片处理
* 3D扫描
* 计算摄影

## 专业应用

图形学应用很广泛，其中涉及的相关行业如下：

* 电子游戏
* 动画
* 视觉效果
* 动作电影
* CAD/CAM
* 场景模拟
* 医学影像
* 信息可视化

## 图形APIs

## 绘图流水线

将三维模型渲染到二维平面的过程。wiki介绍如下：

> **绘图流水线**(Graphics pipeline，亦称**绘图管线**)是电脑图形系统将三维模型[渲染](https://zh.wikipedia.org/wiki/%E6%B8%B2%E6%9F%93)到二维屏幕上的过程。简单地说，当一个在[电子游戏](https://zh.wikipedia.org/wiki/%E7%94%B5%E5%AD%90%E6%B8%B8%E6%88%8F)或[三维动画](https://zh.wikipedia.org/wiki/%E4%B8%89%E7%B6%AD%E5%8B%95%E7%95%AB)内的[三维模型](https://zh.wikipedia.org/wiki/%E4%B8%89%E7%BB%B4%E6%A8%A1%E5%9E%8B)被创建的时候，绘图流水线就是把该模型转换成屏幕画面的过程。由于这个过程中所进行的操作严重依赖用户所使用的软件、硬件等，因此并不存在通用的绘图流水线。尽管如此，现今存在着类似[OpenGL](https://zh.wikipedia.org/wiki/OpenGL)和[DirectX](https://zh.wikipedia.org/wiki/DirectX)的图形接口，将相似的操作统一起来，并把底层硬件[抽象化](https://zh.wikipedia.org/wiki/%E6%8A%BD%E8%B1%A1%E5%8C%96_(%E8%A8%88%E7%AE%97%E6%A9%9F%E7%A7%91%E5%AD%B8))，以减轻程序员的负担。
>
> 大多时候，绘图管线都是用硬件实现的。其与现代[中央处理器](https://zh.wikipedia.org/wiki/%E4%B8%AD%E5%A4%AE%E5%A4%84%E7%90%86%E5%99%A8)的流水线相似，所有步骤都会以并行的形式运行。

其中涉及到的通用技术有：

* 4维矩阵的运算
* z-buffer
* 面剔除
* Level Of Detail（LOD）

## 数字问题

 在现代计算机中，几乎所有的浮点值都符合IEEE标准。

## 效率

一般来说，都是需要具体问题具体分析的，才能做到最好的优化。但一下几点优化建议，一般来说，都是通用的。

1. 代码写得越直白越好。
2. 使用优化方式来编译。
3. 使用性能测试工具查找程序性能瓶颈。
4. 检查数据结构定义。如果可以，把数据设计成内存对伊模式。
5. 

## 设计和编写图形程序

### 类设计

### float和double比较

### 图形程序的调试

* 科学的方法

大意是，对于一些懵懵懂懂的概念，可以通过假说-实验的方法，一步步来正确理解这个概念。

* 图片作为调试的输出

大意是，将想要调试的信息转换成rbga的形式，然后在图片上着色。

* 调试方式
* 数据可视化调试

在一堆的调试信息中，获取自己关心的信息，则需要良好的规范的调试数据输出格式。有助于阅读和查找。