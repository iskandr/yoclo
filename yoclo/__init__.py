import inspect
import sys
from argparse import ArgumentParser


def parser_from_fn(fn):
    parser = ArgumentParser(fn.__name__)
    signature = inspect.signature(fn)
    for param_name, param in signature.parameters.items():
        param_name = "--" + param_name.replace("_", "-")
        t = param.annotation
        if t == inspect._empty:
            t = str
        if param.default == inspect._empty:
            parser.add_argument(param_name, type=t, required=True)
        else:
            parser.add_argument(param_name, type=t, required=False, default=param.default)
    return parser

def cli_args_to_kwargs(args):
    return {k.replace("-", "_"): v for k, v in vars(args).items()}

def run(entry_fn):
    parser = parser_from_fn(entry_fn)
    args = parser.parse_args(sys.argv[1:])
    return entry_fn(**cli_args_to_kwargs(args))

