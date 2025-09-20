from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="EventDetectedOffsideSoccer")


@_attrs_define
class EventDetectedOffsideSoccer:
    """
    Attributes:
        timestamp (Union[Unset, int]):
        timestamp_ms (Union[Unset, int]):
        timezone_id (Union[Unset, int]):
        game_clock (Union[Unset, str]):
        period (Union[Unset, str]):
        player_id (Union[Unset, int]):
        group_id (Union[Unset, int]):
        number_of_players_offside (Union[Unset, float]):
        receiving_player1 (Union[Unset, float]):
        offside_distance_player1 (Union[Unset, float]):
        receiving_player2 (Union[Unset, float]):
        offside_distance_player2 (Union[Unset, float]):
        receiving_player3 (Union[Unset, float]):
        offside_distance_player3 (Union[Unset, float]):
    """

    timestamp: Union[Unset, int] = UNSET
    timestamp_ms: Union[Unset, int] = UNSET
    timezone_id: Union[Unset, int] = UNSET
    game_clock: Union[Unset, str] = UNSET
    period: Union[Unset, str] = UNSET
    player_id: Union[Unset, int] = UNSET
    group_id: Union[Unset, int] = UNSET
    number_of_players_offside: Union[Unset, float] = UNSET
    receiving_player1: Union[Unset, float] = UNSET
    offside_distance_player1: Union[Unset, float] = UNSET
    receiving_player2: Union[Unset, float] = UNSET
    offside_distance_player2: Union[Unset, float] = UNSET
    receiving_player3: Union[Unset, float] = UNSET
    offside_distance_player3: Union[Unset, float] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        timestamp = self.timestamp

        timestamp_ms = self.timestamp_ms

        timezone_id = self.timezone_id

        game_clock = self.game_clock

        period = self.period

        player_id = self.player_id

        group_id = self.group_id

        number_of_players_offside = self.number_of_players_offside

        receiving_player1 = self.receiving_player1

        offside_distance_player1 = self.offside_distance_player1

        receiving_player2 = self.receiving_player2

        offside_distance_player2 = self.offside_distance_player2

        receiving_player3 = self.receiving_player3

        offside_distance_player3 = self.offside_distance_player3

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
        if number_of_players_offside is not UNSET:
            field_dict["number_of_players_offside"] = number_of_players_offside
        if receiving_player1 is not UNSET:
            field_dict["receiving_player1"] = receiving_player1
        if offside_distance_player1 is not UNSET:
            field_dict["offside_distance_player1"] = offside_distance_player1
        if receiving_player2 is not UNSET:
            field_dict["receiving_player2"] = receiving_player2
        if offside_distance_player2 is not UNSET:
            field_dict["offside_distance_player2"] = offside_distance_player2
        if receiving_player3 is not UNSET:
            field_dict["receiving_player3"] = receiving_player3
        if offside_distance_player3 is not UNSET:
            field_dict["offside_distance_player3"] = offside_distance_player3

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

        number_of_players_offside = d.pop("number_of_players_offside", UNSET)

        receiving_player1 = d.pop("receiving_player1", UNSET)

        offside_distance_player1 = d.pop("offside_distance_player1", UNSET)

        receiving_player2 = d.pop("receiving_player2", UNSET)

        offside_distance_player2 = d.pop("offside_distance_player2", UNSET)

        receiving_player3 = d.pop("receiving_player3", UNSET)

        offside_distance_player3 = d.pop("offside_distance_player3", UNSET)

        event_detected_offside_soccer = cls(
            timestamp=timestamp,
            timestamp_ms=timestamp_ms,
            timezone_id=timezone_id,
            game_clock=game_clock,
            period=period,
            player_id=player_id,
            group_id=group_id,
            number_of_players_offside=number_of_players_offside,
            receiving_player1=receiving_player1,
            offside_distance_player1=offside_distance_player1,
            receiving_player2=receiving_player2,
            offside_distance_player2=offside_distance_player2,
            receiving_player3=receiving_player3,
            offside_distance_player3=offside_distance_player3,
        )

        event_detected_offside_soccer.additional_properties = d
        return event_detected_offside_soccer

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
