class Args:
    train_path = './data_test/train_process.json'
    test_path = './data_test/test_process.json'
    seq_labels_path = './data_test/intents.txt'
    token_labels_path = './data_test/slots.txt'
    bert_dir = './baseBert'
    save_dir = './checkpoints/'
    load_dir = f'./checkpoints/model.pt'
    do_train = False
    do_eval = True
    do_test = False
    do_save = False
    do_predict = True
    load_model = True
    device = None

    seqlabel2id = {}
    id2seqlabel = {}
    with open(seq_labels_path, 'r') as fp:
        seq_labels = fp.read().split('\n')
        for i, label in enumerate(seq_labels):
            seqlabel2id[label] = i
            id2seqlabel[i] = label

    tokenlabel2id = {}
    id2tokenlabel = {}
    with open(token_labels_path, 'r') as fp:
        token_labels = fp.read().split('\n')
        for i, label in enumerate(token_labels):
            tokenlabel2id[label] = i
            id2tokenlabel[i] = label

    tmp = ['O']
    for label in token_labels:
        B_label = 'B-' + label
        I_label = 'I-' + label
        tmp.append(B_label)
        tmp.append(I_label)

    nerlabel2id = {}
    id2nerlabel = {}
    for i, label in enumerate(tmp):
        nerlabel2id[label] = i
        id2nerlabel[i] = label

    hidden_size = 768
    seq_num_labels = len(seq_labels)
    token_num_labels = len(tmp)
    max_len = 128
    batchsize = 64
    lr = 2e-5
    epoch = 10
    hidden_dropout_prob = 0.1

    gossip_corpus = {
        'CHAT_GREETING': [
            '你好呀',
            'Hi~~',
            '好呀~',
            'Hello~'
        ],
        'CHAT_BYEBYE': [
            '再见，欢迎再次找我~',
            '古德拜~',
            'Bye~Bye~'
        ],
        'CHAT_THANK': [
            '不客气，这是我应该做的',
            '甭客气~',
            '这是我的荣幸'
        ],
        'UNKNOWN': [
            '请换个问题或者问法吧。。我还没学会介个。。。',
            '矮油，这个我还真不一定知道啊。问问老白吧~'
        ],
        'USELESS': [
            '或许我们可以聊点更有用的。',
            '掐指一算，这句话没多少用啊~'
        ]
    }

    semantic_slot = {
        # 学校基本信息
        "UNIVERSITY_INFO": {
            "slot_list": ["UNIVERSITY"],
            "slot_values": None,
            "cql_template": "MATCH(p:学校) WHERE p.name='{UNIVERSITY}' RETURN p.desc",
            "reply_template": "'{UNIVERSITY}' 的基本情况如下：\n",
            "ask_template": "您问的是 '{UNIVERSITY}' 的基本情况吗？",
            "intent_strategy": "",
            "deny_response": "很抱歉没有理解你的意思呢~"
        },
        # 学校入学要求
        "UNIVERSITY_REQ": {
            "slot_list": ["UNIVERSITY"],
            "slot_values": None,
            "cql_template": "MATCH(p:学校) WHERE p.name='{UNIVERSITY}' RETURN p.require",
            "reply_template": "'{UNIVERSITY}' 的基本要求如下：\n",
            "ask_template": "您问的是 '{UNIVERSITY}' 的入学要求吗？",
            "intent_strategy": "",
            "deny_response": "您说的我有点不明白，您可以换个问法问我哦~"
        },
        # 学校花费
        "UNIVERSITY_COST": {
            "slot_list": ["UNIVERSITY"],
            "slot_values": None,
            "cql_template": "MATCH(p:学校) WHERE p.name='{UNIVERSITY}' RETURN p.cost",
            "reply_template": "'{UNIVERSITY}' 的花费大致是：\n",
            "ask_template": "您问的是 '{UNIVERSITY}' 的入学花费吗？",
            "intent_strategy": "",
            "deny_response": "额~似乎有点不理解你说的是啥呢~"
        },
        # 专业信息
        "MAJOR_INFO": {
            "slot_list": ["MAJOR"],
            "slot_values": None,
            "cql_template": "MATCH(p:专业) WHERE p.name='{MAJOR}' RETURN p.desc",
            "reply_template": "'{MAJOR}' 的基本情况如下：\n",
            "ask_template": "您问的是 '{MAJOR}' 的基本情况吗？",
            "intent_strategy": "",
            "deny_response": "人类的语言太难了！！"
        }
    }


if __name__ == '__main__':
    args = Args()
    print(args.seq_labels)
    print(args.seqlabel2id)
    print(args.tokenlabel2id)
    print(args.nerlabel2id)
