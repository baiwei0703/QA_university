from torch.utils.data import DataLoader, Dataset
from config import Args
from preprocess import Processor, get_features
from transformers import BertTokenizer


class BertDataset(Dataset):
    def __init__(self, features):
        self.features = features
        self.nums = len(self.features)

    def __len__(self):
        return self.nums

    def __getitem__(self, item):
        data = {
            'input_ids': self.features[item].input_ids.long(),
            'attention_mask': self.features[item].attention_mask.long(),
            'token_type_ids': self.features[item].token_type_ids.long(),
            'seq_label_ids': self.features[item].seq_label_ids.long(),
            'token_label_ids': self.features[item].token_label_ids.long(),
        }
        return data


if __name__ == '__main__':
    args = Args()
    tokenizer = BertTokenizer.from_pretrained(args.bert_dir)
    raw_examples = Processor.get_examples(args.train_path, 'train')
    train_features = get_features(raw_examples, tokenizer, args)
    train_dataset = BertDataset(train_features)
    train_loader = DataLoader(train_dataset, batch_size=args.batchsize, shuffle=True)

    for step, train_batch in enumerate(train_loader):
        print(train_batch)
        break

    raw_examples = Processor.get_examples(args.test_path, 'test')
    test_features = get_features(raw_examples, tokenizer, args)
    test_dataset = BertDataset(test_features)
    test_loader = DataLoader(test_dataset, batch_size=args.batchsize, shuffle=True)
