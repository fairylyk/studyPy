#!/usr/bin/python
# vim: set fileencoding=utf-8 :


class TestBasePara(object):

    """
    1、有默认值的参数必须在没有默认值的参数后面，否则会报错SyntaxError
    2、当位置可变参数和关键字可变参数一起使用时候，可变位置参数必须在前
    3、普通参数可以和可变参数一起使用，但是传参的时候必须匹配
    4、关键字可变参数不允许在普通参数之前
    5、位置可变参数可以在普通参数之前，
       但是在位置可变参数之后的普通参数变成可keyword-only 参数（python3特性）
    """

    def basic_fun(self, basic_para):
        """
        :param basic_para: 基本参数
        """
        print 'basic_para：', basic_para

    def default_fun(self, default_para=1):
        """
        :param default_para: 默认参数：没有传参时。使用默认值
        """
        print 'default_para: ',default_para

    def variable_position_fun(self, *variable_position_para):
        """
        :param variable_para: 可变位置参数：定义参数时前面加一个*，表示这个参数是可变的，
        可以接受任意多个参数，这些参数构成一个元组，只能通过位置参数传递
        """
        print
        for arg in variable_position_para:
            print arg

    def variable_key_fun(self, **variable_key_para):
        """
        :param variable_position_para:可变关键字参数：定义参数时，
        在前面加**，表示这个参数可变，可以接受任意多个参数，
        这些参数构成一个字典，只能通过关键字参数传递
        """
        print
        for key, value in variable_key_para.iteritems():
            print key + ":" + value

    def test_call_fun(self):

        # basic_para： basicPara
        self.basic_fun("basicPara")

        # result:1
        self.default_fun()
        # result:66
        self.default_fun("66")

        # result:
        # Java
        # Python
        # C + +
        self.variable_position_fun('Java', 'Python', 'C++')

        # result:
        # Python:6
        # C:3
        # Java:5
        self.variable_key_fun(Java='5', Python='6', C="3")
