from  lib import  cmd_route_table
import svc



while True:
    op = input('请输入你的操作：')

    # 如果能找到改指令的处理函数
    if op in cmd_route_table:
        # 查找改指令对应的业务处理函数
        svcFunc = cmd_route_table[op]
        # 调用业务处理函数
        svcFunc()

    else:
        print('该指令没有对应业务处理')