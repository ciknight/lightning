from django.contrib.admin import ModelAdmin as DjangoModelAdmin
from django.utils import six

# 属性的常量声明

# 根据哪个字段进行筛选登录的用户，因为一个模型可能有多个字段指向用户模型
BSM_AUTH_FILTER_FIELD = 'user_field'

# 是否允许根据当前登录用户进行筛选
BSM_FILTER_BY_LOGIN_USER = 'filter_by_login_user'

# 声明父亲字段, 只用来针对树形结构做声明，只能配置单一的字段
BSM_PARENT_FIELD = 'parent_field'

# 属性和默认值映射
ATTRS_DICT = {
    BSM_AUTH_FILTER_FIELD: None,
    BSM_FILTER_BY_LOGIN_USER: True,
    BSM_PARENT_FIELD: None,
}


class BaseMetaclass(type):

    def __new__(cls, name, bases, attrs):
        base_attrs = ATTRS_DICT
        base_attrs.update(attrs)
        return super(BaseMetaclass, cls).__new__(cls, name, bases, base_attrs)


class ModelAdmin(DjangoModelAdmin):

    @six.add_metaclass(BaseMetaclass)
    class GMeta:
        pass


class BSMMetaClass(type):
    """
    重写通用的 Admin 的类，和 Django 的 ModelAdmin 完全区分开来，
    这里为了统一属性的，重写 Meta    
    """

    def __new__(cls, name, bases, attrs):
        base_attrs = ATTRS_DICT
        base_attrs.update(attrs)
        return super(BSMMetaClass, cls).__new__(cls, name, bases, base_attrs)


@six.add_metaclass(BSMMetaClass)
class BSMAdmin:
    """通用套件全局定义管理配置的基类

    用户可以继承此类，然后重新定义配置，然后服务端导出配置，
    前端可以根据配置动态的构造管理后台界面
    """
    pass
