# 概率论

## 基本概念

* 期望
  * $$E(f(x))=\sum_{k=1}^n{f(x_k)P(x_k)}$$
  * $$E(f(x))=\int_{-\infty}^{+\infty}{f(x)p(x)dx}$$
* $$E(f(x)) \ne f(E(x))$$
  * 函数的期望不一定等于期望的函数
* $$E(A + B) = E(A) + E(B)​$$
* $$E(AB) \ne E(A)E(B)$$
  - 乘积的期望不一定等于期望的乘积
  -  A, B 独立时相等
* 方差
  * $$Var(x) = E((x - E(x))^2 = E(x^2) - E^2(x)$$
* $$Var(A + B) \ne Var(A) + Var(B)​$$
  * A, B 不相关时相等
* 协方差
  * $$COV(A, B) = E((A - E(A)(B-E(B))) = E(AB) - E(A)E(B)$$
* 无关
  * $$COV(A, B) = 0​$$
* 独立
  * $$P(AB) = P(A)P(B)​$$
* 独立一定无关，无关不一定独立
* 条件概率公式
  * $$p(A|B)=\frac{P(A, B)}{P(B)}$$

## 概率模型

### 基本概念

* 描述：基于物体的某种内在属性 $$y​$$，物体呈现出了某种可观测性质 $$x​$$。则式 $$p(y|x)​$$ 意为通过可观测性质 $$x​$$ 反推出物体有内在属性 $$y​$$ 的概率分布。不妨称 $$y​$$ 为 因，$$x​$$ 为果。
* 判别式模型直接建模 $$p(y|x)$$
  * 决策树，神经网络，支持向量机
* 生成式模型先对 $$p(x,y)$$ 建模，再由 $$p(y|x)=\frac{p(x, y)}{p(x)}$$ 得到 $$p(y|x)$$
  * 贝叶斯分类器，贝叶斯网

* 贝叶斯公式

$$
p(y|x)=\frac{p(x|y)p(y)}{p(x)}
$$

* 后验概率 (posterior)
  * $$p(y|x)$$ 
  *  由结果推断原因的概率分布
* 先验概率 (prior)
  * $$p(y)$$
  * 原因概率分布
* 似然估计 (likelihood)
  * $$p(x|y)$$
  * 原因到结果的概率分布
* 证据（evidence）
  * $$p(x)$$
  * 结果的概率分布

### 参数估计

#### 极大似然估计（Maxmimum Likelihood Estimation, MLE）

$$
p(y|x) \varpropto p(x|y)
$$

##### 常用$p(x|y)$先验分布

###### 离散值

* 二项分布
* 泊松分布

###### 连续值

* 正态分布
  $$
  
  $$
  

##### 朴素贝叶斯

基于属性独立假设
$$
p(\boldsymbol{x}|c)=\prod_{x}p(x|c)
$$

#### 最大后验估计（Maximum A Posteriori estimation, MAP）

$$
p(y|x) \varpropto p(x|y)p(y)
$$

#### 贝叶斯估计（Bayesian Estimation）

$$
p(y|x) \varpropto \frac{p(x|y)p(y)}{p(x)}
$$

### 概率估计

* 离散属性：统计频率，可能需要加上拉普拉斯修正，避免“未被观测”被等价于“出现概率为0”
* 连续属性，假设为正态分布，估计均值和方差

## Trick

### 拉普拉斯修正

给每一个估计的概率值都加上一个很小的偏置，使其不为 0

## Reference

1. [极大似然估计与最大后验概率估计](https://zhuanlan.zhihu.com/p/40024110)

2. [最大似然估计、最大后验估计、贝叶斯估计的对比](https://www.cnblogs.com/jiangxinyang/p/9378535.html)

3. [贝叶斯估计、最大似然估计、最大后验概率估计](http://noahsnail.com/2018/05/17/2018-05-17-%E8%B4%9D%E5%8F%B6%E6%96%AF%E4%BC%B0%E8%AE%A1%E3%80%81%E6%9C%80%E5%A4%A7%E4%BC%BC%E7%84%B6%E4%BC%B0%E8%AE%A1%E3%80%81%E6%9C%80%E5%A4%A7%E5%90%8E%E9%AA%8C%E6%A6%82%E7%8E%87%E4%BC%B0%E8%AE%A1/)

