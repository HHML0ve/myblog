from django.urls import path

from . import views

urlpatterns = [
    path('content', views.knowledge, name='knowledge'),
    path('catalog', views.catalog, name='catalog')
]

# 函数 path() 具有四个参数，两个必须参数：route 和 view，两个可选参数：kwargs 和 name。

# 1 route 是一个匹配 URL 的准则（类似正则表达式）。
#   当 Django 响应一个请求时，它会从 urlpatterns 的第一项开始，按顺序依次匹配列表中的项，直到找到匹配的项。
#   处理请求 https://www.example.com/myapp/?page=3 时，也只会尝试匹配 myapp/

# 2 view 当 Django 找到了一个匹配的准则，就会调用这个特定的视图函数，并传入一个 HttpRequest 对象作为第一个参数，被“捕获”的参数以关键字参数的形式传入。

# 3 kwargs 任意个关键字参数可以作为一个字典传递给目标视图函数。本教程中不会使用这一特性。

# name 为你的 URL 取名能使你在 Django 的任意地方唯一地引用它，尤其是在模板中。这个有用的特性允许你只改一个文件就能全局地修改某个 URL 模式


# 在使用的过程中遇到的问题
# 1、当urlpatterns中只有一个path函数时候，第一个参数route 应该为空，否则找不到路由
