import hashlib
import json
from datetime import datetime


class Block:
    """
        区块结构
            prev_hash:      父区块哈希值
            transactions:           交易对
            timestamp:      区块创建时间
            hash:           区块哈希值
            Nonce:        随机数
    """

    def __init__(self, transactions, prev_hash):
        # 将传入的父哈希值和数据保存到类变量中
        self.prev_hash = prev_hash
        self.transactions = transactions
        # 获取当前时间
        self.timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # 设置Nonce和哈希的初始值为None
        self.nonce = None
        self.hash = None

    def get_hash(self):
        return self.hash

    def __repr__(self):
        return "区块内容：%s\n哈希值: %s" % (json.dumps(self.transactions), self.hash)
