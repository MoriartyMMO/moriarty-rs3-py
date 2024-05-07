from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ._log import log as clog
else:
    from cockbot5.core import log as clog


def log(message: str) -> None:
    """
    Logs a message to the game's developer console.
    You can access this console by pressing alt + back-tick in-game.

    :return: None
    """
    clog(f"<img=12><col=fc9635>[Moriarty]</col> {message}")
