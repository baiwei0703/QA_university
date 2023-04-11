# -*- coding:utf-8 -*-
from transformers import AutoTokenizer, AutoModelForMaskedLM

if __name__ == '__main__':
    tokenizer = AutoTokenizer.from_pretrained("hfl/chinese-bert-wwm-ext")

    model = AutoModelForMaskedLM.from_pretrained("hfl/chinese-bert-wwm-ext")

