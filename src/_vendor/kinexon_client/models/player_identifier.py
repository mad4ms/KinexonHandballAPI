from collections.abc import Mapping
from typing import Any, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PlayerIdentifier")


@_attrs_define
class PlayerIdentifier:
    """
    Attributes:
        in_team_team (Union[Unset, str]): Select all players of a team <TEAM>
        in_group_group (Union[Unset, str]): Select all players of a group <GROUP>
        in_league_league (Union[Unset, str]): Select all players of league <LEAGUE>
        in_entity (Union[Unset, str]): Select all players of selected entity (only in combination with TimeEntity
            schema)
        player_id (Union[Unset, int]): Select only one player with given <PLAYER_ID>
        player_idplayer_id (Union[Unset, str]): Select a set of player with comma seperated <PLAYER_ID>
    """

    in_team_team: Union[Unset, str] = UNSET
    in_group_group: Union[Unset, str] = UNSET
    in_league_league: Union[Unset, str] = UNSET
    in_entity: Union[Unset, str] = UNSET
    player_id: Union[Unset, int] = UNSET
    player_idplayer_id: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        in_team_team = self.in_team_team

        in_group_group = self.in_group_group

        in_league_league = self.in_league_league

        in_entity = self.in_entity

        player_id = self.player_id

        player_idplayer_id = self.player_idplayer_id

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if in_team_team is not UNSET:
            field_dict["in-team-<TEAM>"] = in_team_team
        if in_group_group is not UNSET:
            field_dict["in-group-<GROUP>"] = in_group_group
        if in_league_league is not UNSET:
            field_dict["in-league-<LEAGUE>"] = in_league_league
        if in_entity is not UNSET:
            field_dict["in-entity"] = in_entity
        if player_id is not UNSET:
            field_dict["<PLAYER_ID>"] = player_id
        if player_idplayer_id is not UNSET:
            field_dict["<PLAYER_ID>,<PLAYER_ID>"] = player_idplayer_id

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        in_team_team = d.pop("in-team-<TEAM>", UNSET)

        in_group_group = d.pop("in-group-<GROUP>", UNSET)

        in_league_league = d.pop("in-league-<LEAGUE>", UNSET)

        in_entity = d.pop("in-entity", UNSET)

        player_id = d.pop("<PLAYER_ID>", UNSET)

        player_idplayer_id = d.pop("<PLAYER_ID>,<PLAYER_ID>", UNSET)

        player_identifier = cls(
            in_team_team=in_team_team,
            in_group_group=in_group_group,
            in_league_league=in_league_league,
            in_entity=in_entity,
            player_id=player_id,
            player_idplayer_id=player_idplayer_id,
        )

        player_identifier.additional_properties = d
        return player_identifier

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
