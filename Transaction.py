import json

class Transaction:
    def __init__(self, sender, recipient, amount):
        if isinstance(sender, bytes):
            sender = sender.decode('utf-8')
        self.sender = sender  # 发送方
        if isinstance(recipient, bytes):
            recipient = recipient.decode('utf-8')
        self.recipient = recipient  # 接收方
        self.amount = amount  # 交易数量
        self.signature = None  # 交易发起方签名
        self.pubkey = None  # 交易发送方的公钥

    def set_sign(self, signature, pubkey):
        self.signature = signature  # 签名
        self.pubkey = pubkey  # 发送方公钥

    def __repr__(self):
        if self.sender:
            s = "从 %s 转至 %s %f个加密货币" % (self.sender, self.recipient, self.amount)
        else:
            s = "%s 挖矿获取%d个加密货币" % (self.recipient, self.amount)
        return s


class TransactionEncoder(json.JSONEncoder):
    """
    定义Json的编码类，用来序列化Transaction
    """

    def default(self, obj):
        if isinstance(obj, Transaction):
            return obj.__dict__
        else:
            return json.JSONEncoder.default(self, obj)
