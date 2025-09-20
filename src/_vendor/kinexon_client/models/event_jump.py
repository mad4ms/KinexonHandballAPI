from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.event_jump_jump_category import EventJumpJumpCategory
from ..types import UNSET, Unset

T = TypeVar("T", bound="EventJump")


@_attrs_define
class EventJump:
    """
    Attributes:
        timestamp (Union[Unset, int]):
        timestamp_ms (Union[Unset, int]):
        timezone_id (Union[Unset, int]):
        game_clock (Union[Unset, str]):
        period (Union[Unset, str]):
        player_id (Union[Unset, int]):
        airtime (Union[Unset, float]):
        height (Union[Unset, float]):
        x (Union[Unset, float]):
        y (Union[Unset, float]):
        distance (Union[Unset, float]):
        jump_max_ratio (Union[Unset, float]):
        jump_category (Union[Unset, EventJumpJumpCategory]):
    """

    timestamp: Union[Unset, int] = UNSET
    timestamp_ms: Union[Unset, int] = UNSET
    timezone_id: Union[Unset, int] = UNSET
    game_clock: Union[Unset, str] = UNSET
    period: Union[Unset, str] = UNSET
    player_id: Union[Unset, int] = UNSET
    airtime: Union[Unset, float] = UNSET
    height: Union[Unset, float] = UNSET
    x: Union[Unset, float] = UNSET
    y: Union[Unset, float] = UNSET
    distance: Union[Unset, float] = UNSET
    jump_max_ratio: Union[Unset, float] = UNSET
    jump_category: Union[Unset, EventJumpJumpCategory] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        timestamp = self.timestamp

        timestamp_ms = self.timestamp_ms

        timezone_id = self.timezone_id

        game_clock = self.game_clock

        period = self.period

        player_id = self.player_id

        airtime = self.airtime

        height = self.height

        x = self.x

        y = self.y

        distance = self.distance

        jump_max_ratio = self.jump_max_ratio

        jump_category: Union[Unset, str] = UNSET
        if not isinstance(self.jump_category, Unset):
            jump_category = self.jump_category.value

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if timestamp is not UNSET:
            field_dict["timestamp"] = timestamp
        if timestamp_ms is not UNSET:
            field_dict["timestamp_ms"] = timestamp_ms
        if timezone_id is not UNSET:
            field_dict["timezone_id"] = timezone_id
        if game_clock is not UNSET:
            field_dict["game_clock"] = game_clock
        if period is not UNSET:
            field_dict["period"] = period
        if player_id is not UNSET:
            field_dict["player_id"] = player_id
        if airtime is not UNSET:
            field_dict["airtime"] = airtime
        if height is not UNSET:
            field_dict["height"] = height
        if x is not UNSET:
            field_dict["x"] = x
        if y is not UNSET:
            field_dict["y"] = y
        if distance is not UNSET:
            field_dict["distance"] = distance
        if jump_max_ratio is not UNSET:
            field_dict["jump_max_ratio"] = jump_max_ratio
        if jump_category is not UNSET:
            field_dict["jump_category"] = jump_category

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        timestamp = d.pop("timestamp", UNSET)

        timestamp_ms = d.pop("timestamp_ms", UNSET)

        timezone_id = d.pop("timezone_id", UNSET)

        game_clock = d.pop("game_clock", UNSET)

        period = d.pop("period", UNSET)

        player_id = d.pop("player_id", UNSET)

        airtime = d.pop("airtime", UNSET)

        height = d.pop("height", UNSET)

        x = d.pop("x", UNSET)

        y = d.pop("y", UNSET)

        distance = d.pop("distance", UNSET)

        jump_max_ratio = d.pop("jump_max_ratio", UNSET)

        _jump_category = d.pop("jump_category", UNSET)
        jump_category: Union[Unset, EventJumpJumpCategory]
        if isinstance(_jump_category, Unset):
            jump_category = UNSET
        else:
            jump_category = EventJumpJumpCategory(_jump_category)

        event_jump = cls(
            timestamp=timestamp,
            timestamp_ms=timestamp_ms,
            timezone_id=timezone_id,
            game_clock=game_clock,
            period=period,
            player_id=player_id,
            airtime=airtime,
            height=height,
            x=x,
            y=y,
            distance=distance,
            jump_max_ratio=jump_max_ratio,
            jump_category=jump_category,
        )

        event_jump.additional_properties = d
        return event_jump

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
