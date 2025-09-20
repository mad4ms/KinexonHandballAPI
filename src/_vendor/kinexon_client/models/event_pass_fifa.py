from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="EventPassFifa")


@_attrs_define
class EventPassFifa:
    """
    Attributes:
        timestamp (Union[Unset, int]):
        timestamp_ms (Union[Unset, int]):
        timezone_id (Union[Unset, int]):
        game_clock (Union[Unset, str]):
        period (Union[Unset, str]):
        player_id (Union[Unset, int]):
        duration_ms (Union[Unset, float]):
        distance_m (Union[Unset, float]):
        max_speed_mps (Union[Unset, float]):
        average_spin_rate_rotp_s (Union[Unset, float]):
        start_position_mx (Union[Unset, float]):
        start_position_my (Union[Unset, float]):
        start_position_mz (Union[Unset, float]):
        end_position_mx (Union[Unset, float]):
        end_position_my (Union[Unset, float]):
        end_position_mz (Union[Unset, float]):
        verticality_m (Union[Unset, float]):
        horizontality_m (Union[Unset, float]):
        is_successful (Union[Unset, int]):
        meta_data (Union[Unset, str]):
    """

    timestamp: Union[Unset, int] = UNSET
    timestamp_ms: Union[Unset, int] = UNSET
    timezone_id: Union[Unset, int] = UNSET
    game_clock: Union[Unset, str] = UNSET
    period: Union[Unset, str] = UNSET
    player_id: Union[Unset, int] = UNSET
    duration_ms: Union[Unset, float] = UNSET
    distance_m: Union[Unset, float] = UNSET
    max_speed_mps: Union[Unset, float] = UNSET
    average_spin_rate_rotp_s: Union[Unset, float] = UNSET
    start_position_mx: Union[Unset, float] = UNSET
    start_position_my: Union[Unset, float] = UNSET
    start_position_mz: Union[Unset, float] = UNSET
    end_position_mx: Union[Unset, float] = UNSET
    end_position_my: Union[Unset, float] = UNSET
    end_position_mz: Union[Unset, float] = UNSET
    verticality_m: Union[Unset, float] = UNSET
    horizontality_m: Union[Unset, float] = UNSET
    is_successful: Union[Unset, int] = UNSET
    meta_data: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        timestamp = self.timestamp

        timestamp_ms = self.timestamp_ms

        timezone_id = self.timezone_id

        game_clock = self.game_clock

        period = self.period

        player_id = self.player_id

        duration_ms = self.duration_ms

        distance_m = self.distance_m

        max_speed_mps = self.max_speed_mps

        average_spin_rate_rotp_s = self.average_spin_rate_rotp_s

        start_position_mx = self.start_position_mx

        start_position_my = self.start_position_my

        start_position_mz = self.start_position_mz

        end_position_mx = self.end_position_mx

        end_position_my = self.end_position_my

        end_position_mz = self.end_position_mz

        verticality_m = self.verticality_m

        horizontality_m = self.horizontality_m

        is_successful = self.is_successful

        meta_data = self.meta_data

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
            field_dict["playerId"] = player_id
        if duration_ms is not UNSET:
            field_dict["durationMs"] = duration_ms
        if distance_m is not UNSET:
            field_dict["distanceM"] = distance_m
        if max_speed_mps is not UNSET:
            field_dict["maxSpeedMps"] = max_speed_mps
        if average_spin_rate_rotp_s is not UNSET:
            field_dict["averageSpinRateRotpS"] = average_spin_rate_rotp_s
        if start_position_mx is not UNSET:
            field_dict["startPositionMX"] = start_position_mx
        if start_position_my is not UNSET:
            field_dict["startPositionMY"] = start_position_my
        if start_position_mz is not UNSET:
            field_dict["startPositionMZ"] = start_position_mz
        if end_position_mx is not UNSET:
            field_dict["endPositionMX"] = end_position_mx
        if end_position_my is not UNSET:
            field_dict["endPositionMY"] = end_position_my
        if end_position_mz is not UNSET:
            field_dict["endPositionMZ"] = end_position_mz
        if verticality_m is not UNSET:
            field_dict["verticalityM"] = verticality_m
        if horizontality_m is not UNSET:
            field_dict["horizontalityM"] = horizontality_m
        if is_successful is not UNSET:
            field_dict["isSuccessful"] = is_successful
        if meta_data is not UNSET:
            field_dict["metaData"] = meta_data

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        timestamp = d.pop("timestamp", UNSET)

        timestamp_ms = d.pop("timestamp_ms", UNSET)

        timezone_id = d.pop("timezone_id", UNSET)

        game_clock = d.pop("game_clock", UNSET)

        period = d.pop("period", UNSET)

        player_id = d.pop("playerId", UNSET)

        duration_ms = d.pop("durationMs", UNSET)

        distance_m = d.pop("distanceM", UNSET)

        max_speed_mps = d.pop("maxSpeedMps", UNSET)

        average_spin_rate_rotp_s = d.pop("averageSpinRateRotpS", UNSET)

        start_position_mx = d.pop("startPositionMX", UNSET)

        start_position_my = d.pop("startPositionMY", UNSET)

        start_position_mz = d.pop("startPositionMZ", UNSET)

        end_position_mx = d.pop("endPositionMX", UNSET)

        end_position_my = d.pop("endPositionMY", UNSET)

        end_position_mz = d.pop("endPositionMZ", UNSET)

        verticality_m = d.pop("verticalityM", UNSET)

        horizontality_m = d.pop("horizontalityM", UNSET)

        is_successful = d.pop("isSuccessful", UNSET)

        meta_data = d.pop("metaData", UNSET)

        event_pass_fifa = cls(
            timestamp=timestamp,
            timestamp_ms=timestamp_ms,
            timezone_id=timezone_id,
            game_clock=game_clock,
            period=period,
            player_id=player_id,
            duration_ms=duration_ms,
            distance_m=distance_m,
            max_speed_mps=max_speed_mps,
            average_spin_rate_rotp_s=average_spin_rate_rotp_s,
            start_position_mx=start_position_mx,
            start_position_my=start_position_my,
            start_position_mz=start_position_mz,
            end_position_mx=end_position_mx,
            end_position_my=end_position_my,
            end_position_mz=end_position_mz,
            verticality_m=verticality_m,
            horizontality_m=horizontality_m,
            is_successful=is_successful,
            meta_data=meta_data,
        )

        event_pass_fifa.additional_properties = d
        return event_pass_fifa

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
