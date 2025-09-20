from collections.abc import Mapping
from typing import Any, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="PlayerModel")


@_attrs_define
class PlayerModel:
    """
    Attributes:
        cache_buster_hash (Union[Unset, str]): the cachebuster hash
        id (Union[Unset, int]): the player id
        first_name (Union[Unset, str]): First Name of the player
        last_name (Union[Unset, str]): Last Name of the player
        function (Union[Unset, str]): Function of the player
        number (Union[Unset, int]): Number of the player
        date_of_birth (Union[Unset, str]): Date of birth of the player
        last_tag_ids (Union[Unset, list[int]]): Array of last tag id's (integers) of the player
        last_group (Union[Unset, int]): Last Group of the player
        team_id (Union[Unset, int]): Team Id of the player
        league_id (Union[Unset, str]): League Id of the player
        deleted (Union[Unset, bool]): Is the player deleted
        player_db_uuid (Union[Unset, str]): UUID of the Player
        sports_cloud_uuid (Union[Unset, str]): UUID in Sports Cloud
        sports_cloud_version (Union[Unset, str]): Datetime version
    """

    cache_buster_hash: Union[Unset, str] = UNSET
    id: Union[Unset, int] = UNSET
    first_name: Union[Unset, str] = UNSET
    last_name: Union[Unset, str] = UNSET
    function: Union[Unset, str] = UNSET
    number: Union[Unset, int] = UNSET
    date_of_birth: Union[Unset, str] = UNSET
    last_tag_ids: Union[Unset, list[int]] = UNSET
    last_group: Union[Unset, int] = UNSET
    team_id: Union[Unset, int] = UNSET
    league_id: Union[Unset, str] = UNSET
    deleted: Union[Unset, bool] = UNSET
    player_db_uuid: Union[Unset, str] = UNSET
    sports_cloud_uuid: Union[Unset, str] = UNSET
    sports_cloud_version: Union[Unset, str] = UNSET
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        cache_buster_hash = self.cache_buster_hash

        id = self.id

        first_name = self.first_name

        last_name = self.last_name

        function = self.function

        number = self.number

        date_of_birth = self.date_of_birth

        last_tag_ids: Union[Unset, list[int]] = UNSET
        if not isinstance(self.last_tag_ids, Unset):
            last_tag_ids = self.last_tag_ids

        last_group = self.last_group

        team_id = self.team_id

        league_id = self.league_id

        deleted = self.deleted

        player_db_uuid = self.player_db_uuid

        sports_cloud_uuid = self.sports_cloud_uuid

        sports_cloud_version = self.sports_cloud_version

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if cache_buster_hash is not UNSET:
            field_dict["cacheBusterHash"] = cache_buster_hash
        if id is not UNSET:
            field_dict["id"] = id
        if first_name is not UNSET:
            field_dict["first_name"] = first_name
        if last_name is not UNSET:
            field_dict["last_name"] = last_name
        if function is not UNSET:
            field_dict["function"] = function
        if number is not UNSET:
            field_dict["number"] = number
        if date_of_birth is not UNSET:
            field_dict["dateOfBirth"] = date_of_birth
        if last_tag_ids is not UNSET:
            field_dict["last_tag_ids"] = last_tag_ids
        if last_group is not UNSET:
            field_dict["last_group"] = last_group
        if team_id is not UNSET:
            field_dict["team_id"] = team_id
        if league_id is not UNSET:
            field_dict["league_id"] = league_id
        if deleted is not UNSET:
            field_dict["deleted"] = deleted
        if player_db_uuid is not UNSET:
            field_dict["player_db_uuid"] = player_db_uuid
        if sports_cloud_uuid is not UNSET:
            field_dict["sports_cloud_uuid"] = sports_cloud_uuid
        if sports_cloud_version is not UNSET:
            field_dict["sports_cloud_version"] = sports_cloud_version

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        d = dict(src_dict)
        cache_buster_hash = d.pop("cacheBusterHash", UNSET)

        id = d.pop("id", UNSET)

        first_name = d.pop("first_name", UNSET)

        last_name = d.pop("last_name", UNSET)

        function = d.pop("function", UNSET)

        number = d.pop("number", UNSET)

        date_of_birth = d.pop("dateOfBirth", UNSET)

        last_tag_ids = cast(list[int], d.pop("last_tag_ids", UNSET))

        last_group = d.pop("last_group", UNSET)

        team_id = d.pop("team_id", UNSET)

        league_id = d.pop("league_id", UNSET)

        deleted = d.pop("deleted", UNSET)

        player_db_uuid = d.pop("player_db_uuid", UNSET)

        sports_cloud_uuid = d.pop("sports_cloud_uuid", UNSET)

        sports_cloud_version = d.pop("sports_cloud_version", UNSET)

        player_model = cls(
            cache_buster_hash=cache_buster_hash,
            id=id,
            first_name=first_name,
            last_name=last_name,
            function=function,
            number=number,
            date_of_birth=date_of_birth,
            last_tag_ids=last_tag_ids,
            last_group=last_group,
            team_id=team_id,
            league_id=league_id,
            deleted=deleted,
            player_db_uuid=player_db_uuid,
            sports_cloud_uuid=sports_cloud_uuid,
            sports_cloud_version=sports_cloud_version,
        )

        player_model.additional_properties = d
        return player_model

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
