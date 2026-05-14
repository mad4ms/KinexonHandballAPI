from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="EventPassFifa")


@_attrs_define
class EventPassFifa:
    """
    Attributes:
        timestamp (int | Unset):
        timestamp_ms (int | Unset):
        timezone_id (int | Unset):
        game_clock (str | Unset):
        period (str | Unset):
        player_id (int | Unset):
        duration_ms (float | Unset):
        distance_m (float | Unset):
        max_speed_mps (float | Unset):
        average_spin_rate_rotp_s (float | Unset):
        start_position_mx (float | Unset):
        start_position_my (float | Unset):
        start_position_mz (float | Unset):
        end_position_mx (float | Unset):
        end_position_my (float | Unset):
        end_position_mz (float | Unset):
        verticality_m (float | Unset):
        horizontality_m (float | Unset):
        is_successful (int | Unset):
        meta_data (str | Unset):
    """

    timestamp: int | Unset = UNSET
    timestamp_ms: int | Unset = UNSET
    timezone_id: int | Unset = UNSET
    game_clock: str | Unset = UNSET
    period: str | Unset = UNSET
    player_id: int | Unset = UNSET
    duration_ms: float | Unset = UNSET
    distance_m: float | Unset = UNSET
    max_speed_mps: float | Unset = UNSET
    average_spin_rate_rotp_s: float | Unset = UNSET
    start_position_mx: float | Unset = UNSET
    start_position_my: float | Unset = UNSET
    start_position_mz: float | Unset = UNSET
    end_position_mx: float | Unset = UNSET
    end_position_my: float | Unset = UNSET
    end_position_mz: float | Unset = UNSET
    verticality_m: float | Unset = UNSET
    horizontality_m: float | Unset = UNSET
    is_successful: int | Unset = UNSET
    meta_data: str | Unset = UNSET
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
