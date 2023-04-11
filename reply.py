from config import Args
import random


def classifier(msg):
    """
    传入消息，返回意图
    :param msg:
    :return:
    """
    intent = 'greet'
    slots = []
    return intent, slots


def gossip_robot(intent):
    """
    根据意图，返回随机回答
    :param intent:
    :return:
    """
    return random.choice(Args.gossip_corpus[intent])


def load_user_dialogue_context(user):
    """
    根据用户标识，获取用户上一轮对话的内容
    :param user: 用户标识
    :return: 上一轮用户的对话内容
    """
    return 'Hi'


def pro_bot(msg, user):
    answer = ''
    return answer


def intent_classifier(msg, user_id):
    user_intent, slot_list = classifier(msg)
    print(user_intent)
    if user_intent in Args.gossip_corpus.keys():
        reply = gossip_robot(user_intent)
    elif user_intent == "accept":
        pre_context = load_user_dialogue_context(user_id)
        # 根据前一轮的问题进行回答
        reply = "回答上一轮的问题"
    else:
        # 使用专业机器人进行回答
        reply = pro_bot(msg, user_id)
    return reply


if __name__ == '__main__':
    while 1:
        user_input = input("用户输入：")
        print(intent_classifier(user_input, '1'))
