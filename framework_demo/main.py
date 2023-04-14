# -*- coding:utf-8 -*-
from moudels import classifier, gossip_robot, pro_bot, load_user_dialogue_context
from config import Args


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
        reply = pro_bot(user_intent, slot_list, user_id)
    return reply


if __name__ == '__main__':
    while 1:
        user_input = input("用户输入：")
        print(intent_classifier(user_input, '1'))
