from typing import (
    Optional,
    Tuple,
    Sequence,
    overload,
    Union,
    Callable,
    List,
    Iterator,
)

from pygame._common import RectValue
from typing_extensions import Literal as Literal
from typing_extensions import Protocol

from pygame.math import Vector2, Vector3
from pygame.rect import Rect

Coordinate = Union[Tuple[float, float], Sequence[float], Vector2, Tuple[int, int]]

Shape = Union["Line", "Circle", "Rect", "Polygon"]

_CanBeLine = Union[
    Rect,
    Line,
    Tuple[float, float, float, float],
    Tuple[Coordinate, Coordinate],
    Sequence[float],
    Sequence[Coordinate],
]

class _HasLineAttribute(Protocol):
    # An object that has a line attribute that is either a line, or a function
    # that returns a line confirms to the rect protocol
    line: Union[LineValue, Callable[[], LineValue]]

LineValue = Union[_CanBeLine, _HasLineAttribute]

_CanBeCircle = Union[Vector3, Circle, Tuple[float, float, float], Sequence[float]]
_CanBeCollided = Union[Circle, Rect, Line, Sequence[int, int]]

class _HasCirclettribute(Protocol):
    # An object that has a circle attribute that is either a circle, or a function
    # that returns a circle
    circle: Union[CircleValue, Callable[[], CircleValue]]

CircleValue = Union[_CanBeCircle, _HasCirclettribute]

class Line(Sequence[float]):
    x1: float
    y1: float
    x2: float
    y2: float
    a: Tuple[float, float]
    b: Tuple[float, float]
    length: float
    midpoint: Tuple[float, float]
    midpoint_x: float
    midpoint_y: float
    slope: float
    __safe_for_unpickling__: Literal[True]
    __hash__: None  # type: ignore

    @overload
    def __init__(self, line: Line) -> None: ...
    @overload
    def __init__(self, x1: float, y1: float, x2: float, y2: float) -> None: ...
    @overload
    def __init__(self, first: Sequence[float], second: Sequence[float]) -> None: ...
    @overload
    def __init__(self, single_arg: LineValue) -> None: ...
    def __len__(self) -> Literal[4]: ...
    def __iter__(self) -> Iterator[float]: ...
    @overload
    def __getitem__(self, i: int) -> float: ...
    @overload
    def __getitem__(self, s: slice) -> List[float]: ...
    @overload
    def __setitem__(self, key: int, value: float) -> None: ...
    @overload
    def __setitem__(self, key: slice, value: Union[float, Line]) -> None: ...
    def __copy__(self) -> Line: ...

    copy = __copy__

    @overload
    def update(self, x1: float, y1: float, x2: float, y2: float) -> None: ...
    @overload
    def update(self, a: Coordinate, b: Coordinate) -> None: ...
    @overload
    def update(self, single_arg: LineValue) -> None: ...
    def collideswith(self, other: _CanBeCollided) -> bool: ...
    @overload
    def collidepoint(self, x: float, y: float) -> bool: ...
    @overload
    def collidepoint(self, x_y: Coordinate) -> bool: ...
    @overload
    def collideline(self, line: Line) -> bool: ...
    @overload
    def collideline(self, x1: float, y1: float, x2: float, y2: float) -> bool: ...
    @overload
    def collideline(self, first: Sequence[float], second: Sequence[float]) -> bool: ...
    def colliderect(self, rect: RectValue) -> bool: ...
    @overload
    def colliderect(self, left_top: Coordinate, width_height: Coordinate) -> bool: ...
    @overload
    def colliderect(
        self, left: float, top: float, width: float, height: float
    ) -> bool: ...
    @overload
    def collidecircle(self, circle: CircleValue) -> bool: ...
    @overload
    def collidecircle(self, x: float, y: float, r: float) -> bool: ...
    def collidepolygon(self, polygon: Polygon, only_edges: bool = False) -> bool: ...
    def as_circle(self) -> Circle: ...
    def as_rect(self) -> Rect: ...
    @overload
    def move(self, x: float, y: float) -> Line: ...
    @overload
    def move(self, move_by: Coordinate) -> Line: ...
    @overload
    def move_ip(self, x: float, y: float) -> None: ...
    @overload
    def move_ip(self, move_by: Coordinate) -> None: ...
    def at(self, weight: float) -> Tuple[float, float]: ...
    @overload
    def scale(self, factor: float, origin: float) -> Line: ...
    @overload
    def scale_ip(self, factor: float, origin: float) -> None: ...
    @overload
    def scale(self, factor_and_origin: Sequence[float, float]) -> Line: ...
    @overload
    def scale_ip(self, factor_and_origin: Sequence[float, float]) -> None: ...
    def flip(self) -> Line: ...
    def flip_ip(self) -> None: ...
    def is_parallel(self, line: LineValue) -> bool: ...
    def is_perpendicular(self, line: LineValue) -> bool: ...

