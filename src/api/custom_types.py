from pydantic import ByteSize


class StrByteSize(ByteSize):
    def __str__(self) -> str:
        return self.human_readable(decimal=True)
