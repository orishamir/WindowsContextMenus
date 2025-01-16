from dataclasses import dataclass

from src.comparers.icomparer import IComparer


@dataclass
class DosWildcard(IComparer):
    """
    Works like DOS-style wildcard characters:
        ? matches one arbitrary character.
        * matches zero or more arbitrary characters.
    Example:
        "Mic?osoft W*d" - Finds files where the file name starts with "Mic", followed by some character,
                          followed by "osoft w", followed by any characters ending with d.
    """
    string: str

    def to_aqs_string(self) -> str:
        return f":~{self.string}"