class Circle:
    x: float
    y: float
    r: float
    r_sqr: float
    d: float
    diameter: float
    area: float
    circumference: float
    center: Tuple[float, float]
    __safe_for_unpickling__: Literal[True]
    __hash__: None  # type: ignore

    @overload
    def __init__(self, x: float, y: float, r: float) -> None: ...
    @overload
    def __init__(self, pos: Sequence[float], r: float) -> None: ...
    @overload
    def __init__(self, circle: CircleValue) -> None: ...
    @overload
    def __init__(self, single_arg: CircleValue) -> None: ...
    @overload
    def collidecircle(self, circle: CircleValue) -> bool: ...
    @overload
    def collidecircle(self, x: float, y: float, r: float) -> bool: ...
    @overload
    def collideline(self, line: LineValue) -> bool: ...
    @overload
    def collideline(self, x1: float, y1: float, x2: float, y2: float) -> bool: ...
    @overload
    def collidepoint(self, x: float, y: float) -> bool: ...
    @overload
    def collidepoint(self, point: Coordinate) -> bool: ...
    @overload
    def colliderect(self, rect: Rect) -> bool: ...
    @overload
    def colliderect(self, x: int, y: int, w: int, h: int) -> bool: ...
    def collideswith(self, other: _CanBeCollided) -> bool: ...
    def __copy__(self) -> Circle: ...

    copy = __copy__

    def as_rect(self) -> Rect: ...
    @overload
    def update(self, circle: CircleValue) -> None: ...
    @overload
    def update(self, x: float, y: float, r: float) -> None: ...
    @overload
    def move(self, x: float, y: float) -> Circle: ...
    @overload
    def move(self, move_by: Coordinate) -> Circle: ...
    @overload
    def move_ip(self, x: float, y: float) -> None: ...
    @overload
    def move_ip(self, move_by: Coordinate) -> None: ...
    def contains(self, shape: Shape) -> bool: ...

class Polygon:
    vertices: List[Coordinate]
    verts_num: int
    perimeter: float
    c_x: float
    c_y: float
    center: Tuple[float, float]
    __safe_for_unpickling__: Literal[True]
    __hash__: None  # type: ignore

    @overload
    def __init__(self, vertices: Sequence[Coordinate]) -> None: ...
    @overload
    def __setitem__(self, key: int, value: Coordinate) -> None: ...
    @overload
    def __getitem__(self, i: int) -> Sequence[Coordinate]: ...
    @overload
    def __init__(self, *args) -> None: ...
    @overload
    def __init__(self, polygon: Polygon) -> None: ...
    def __copy__(self) -> Polygon: ...

    copy = __copy__

    def rotate(self, angle: float) -> Polygon: ...
    def rotate_ip(self, angle: float) -> None: ...
    @overload
    def move(self, x: float, y: float) -> Polygon: ...
    @overload
    def move(self, move_by: Coordinate) -> Polygon: ...
    @overload
    def as_segments(self) -> List[Line]: ...
    @overload
    def move_ip(self, x: float, y: float) -> None: ...
    @overload
    def move_ip(self, move_by: Coordinate) -> None: ...
    def collidepoint(self, x: float, y: float) -> bool: ...
    @overload
    def collidepoint(self, point: Coordinate) -> bool: ...
    def collideline(self, line: LineValue, only_edges: bool = False) -> bool: ...
    def get_bounding_box(self) -> Rect: ...
    def is_convex() -> bool: ...
    def insert_vertex(self, index: int, vertex: Coordinate) -> None: ...
    def remove_vertex(self, index: int) -> None: ...
    def pop_vertex(self, index: int) -> Coordinate: ...

def regular_polygon(
    sides: int, center: Coordinate, radius: float, angle: float = 0
) -> Polygon: ...
@overload
def raycast(
    origin: Coordinate,
    direction: Coordinate,
    max_dist: float,
    colliders: Sequence[Union[Rect, Circle, Line]],
) -> Optional[Tuple[float, float]]: ...
@overload
def raycast(
    origin: Coordinate,
    angle: float,
    max_dist: float,
    colliders: Sequence[Union[Rect, Circle, Line]],
) -> Optional[Tuple[float, float]]: ...

Ray = Union[
    Line,
    Tuple[Coordinate, Coordinate, float],
    Tuple[Coordinate, float, float],
    Tuple[Coordinate, Coordinate],
]

@overload
def raycast(
    line: Line,
    colliders: Sequence[Union[Rect, Circle, Line]],
) -> Optional[Tuple[float, float]]: ...
@overload
def multiraycast(
    rays: Sequence[Ray],
    colliders: Sequence[Union[Rect, Circle, Line]],
) -> Sequence[Optional[Tuple[float, float]]]: ...
def rect_to_polygon(rect: Rect) -> Polygon: ...
def is_line(obj) -> bool: ...
def is_circle(obj) -> bool: ...
def is_polygon(obj) -> bool: ...
