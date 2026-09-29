from typing import Callable, Optional

_session_provider : Optional[Callable] = None

def set_session_provider(provider: Callable) -> None:
    global _session_provider

    _session_provider = provider

async def get_session():
    if _session_provider is None:
        RuntimeError(
            "Session have not been set up yet."
            "You can set your session via set_session_provider function!"
        )

    async for session in _session_provider():
        yield session