"""
    1、存储商品信息的字典名由 shang_pin_info 改为 dict_commodity_info
    2、存储顾客订单的列表名由 ding_dan 改为 list_order
    3、原函数名由 gou_wu() 改为 select_menu()
    4、将大函数select_menu() 划分为2个函数，购物 buying() 和订单处理 settlement()
    5.1、将buying() 划分为2个函数，打印商品信息 print_commodity_info() 和创建订单 create_order()
    5.1.1、print_commodity_info()：遍历字典dict_commodity_info，格式化打印
    5.1.2、create_order() 内抽离出获取商品id函数 input_commodity_id()
    6.1、将settlement()划分为3个函数打印订单信息 print_orders()、计算总价 calculate_total_price() 和支付 paying(total_price)
    6.1.1、print_orders()：遍历列表list_order，格式化打印
    6.1.2、calculate_total_price()：总价 zong_jia 改为 total_price
    6.1.3、paying(total_price)：钱由 qian 改为 money
"""

dict_commodity_info = {
    101: {"name": "屠龙刀", "price": 10000},
    102: {"name": "倚天剑", "price": 10000},
    103: {"name": "九阴白骨爪", "price": 8000},
    104: {"name": "九阳神功", "price": 9000},
    105: {"name": "降龙十八掌", "price": 8000},
    106: {"name": "乾坤大挪移", "price": 10000}
}

list_order = []


def select_menu():
    """
        选择菜单
    """
    while True:
        item = input("1键购买，2键结算。")
        if item == "1":
            buying()
        elif item == "2":
            settlement()


def settlement():
    """
        结算
    """
    print_orders()
    total_price = calculate_total_price()
    paying(total_price)


def paying(total_price):
    """
        支付过程
    :param total_price: 需要支付的价格
    """
    while True:
        money = float(input("总价%d元，请输入金额：" % total_price))
        if money >= total_price:
            print("购买成功，找回：%d元。" % (money - total_price))
            list_order.clear()
            break
        else:
            print("金额不足.")


def calculate_total_price():
    """
        计算总价格
    """
    total_price = 0
    for order in list_order:
        commodity = dict_commodity_info[order["cid"]]
        total_price += commodity["price"] * order["count"]
    return total_price


def print_orders():
    """
        打印订单
    """
    for order in list_order:
        commodity = dict_commodity_info[order["cid"]]
        print("商品：%s，单价：%d,数量:%d." % (commodity["name"], commodity["price"], order["count"]))


def buying():
    """
        购买
    """
    print_commodity_info()

    create_order()

    print("添加到购物车。")


def create_order():
    """
        创建订单
    """
    cid = input_commodity_id()
    count = int(input("请输入购买数量："))
    order = {"cid": cid, "count": count}
    list_order.append(order)


def input_commodity_id():
    """
        获取商品订单
    """
    while True:
        cid = int(input("请输入商品编号："))
        if cid in dict_commodity_info:
            break
        else:
            print("该商品不存在")
    return cid


def print_commodity_info():
    """
        打印商品信息
    """
    for key, value in dict_commodity_info.items():
        print("编号：%d，名称：%s，单价：%d。" % (key, value["name"], value["price"]))


select_menu()
