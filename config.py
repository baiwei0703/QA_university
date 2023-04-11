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


if __name__ == '__main__':
    args = Args()
    print(args.seq_labels)
    print(args.seqlabel2id)
    print(args.tokenlabel2id)
    print(args.nerlabel2id)
