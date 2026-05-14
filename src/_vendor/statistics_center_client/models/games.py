from __future__ import annotations

from collections.abc import Mapping
from typing import Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="Games")


@_attrs_define
class Games:
    """
    Attributes:
        match_id (str | Unset):  Example: 1234813.
        home_team (str | Unset):  Example: Team A.
        away_team (str | Unset):  Example: Team B.
    """

    match_id: str | Unset = UNSET
    home_team: str | Unset = UNSET
    away_team: str | Unset = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        match_id = self.match_id

        home_team = self.home_team

        away_team = self.away_team

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if match_id is not UNSET:
            field_dict["match_id"] = match_id
        if home_team is not UNSET:
            field_dict["home_team"] = home_team
        if away_team is not UNSET:
            field_dict["away_team"] = away_team

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        match_id = d.pop("match_id", UNSET)

        home_team = d.pop("home_team", UNSET)

        away_team = d.pop("away_team", UNSET)

        games = cls(
            match_id=match_id,
            home_team=home_team,
            away_team=away_team,
        )

        games.additional_properties = d
        return games

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
