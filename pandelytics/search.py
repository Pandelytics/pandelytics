from importlib import import_module


def search(engine, type_="News"):
    """ Returns results """

    module = f"pandelytics.engines.{engine.lower()}"
    try:
        mod = import_module(module)
    except (ImportError, ModuleNotFoundError):
        print(Exception(
            f"Engine <{module}> does not exists"))
        return

    try:
        engine_class = getattr(mod, type_)
    except AttributeError:
        print(Exception(
            f"Engine <{module}> does not implement {type_}"))
        return

    engine = engine_class()
    return engine.response()
