# AICheckPayload
Check Payload By AI!

![](https://verylargefile.huolongguo1o.repl.co/image/0.1)![](https://verylargefile.huolongguo1o.repl.co/image/0.2)![](https://verylargefile.huolongguo1o.repl.co/image/0.3)![](https://verylargefile.huolongguo1o.repl.co/image/0.4)![](https://verylargefile.huolongguo1o.repl.co/image/0.5)![](https://verylargefile.huolongguo1o.repl.co/image/0.6)![](https://verylargefile.huolongguo1o.repl.co/image/0.7)![](https://verylargefile.huolongguo1o.repl.co/image/0.8)![](https://verylargefile.huolongguo1o.repl.co/image/0.9)![](https://verylargefile.huolongguo1o.repl.co/image/0.10)![](https://verylargefile.huolongguo1o.repl.co/image/0.1)![](https://verylargefile.huolongguo1o.repl.co/image/0.2)![](https://verylargefile.huolongguo1o.repl.co/image/0.3)![](https://verylargefile.huolongguo1o.repl.co/image/0.4)![](https://verylargefile.huolongguo1o.repl.co/image/0.5)![](https://verylargefile.huolongguo1o.repl.co/image/0.6)![](https://verylargefile.huolongguo1o.repl.co/image/0.7)![](https://verylargefile.huolongguo1o.repl.co/image/0.8)![](https://verylargefile.huolongguo1o.repl.co/image/0.9)![](https://verylargefile.huolongguo1o.repl.co/image/0.10)

## 1.引入

传统的检测方式很容易漏报/误报，开发者往往不能一次性掌握各种软件的全部特性和所有漏洞，松一些会导致出现漏报或绕过，紧一些（例如过滤全部单引号以防sql注入）会影响体验；而针对每种攻击/poc/exp/漏洞都需要重写代码或者正则表达式，很麻烦。机器学习就能完美解决以上问题。

## 2.介绍

[AICheckPayload](https://github.com/huolongguo1O/AICheckPayload)旨在利用机器学习识别危险参数，比传统方式更加方便快捷，且能识别潜在的漏洞（在没有针对log4j2的poc[5]训练的情况下，识别出了log4j2的poc是危险的）。

AICheckPayload是基于bert-base-uncased[4]（transformer encoder架构）的，tiny版基于bert-tiny。


## 3.训练

我在kaggle[2]平台上利用transformers的trainer api完成了训练。

以下是一些训练Tiny[3]版本的信息：
```
epoch：3
step：10896
学习率：从5e-5开始下降(AdamW)
数据集：huolongguo10/insecure
```

下图是loss的情况：

![image](https://user-images.githubusercontent.com/121071167/235354071-f1dea154-7ef2-435b-87f1-d84d767f67a8.png)

## 4.效果

我们用了一个[全新的数据集](https://huggingface.co/datasets/huolongguo10/check_sec_eval)来检验效果。结果：

![7b4c018d147a2d94dfc8f55c849c39b](https://user-images.githubusercontent.com/121071167/235436288-88499ddc-cada-4a6f-b302-7d0930d9f07e.png)

整体来说，95%的准确率不算很高，但这只是一个初步的训练，微调之后效果可能会更佳。

Tiny[3]版不但没用降低准确率，反而比原版更高[1]（多对了一个），且速度更快。

## 5.问题

测试发现脸滚键盘也会被报insecure，另外只要有大于号或小于号就会报不安全，有待提高。

## 6.地址

https://huggingface.co/huolongguo10/check_sec_tiny

https://huggingface.co/huolongguo10/check_sec

https://huggingface.co/spaces/huolongguo10/huolongguo10-check_sec

[1]: https://huggingface.co/spaces/huolongguo10/evaluator_cs 
[2]: https://www.kaggle.com/
[3]: https://huggingface.co/huolongguo10/check_sec_tiny
[4]: https://huggingface.co/bert-base-uncased
[5]: https://www.cnblogs.com/peace-and-romance/p/15717457.html
