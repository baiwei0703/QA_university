# -*- coding:utf-8 -*-
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


def pro_bot(intent, slots, user):
    answer = ''
    return answer
