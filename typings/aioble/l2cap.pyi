from typing import Any

def log_error(*args, **kwargs) -> Any: ...
def register_irq_handler(*args, **kwargs) -> Any: ...
def const(*args, **kwargs) -> Any: ...

class L2CAPChannel:
    def available(self, *args, **kwargs) -> Any: ...
    send: Any
    recvinto: Any
    flush: Any
    disconnect: Any
    def __init__(self, *argv, **kwargs) -> None: ...

class L2CAPDisconnectedError(Exception): ...
