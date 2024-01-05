import json
import hashlib
from Transaction import Transaction, TransactionEncoder

class ProofOfWork:
    """
        工作量证明
    """

    def __init__(self, block, miner, difficult=5):
        self.block = block

        # 定义工作量难度，默认为5，表示有效的哈希值以5个“0”开头
        self.difficulty = difficult

        self.miner = miner
        # 添加挖矿奖励
        self.reward_amount = 1

    def mine(self):
        """
            挖矿函数
        """
        i = 0
        prefix = '0' * self.difficulty

        # 添加奖励
        t = Transaction(
            sender="",
            recipient=self.miner.address,
            amount=self.reward_amount
        )
        sig = self.miner.sign(json.dumps(t, cls=TransactionEncoder))
        t.set_sign(sig, self.miner.pubkey)
        self.block.transactions.append(t)

        while True:
            message = hashlib.sha256()
            message.update(str(self.block.prev_hash).encode('utf-8'))
            # 更新区块中的交易数据
            message.update(str(self.block.transactions).encode('utf-8'))
            message.update(str(self.block.timestamp).encode('utf-8'))
            message.update(str(i).encode("utf-8"))
            digest = message.hexdigest()
            if digest.startswith(prefix):
                self.block.nonce = i
                self.block.hash = digest
                return self.block
            i += 1

    def validate(self):
        """
            验证有效性
        """
        message = hashlib.sha256()
        message.update(str(self.block.prev_hash).encode('utf-8'))
        # 更新区块中的交易数据
        message.update(json.dumps(self.block.transactions).encode('utf-8'))
        message.update(str(self.block.timestamp).encode('utf-8'))
        message.update(str(self.block.nonce).encode('utf-8'))
        digest = message.hexdigest()

        prefix = '0' * self.difficulty
        return digest.startswith(prefix)
