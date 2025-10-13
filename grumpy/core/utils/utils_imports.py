from importlib import import_module


def get_attr_from_path(path):
    package, attr = path.rsplit(".", 1)
    return getattr(import_module(package), attr)
