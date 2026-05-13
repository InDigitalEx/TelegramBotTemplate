class SingletonMeta(type):
    """Metaclass implementing a simple singleton pattern.

    Any class using `metaclass=SingletonMeta` will be instantiated once.
    Subsequent calls return the same instance.

    Note: this implementation stores the instance on the metaclass itself,
    so it behaves as a process-wide singleton for all classes using it.
    """

    _instance = None

    def __call__(cls, *args, **kwargs):
        if cls._instance:
            return cls._instance
        cls._instance = super(SingletonMeta, cls).__call__(*args, **kwargs)
        return cls._instance

