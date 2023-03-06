from lib import cmd_dispatch

@cmd_dispatch('查询价格')
def queryPrice():
    # 具体的查询价格处理代码
    print('执行查询价格的业务')


@cmd_dispatch('退货')
def refund():
    # 具体的退货处理代码
    print('执行退货的业务')