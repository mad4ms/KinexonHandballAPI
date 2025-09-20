from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="EventBallPossession")


@_attrs_define
class EventBallPossession:
    """
    Attributes:
        timestamp (Union[Unset, int]):
        timestamp_ms (Union[Unset, int]):
        timezone_id (Union[Unset, int]):
        game_clock (Union[Unset, str]):
        period (Union[Unset, str]):
        player_id (Union[Unset, int]):
        duration (Union[Unset, float]):
        trajectory (Union[Unset, str]):
        number_of_contacts (Union[Unset, float]):
        verticality (Union[Unset, float]):
        horizontality (Union[Unset, float]):
        pressure_index_max (Union[Unset, float]):
        pressure_index_min (Union[Unset, float]):
        pressure_index_avg (Union[Unset, float]):
    """

    timestamp: Union[Unset, int] = UNSET
    timestamp_ms: Union[Unset, int] = UNSET
    timezone_id: Union[Unset, int] = UNSET
    game_clock: Union[Unset, str] = UNSET
    period: Union[Unset, str] = UNSET
    player_id: Union[Unset, int] = UNSET
    duration: Union[Unset, float] = UNSET
    trajectory: Union[Unset, str] = UNSET
    number_of_contacts: Union[Unset, float] = UNSET
    verticality: Union[Unset, float] = UNSET
    horizontality: Union[Unset, float] = UNSET
    pressure_index_max: Union[Unset, float] = UNSET
    pressure_index_min: Union[Unset, float] = UNSET
    pressure_index_avg: Union[Unset, float] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        timestamp = self.timestamp

        timestamp_ms = self.timestamp_ms

        timezone_id = self.timezone_id

        game_clock = self.game_clock

        period = self.period

        player_id = self.player_id

        duration = self.duration

        trajectory = self.trajectory

        number_of_contacts = self.number_of_contacts

        verticality = self.verticality

        horizontality = self.horizontality

        pressure_index_max = self.pressure_index_max

        pressure_index_min = self.pressure_index_min

        pressure_index_avg = self.pressure_index_avg

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
        if duration is not UNSET:
            field_dict["duration"] = duration
        if trajectory is not UNSET:
            field_dict["trajectory"] = trajectory
        if number_of_contacts is not UNSET:
            field_dict["number_of_contacts"] = number_of_contacts
        if verticality is not UNSET:
            field_dict["verticality"] = verticality
        if horizontality is not UNSET:
            field_dict["horizontality"] = horizontality
        if pressure_index_max is not UNSET:
            field_dict["pressure_index_max"] = pressure_index_max
        if pressure_index_min is not UNSET:
            field_dict["pressure_index_min"] = pressure_index_min
        if pressure_index_avg is not UNSET:
            field_dict["pressure_index_avg"] = pressure_index_avg

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

        duration = d.pop("duration", UNSET)

        trajectory = d.pop("trajectory", UNSET)

        number_of_contacts = d.pop("number_of_contacts", UNSET)

        verticality = d.pop("verticality", UNSET)

        horizontality = d.pop("horizontality", UNSET)

        pressure_index_max = d.pop("pressure_index_max", UNSET)

        pressure_index_min = d.pop("pressure_index_min", UNSET)

        pressure_index_avg = d.pop("pressure_index_avg", UNSET)

        event_ball_possession = cls(
            timestamp=timestamp,
            timestamp_ms=timestamp_ms,
            timezone_id=timezone_id,
            game_clock=game_clock,
            period=period,
            player_id=player_id,
            duration=duration,
            trajectory=trajectory,
            number_of_contacts=number_of_contacts,
            verticality=verticality,
            horizontality=horizontality,
            pressure_index_max=pressure_index_max,
            pressure_index_min=pressure_index_min,
            pressure_index_avg=pressure_index_avg,
        )

        event_ball_possession.additional_properties = d
        return event_ball_possession

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
