import torch


def set_seed(seed):
    torch.manual_seed(seed)

    if torch.cuda.is_available():
        torch.cuda.manual_seed(seed)
        torch.cuda.manual_seed_all(seed)

        # что бы все операции на GPU были детерменированными
        torch.backends.cudnn.deterministic = True
        torch.backends.cudnn.benchmark = False