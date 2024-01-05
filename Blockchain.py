class BlockChain:
    """
        区块链结构体
            blocks:        包含的区块列表
    """

    def __init__(self):
        self.blocks = []

    def add_block(self, block):
        """
        添加区块
        """
        self.blocks.append(block)

    def last_block(self):
        l = len(self.blocks)
        return self.blocks[l - 1]

    def print_list(self):
        print("区块链包含区块个数: %d\n" % len(self.blocks))
        for block in self.blocks:
            print("上个区块哈希：%s" % block.prev_hash)
            print("区块内容：%s" % block.transactions)
            print("区块哈希：%s" % block.hash)
            print("\n")


def get_balance(blockchain,user):
    balance = 0
    for block in blockchain.blocks:
        for t in block.transactions:
            if t.sender == user.address.decode():
                balance -= t.amount
            elif t.recipient == user.address.decode():
                balance += t.amount
    return balance
