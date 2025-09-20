from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="EventDownOnPads")


@_attrs_define
class EventDownOnPads:
    """
    Attributes:
        timestamp (Union[Unset, int]):
        timestamp_ms (Union[Unset, int]):
        timezone_id (Union[Unset, int]):
        game_clock (Union[Unset, str]):
        period (Union[Unset, str]):
        player_id (Union[Unset, int]):
        group_id (Union[Unset, int]):
        impact_peak (Union[Unset, float]):
        time_to_on_pads (Union[Unset, float]):
        trajectory (Union[Unset, str]):
    """

    timestamp: Union[Unset, int] = UNSET
    timestamp_ms: Union[Unset, int] = UNSET
    timezone_id: Union[Unset, int] = UNSET
    game_clock: Union[Unset, str] = UNSET
    period: Union[Unset, str] = UNSET
    player_id: Union[Unset, int] = UNSET
    group_id: Union[Unset, int] = UNSET
    impact_peak: Union[Unset, float] = UNSET
    time_to_on_pads: Union[Unset, float] = UNSET
    trajectory: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        timestamp = self.timestamp

        timestamp_ms = self.timestamp_ms

        timezone_id = self.timezone_id

        game_clock = self.game_clock

        period = self.period

        player_id = self.player_id

        group_id = self.group_id

        impact_peak = self.impact_peak

        time_to_on_pads = self.time_to_on_pads

        trajectory = self.trajectory

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
        if group_id is not UNSET:
            field_dict["group_id"] = group_id
        if impact_peak is not UNSET:
            field_dict["impact_peak"] = impact_peak
        if time_to_on_pads is not UNSET:
            field_dict["time_to_on_pads"] = time_to_on_pads
        if trajectory is not UNSET:
            field_dict["trajectory"] = trajectory

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

        group_id = d.pop("group_id", UNSET)

        impact_peak = d.pop("impact_peak", UNSET)

        time_to_on_pads = d.pop("time_to_on_pads", UNSET)

        trajectory = d.pop("trajectory", UNSET)

        event_down_on_pads = cls(
            timestamp=timestamp,
            timestamp_ms=timestamp_ms,
            timezone_id=timezone_id,
            game_clock=game_clock,
            period=period,
            player_id=player_id,
            group_id=group_id,
            impact_peak=impact_peak,
            time_to_on_pads=time_to_on_pads,
            trajectory=trajectory,
        )

        event_down_on_pads.additional_properties = d
        return event_down_on_pads

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
