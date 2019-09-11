[TOC]

# Overview

This Tutorial aims to explain how to quickly construct a web application which contains front end and back end. To be noticed, we will develop all components in the framework of `yarn + webpack`. That is all `*.css` and `*.js` will be packaged into one `index.html` and its assets.

All titles with `WIP` tag means the components should be carefully referenced because they are not intact, which means there may be some mistakes.

# Package Management

## Yarn

### Preparation

Usually we use the `yarn` to help us quickly construct a project skeleton. Make sure [node.js, npm](https://nodejs.org/en/download/), [yarn](https://yarnpkg.com/lang/en/docs/install/#windows-stable) are installed. Use the following instructions to check whether the commands are available:

```sh
node -v
npm -v
yarn -v
```

Due to the possible slow downloading speed, it is considerable to change the yarn source to domestic mirrors:

```bash
# USTC
yarn config set registry http://npmreg.mirrors.ustc.edu.cn/
# TaoBao
yarn config set registry https://registry.npm.taobao.org
```

### Construction

For more instructions, refer to [yarn cheat sheet](https://devhints.io/yarn)

#### Initialization

```bash
yarn init
```

After that, we will get several documents in our project folder. Some important files and usage are list below:

#### CURD

```bash
# Create a dependency/package in production environment
yarn add <Package>
# Create a dependency/package in development environment
yarn add <Package> --dev
# Create a global dependency/package
yarn add <Package> -g
# Update
yarn upgrade <Package>
# Retrieve, list all installed packages
yarn list
# Delete
yarn remove <Package>
```

These packages usually are required in almost projects:

```bash
# webpack
yarn add --dev webpack webpack-cli webpack-dev-server
# babel
yarn add --dev @babel/cli @babel/core @babel/plugin-proposal-class-properties @babel/plugin-proposal-object-rest-spread @babel/preset-env @babel/preset-typescript babel-loader
# Jest
yarn add jest --dev
```

#### Installation

The step to install all required packages with yarn preparing the required packages defined in `package.json`

```sh
yarn install
```

#### Building

For one project, it may reply on several packages (i.e., dependencies) either in production environment or development environment. The former usually is defined in the variable `1` and the later is `2`. They are both in `package.json`. [Here]() is a prototype `package.json`, which predefine  those common used packages in development environment. Another prototype example is used with [vue-cli]()

The main components in `package.json` and their functionalities are listed below:

```
yarn build
```

## Webpack

[webpack]() is a very handy tool to help do something. [Here]() is an example of `webpack.config.js`. To be noticed that the `webpack.config.js` is not necessary when you use some other skeleton tools like `vue`. They will have their own [webpack-style definition]() for different usage. 

# Front End

There are a large number of skeletons for front end, like `vue`, `react` and many blocks like `bootstrap` and `jquery`.

## Vue

To avoid unnecessary misleading, we divide the explanation for `vue` into two part:

- `vue-cli`: purely under the skeleton of `vue`,
- `vue + webpack`: treat `vue` as a package in `webpack`

And here only talk about `vue-cli`. The discussion about `vue + webpack` will be mentioned in [later]()

### Disable Eslint

In `config/index.js`, modify the `useEslint` to `false`

```js
module.exports = {
  dev: {
    useEslint: false,
  }
}
```

### Bootstrap in Vue

Resource: [1](https://bootstrap-vue.js.org/docs/)

### 404

A simplest 404 page template `404.vue` can be

```vue
// 404.vue
<template>
  <div>
    <p>404 - Not Found</p>
  </div>
</template>

```

Add that to route by adding the wildcard character in `routes`, which can be found in `router/index.js`:

```js
export default new Router({
  routes: [
    {
      name: '404',
      path: '/404',
      component: () => import('@/components/404.vue')
    },
    {
      path: '*', //notice that this should be at the bottom of routes
      redirect: '/404'
    }
  ]
})


```



## React

TBA

## Webpack(WIP)

Also, it is possible to construct our own skeleton without others like `vue` and `react`, though it is not suggested. Remember, all discussions about how to use the package in webpack are mainly  involved in three aspects:

- How to import and use in `css/scss`
- How to import and use in `js`
- The necessary modification in `package.json` and `webpack.config.js`

### Bootstrap + Jquery

#### Bootstrap

[速查](http://how2j.cn/k/boostrap/boostrap-tutorial/538.html)

[教程](https://stevenwestmoreland.com/2018/01/how-to-include-bootstrap-in-your-project-with-webpack.html)

##### Installation 

```bash
# dependencies
yarn add jquery popper.js
# Bootstrap
yarn add bootstrap

```

##### Used in js

```js
// import js
import 'bootstrap/dist/js/bootstrap.min'
// import css(not suggested, advise to inlcude the css in style.scss flle)
import "../node_modules/bootstrap/dist/css/bootstrap.css"

```

##### Used in css/scss

```scss
// import all
@import "~bootstrap/dist/css/bootstrap";

// import the needed
// Required
@import "~bootstrap/scss/functions";
@import "~bootstrap/scss/variables";
@import "~bootstrap/scss/mixins";

// Optional
@import "~bootstrap/scss/reboot";
@import "~bootstrap/scss/type";
@import "~bootstrap/scss/images";
@import "~bootstrap/scss/code";
@import "~bootstrap/scss/grid";

```

#### Jquery(WIP)

The most concerned issue must be 

> how to use the $ of jquery in js

One way is to use [expose-loader](https://webpack.js.org/loaders/expose-loader/)

```js
require("expose-loader?$!jquery");

```

[Another way](http://blog.longestm.com/2017/10/12/vue%E5%BC%95%E5%85%A5jquery-bootstrap-webpack/)

### Vue(WIP)

单独一个 vue.app

在`webpack.config.js`里添加

```js
const {VueLoaderPlugin} = require('vue-loader');

module.exports = {
    module: {
        rules: [
            {
                test: /.vue$/,
                loader: 'vue-loader'
            }
        ]
    },
    plugins: [
        new VueLoaderPlugin()
    ]
};

```

Resource: [[1]](https://juejin.im/post/5acd890d6fb9a028d043ca15), [[2]](https://segmentfault.com/a/1190000009466326), [[3]](https://segmentfault.com/a/1190000011280912), [[4]](https://github.com/varHarrie/varharrie.github.io/issues/7), 



# Back End

This part will focus on how to work with the front end skeletons in different back end frameworks like `flask` and `django`

## Flask with Vue

### Vue + Flask

The most simple way to combine these two parts is to start two different service to handle front end and back end separately. More precisely, use the default listening port 8080 of `vue` to provide the front end service and use the default listening port 5000 of `flask` to provide the back end service. In fact, the back end is hidden from users and only can be seen by front end. The front end will request the back end service in inner javascript functions. 

### Vue in Flask

Also, another way is to render the `index.html` directly in `flask` using the `render_template` method. Several points should be noticed as mentioned in Q&A [2](), [3]() and [4](). Indeed, this method can be supplement to [Vue + Flask]().

参考 [1](https://www.zcfy.cc/article/full-stack-single-page-application-with-vue-js-and-flask-4491.html)



### Request passing in F-E (WIP)

Resource: [1](https://codeday.me/bug/20190119/552904.html),[2](https://www.jianshu.com/p/ead7317d01ec)

### Q&A

#### 1. 去除url里的 # 号

A: 修改 `src/router/index.js`的`mode`变量

```js
// 默认无mode关键字，默认模式为 mode: 'hash'
export default new Router({
  mode: 'history',
})


```

#### 2. 修改build生成文件（默认dist）路径

A: 修改 `config/index.js` 中的 `index` 和 `assetRoot`变量

```js
// 变量已修改，和原文件比较
build: {
    // Template for index.html
    index: path.resolve(__dirname, '../../dist/index.html'),

    // Paths
    assetsRoot: path.resolve(__dirname, '../../dist')
}

```

#### 3. Flask 如何渲染Vue通过webpack build生成的模板网页（默认dist/index.html）

A: 注意模板文件路径，在`flask-python`中定义`app`变量时：

```python
# 注意 static_folder 和 template_folder 
# 要指向vue通过webpack build生成的模板网页位置
app = Flask(__name__, static_folder="../dist/static", template_folder="../dist")

```

#### 4. Flask如何使用Vue的路由系统

A: 添加一个 `catch_all`函数来处理所有路由

```python
@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return render_template("index.html")

```

补充问题：这样会不会导致其它路由被捕捉到呢？比如

```python
@app.route('/test')
def test():
    return 'hello world'

```

是否会在vue的路由系统中进行路由？答案是不会的。

### Django with Vue

Resource: [1](https://zhuanlan.zhihu.com/p/25080236)

# Format Configuration

## Jetbrain

### Configure format for `html`



### Set the `.vue` formatter

File  > Settings > Editor > File Types



# Abbreviation

| Abbreviation | Full                          | Explanation               |
| ------------ | ----------------------------- | ------------------------- |
| CURD         | Create-Update-Retrieve-Delete |                           |
| ORM          |                               | The interface to database |
| SSR          | Server Side Rendering         |                           |



### 

