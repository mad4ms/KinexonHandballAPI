from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.event_dfl_cross_dfl_cross_category import EventDflCrossDflCrossCategory
from ..types import UNSET, Unset

T = TypeVar("T", bound="EventDflCross")


@_attrs_define
class EventDflCross:
    """
    Attributes:
        timestamp (Union[Unset, int]):
        timestamp_ms (Union[Unset, int]):
        timezone_id (Union[Unset, int]):
        game_clock (Union[Unset, str]):
        period (Union[Unset, str]):
        player_id (Union[Unset, int]):
        receiving_player (Union[Unset, float]):
        height (Union[Unset, float]):
        distance (Union[Unset, float]):
        dfl_from_open_play (Union[Unset, float]):
        dfl_penalty_box (Union[Unset, float]):
        dfl_play_origin (Union[Unset, float]):
        dfl_semi_field (Union[Unset, float]):
        dfl_flat_cross (Union[Unset, float]):
        dfl_rotation (Union[Unset, float]):
        side (Union[Unset, float]):
        dfl_goalkeeper_interference (Union[Unset, float]):
        dfl_goalkeeper (Union[Unset, float]):
        trajectory (Union[Unset, str]):
        dfl_cross_category (Union[Unset, EventDflCrossDflCrossCategory]):
    """

    timestamp: Union[Unset, int] = UNSET
    timestamp_ms: Union[Unset, int] = UNSET
    timezone_id: Union[Unset, int] = UNSET
    game_clock: Union[Unset, str] = UNSET
    period: Union[Unset, str] = UNSET
    player_id: Union[Unset, int] = UNSET
    receiving_player: Union[Unset, float] = UNSET
    height: Union[Unset, float] = UNSET
    distance: Union[Unset, float] = UNSET
    dfl_from_open_play: Union[Unset, float] = UNSET
    dfl_penalty_box: Union[Unset, float] = UNSET
    dfl_play_origin: Union[Unset, float] = UNSET
    dfl_semi_field: Union[Unset, float] = UNSET
    dfl_flat_cross: Union[Unset, float] = UNSET
    dfl_rotation: Union[Unset, float] = UNSET
    side: Union[Unset, float] = UNSET
    dfl_goalkeeper_interference: Union[Unset, float] = UNSET
    dfl_goalkeeper: Union[Unset, float] = UNSET
    trajectory: Union[Unset, str] = UNSET
    dfl_cross_category: Union[Unset, EventDflCrossDflCrossCategory] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        timestamp = self.timestamp

        timestamp_ms = self.timestamp_ms

        timezone_id = self.timezone_id

        game_clock = self.game_clock

        period = self.period

        player_id = self.player_id

        receiving_player = self.receiving_player

        height = self.height

        distance = self.distance

        dfl_from_open_play = self.dfl_from_open_play

        dfl_penalty_box = self.dfl_penalty_box

        dfl_play_origin = self.dfl_play_origin

        dfl_semi_field = self.dfl_semi_field

        dfl_flat_cross = self.dfl_flat_cross

        dfl_rotation = self.dfl_rotation

        side = self.side

        dfl_goalkeeper_interference = self.dfl_goalkeeper_interference

        dfl_goalkeeper = self.dfl_goalkeeper

        trajectory = self.trajectory

        dfl_cross_category: Union[Unset, str] = UNSET
        if not isinstance(self.dfl_cross_category, Unset):
            dfl_cross_category = self.dfl_cross_category.value

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
        if receiving_player is not UNSET:
            field_dict["receiving_player"] = receiving_player
        if height is not UNSET:
            field_dict["height"] = height
        if distance is not UNSET:
            field_dict["distance"] = distance
        if dfl_from_open_play is not UNSET:
            field_dict["dfl_from_open_play"] = dfl_from_open_play
        if dfl_penalty_box is not UNSET:
            field_dict["dfl_penalty_box"] = dfl_penalty_box
        if dfl_play_origin is not UNSET:
            field_dict["dfl_play_origin"] = dfl_play_origin
        if dfl_semi_field is not UNSET:
            field_dict["dfl_semi_field"] = dfl_semi_field
        if dfl_flat_cross is not UNSET:
            field_dict["dfl_flat_cross"] = dfl_flat_cross
        if dfl_rotation is not UNSET:
            field_dict["dfl_rotation"] = dfl_rotation
        if side is not UNSET:
            field_dict["side"] = side
        if dfl_goalkeeper_interference is not UNSET:
            field_dict["dfl_goalkeeper_interference"] = dfl_goalkeeper_interference
        if dfl_goalkeeper is not UNSET:
            field_dict["dfl_goalkeeper"] = dfl_goalkeeper
        if trajectory is not UNSET:
            field_dict["trajectory"] = trajectory
        if dfl_cross_category is not UNSET:
            field_dict["dfl_cross_category"] = dfl_cross_category

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

        receiving_player = d.pop("receiving_player", UNSET)

        height = d.pop("height", UNSET)

        distance = d.pop("distance", UNSET)

        dfl_from_open_play = d.pop("dfl_from_open_play", UNSET)

        dfl_penalty_box = d.pop("dfl_penalty_box", UNSET)

        dfl_play_origin = d.pop("dfl_play_origin", UNSET)

        dfl_semi_field = d.pop("dfl_semi_field", UNSET)

        dfl_flat_cross = d.pop("dfl_flat_cross", UNSET)

        dfl_rotation = d.pop("dfl_rotation", UNSET)

        side = d.pop("side", UNSET)

        dfl_goalkeeper_interference = d.pop("dfl_goalkeeper_interference", UNSET)

        dfl_goalkeeper = d.pop("dfl_goalkeeper", UNSET)

        trajectory = d.pop("trajectory", UNSET)

        _dfl_cross_category = d.pop("dfl_cross_category", UNSET)
        dfl_cross_category: Union[Unset, EventDflCrossDflCrossCategory]
        if isinstance(_dfl_cross_category, Unset):
            dfl_cross_category = UNSET
        else:
            dfl_cross_category = EventDflCrossDflCrossCategory(_dfl_cross_category)

        event_dfl_cross = cls(
            timestamp=timestamp,
            timestamp_ms=timestamp_ms,
            timezone_id=timezone_id,
            game_clock=game_clock,
            period=period,
            player_id=player_id,
            receiving_player=receiving_player,
            height=height,
            distance=distance,
            dfl_from_open_play=dfl_from_open_play,
            dfl_penalty_box=dfl_penalty_box,
            dfl_play_origin=dfl_play_origin,
            dfl_semi_field=dfl_semi_field,
            dfl_flat_cross=dfl_flat_cross,
            dfl_rotation=dfl_rotation,
            side=side,
            dfl_goalkeeper_interference=dfl_goalkeeper_interference,
            dfl_goalkeeper=dfl_goalkeeper,
            trajectory=trajectory,
            dfl_cross_category=dfl_cross_category,
        )

        event_dfl_cross.additional_properties = d
        return event_dfl_cross

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
