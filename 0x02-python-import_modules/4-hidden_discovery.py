#!/usr/bin/python3
if __name__ == '__main__':
    import importlib.util
    import importlib.machinery

    bytecode_path = './hidden_4.pyc'
    loader = importlib.machinery.SourceFileLoader('hidden_4', bytecode_path)
    spec = importlib.util.spec_from_loader('hidden_4', loader)
    module = importlib.util.module_from_spec(spec)

    spec.loader.exec_module(module)
