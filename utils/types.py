from typing import List
from pydantic import BaseModel


class Span(BaseModel):
    size: float
    flags: int
    font: str
    color: int
    ascender: float
    descender: float
    text: str
    origin: List[float]
    bbox: List[float]


class Line(BaseModel):
    spans: List[Span]
    wmode: int
    dir: List[float]
    bbox: List[float]


class Block(BaseModel):
    number: int
    type: int
    bbox: List[float]
    lines: List[Line]


class TextDict(BaseModel):
    width: float
    height: float
    blocks: List[Block]