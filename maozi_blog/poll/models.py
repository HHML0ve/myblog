# coding:utf-8
import datetime

from django.db import models

# Create your models here.
from django.db import models
from django.utils import timezone


# 改变模型需要这三步：
#
# 编辑 models.py 文件，改变模型。
# 运行 python manage.py makemigrations 为模型的改变生成迁移文件。
# 运行 python manage.py migrate 来应用数据库迁移。


class Question(models.Model):
    question_text = models.CharField('question text', max_length=200)
    pub_date = models.DateTimeField('date published')

    # 给模型增加 __str__() 方法是很重要的，这不仅仅能给你在命令行里使用带来方便，Django 自动生成的 admin 里也使用这个方法来表示对象
    # 命令行中使用的命令是： Question.object.all()
    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    # cascade 外键级联 当父表question更新的时候，字表choice跟着更新
    # （如果表 A 中有一个外键引用了表 B 的主键，A 表就是子表，B 表就是父表。当查询表 A 的数据时，通过表 A 的外键将表 B 的相关记录返回，这就是级联查询。）
    # Django 支持所有常用的数据库关系：多对一、多对多和一对一。
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text

# 表名为 app名+类名  eg. poll_question 如果需要可以重新定义
# 字段名会作为数据库中的列名, 如果不使用可选项也会作为人类友好名使用。可选项的使用方法如同 ‘date publishe’

# 当安装完app的后运行如下命令
# py manage.py sqlmigrate app_name 0001
# salmigrate命令只是打印在控制行，并未真实的执行。 真正执行的命令如下：
# py manage.py migrate

# 运行 python manage.py check ;这个命令帮助你检查项目中的问题，并且在检查过程中不会对数据库进行任何操作
