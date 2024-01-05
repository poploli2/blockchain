from Transaction import Transaction
from Block import Block
from Blockchain import BlockChain, get_balance
from Wallet import Wallet, verify_sign
from PoW import ProofOfWork

# 初始化区块链               2,3,4,5四个区块每个区块三个交易，至少三个用户
blockchain = BlockChain()

# 创建三个钱包，一个属于alice，一个属于tom，剩下一个属于bob
alice = Wallet()
tom = Wallet()
bob = Wallet()

# 打印当前钱包情况
print("alice: %d个加密货币" % (get_balance(blockchain, alice)))
print("tom: %d个加密货币" % (get_balance(blockchain, tom)))
print("bob: %d个加密货币" % (get_balance(blockchain, bob)))

# alice生成创世区块，并添加到区块链中

new_block1 = Block(transactions=[], prev_hash="")
w1 = ProofOfWork(new_block1, alice)
genesis_block = w1.mine()
blockchain.add_block(genesis_block)


# 显示alice当前余额

print("alice: %d个加密货币" % (get_balance(blockchain, alice)))


# alice 转账给 tom 0.3个加密货币
transactions = []
new_transaction = Transaction(
    sender=alice.address,
    recipient=tom.address,
    amount=0.3
)
sig = alice.sign(str(new_transaction))
new_transaction.set_sign(sig, alice.pubkey)

# bob 在网络上接收到这笔交易，进行验证没问题后生成一个新的区块并添加到区块链中

if verify_sign(new_transaction.pubkey,
               str(new_transaction),
               new_transaction.signature):

    # 验证交易签名没问题，生成一个新的区块
    print("验证交易成功")
    #获取最后一个区块的哈希值
    prev_hash = blockchain.last_block().get_hash()
    new_block2 = Block(transactions=[new_transaction], prev_hash=prev_hash)
    print("生成新的区块...")
    w2 = ProofOfWork(new_block2, bob)
    block = w2.mine()
    print("将新区块添加到区块链中")
    blockchain.add_block(block)
else:
    print("交易验证失败！")


# 打印当前钱包情况
print("alice: %.1f个加密货币" % (get_balance(blockchain, alice)))
print("tom: %.1f个加密货币" % (get_balance(blockchain, tom)))
print("bob: %d个加密货币" % (get_balance(blockchain, bob)))


#打印当前区块链情况
print("blockchain contents:")
blockchain.print_list()