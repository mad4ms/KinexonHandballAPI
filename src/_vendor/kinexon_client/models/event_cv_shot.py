from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.event_cv_shot_shot_load_category import EventCvShotShotLoadCategory
from ..types import UNSET, Unset

T = TypeVar("T", bound="EventCvShot")


@_attrs_define
class EventCvShot:
    """
    Attributes:
        timestamp (Union[Unset, int]):
        timestamp_ms (Union[Unset, int]):
        timezone_id (Union[Unset, int]):
        game_clock (Union[Unset, str]):
        period (Union[Unset, str]):
        player_id (Union[Unset, int]):
        x (Union[Unset, float]):
        y (Union[Unset, float]):
        distance (Union[Unset, float]):
        made (Union[Unset, float]):
        shot_load (Union[Unset, float]):
        acceleration_max (Union[Unset, float]):
        deceleration_max (Union[Unset, float]):
        speed_max (Union[Unset, float]):
        jump_height (Union[Unset, float]):
        shot_load_category (Union[Unset, EventCvShotShotLoadCategory]):
    """

    timestamp: Union[Unset, int] = UNSET
    timestamp_ms: Union[Unset, int] = UNSET
    timezone_id: Union[Unset, int] = UNSET
    game_clock: Union[Unset, str] = UNSET
    period: Union[Unset, str] = UNSET
    player_id: Union[Unset, int] = UNSET
    x: Union[Unset, float] = UNSET
    y: Union[Unset, float] = UNSET
    distance: Union[Unset, float] = UNSET
    made: Union[Unset, float] = UNSET
    shot_load: Union[Unset, float] = UNSET
    acceleration_max: Union[Unset, float] = UNSET
    deceleration_max: Union[Unset, float] = UNSET
    speed_max: Union[Unset, float] = UNSET
    jump_height: Union[Unset, float] = UNSET
    shot_load_category: Union[Unset, EventCvShotShotLoadCategory] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        timestamp = self.timestamp

        timestamp_ms = self.timestamp_ms

        timezone_id = self.timezone_id

        game_clock = self.game_clock

        period = self.period

        player_id = self.player_id

        x = self.x

        y = self.y

        distance = self.distance

        made = self.made

        shot_load = self.shot_load

        acceleration_max = self.acceleration_max

        deceleration_max = self.deceleration_max

        speed_max = self.speed_max

        jump_height = self.jump_height

        shot_load_category: Union[Unset, str] = UNSET
        if not isinstance(self.shot_load_category, Unset):
            shot_load_category = self.shot_load_category.value

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
        if x is not UNSET:
            field_dict["x"] = x
        if y is not UNSET:
            field_dict["y"] = y
        if distance is not UNSET:
            field_dict["distance"] = distance
        if made is not UNSET:
            field_dict["made"] = made
        if shot_load is not UNSET:
            field_dict["shot_load"] = shot_load
        if acceleration_max is not UNSET:
            field_dict["acceleration_max"] = acceleration_max
        if deceleration_max is not UNSET:
            field_dict["deceleration_max"] = deceleration_max
        if speed_max is not UNSET:
            field_dict["speed_max"] = speed_max
        if jump_height is not UNSET:
            field_dict["jump_height"] = jump_height
        if shot_load_category is not UNSET:
            field_dict["shot_load_category"] = shot_load_category

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

        x = d.pop("x", UNSET)

        y = d.pop("y", UNSET)

        distance = d.pop("distance", UNSET)

        made = d.pop("made", UNSET)

        shot_load = d.pop("shot_load", UNSET)

        acceleration_max = d.pop("acceleration_max", UNSET)

        deceleration_max = d.pop("deceleration_max", UNSET)

        speed_max = d.pop("speed_max", UNSET)

        jump_height = d.pop("jump_height", UNSET)

        _shot_load_category = d.pop("shot_load_category", UNSET)
        shot_load_category: Union[Unset, EventCvShotShotLoadCategory]
        if isinstance(_shot_load_category, Unset):
            shot_load_category = UNSET
        else:
            shot_load_category = EventCvShotShotLoadCategory(_shot_load_category)

        event_cv_shot = cls(
            timestamp=timestamp,
            timestamp_ms=timestamp_ms,
            timezone_id=timezone_id,
            game_clock=game_clock,
            period=period,
            player_id=player_id,
            x=x,
            y=y,
            distance=distance,
            made=made,
            shot_load=shot_load,
            acceleration_max=acceleration_max,
            deceleration_max=deceleration_max,
            speed_max=speed_max,
            jump_height=jump_height,
            shot_load_category=shot_load_category,
        )

        event_cv_shot.additional_properties = d
        return event_cv_shot

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
