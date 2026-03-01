import json
from typing import Any

# Mapping from ugly hashed operationId -> meaningful name
OPID_MAP = {
    "566d29114a11605d95737f60abd4cfd0": "GetStatisticsListDeprecated",
    "d54d2f11c25c494177d090ea3b95f3db": "GetPublicV1StatisticsList",
    "78177200cc2b9fff7579ada0b1ecbc78": "GetTeamsByTeamIdPlayersDeprecated",
    "e3bcaeeece5bd8b95151ff7669d53994": "GetPublicV1TeamsByTeamIdPlayers",
    "49a583357f101cc1006c15dea3efa105": "GetTeamsByTeamIdPlayersByPlayerIdDeprecated",
    "be90c35c61275ac6baef43ab359c001f": "GetPublicV1TeamsByTeamIdPlayersByPlayerId",
    "0ff053da47c2c9aff6a630969537dd41": "GetStatisticsByTypeByPlayerIdByTimeEntityTypeByTimeEntityIdentifierDeprecated",  # noqa: E501
    "a7cad42141c2fb49dd1c3b67e1c968c2": "GetPublicV1StatisticsByTypeByPlayerIdByTimeEntityTypeByTimeEntityIdentifier",  # noqa: E501
    "4c360929b311565c84813123eea34d15": "GetStatisticsByTypeByPlayerIdByTimeEntityRangeTypeDeprecated",  # noqa: E501
    "6140e44b435c3a7a5abb242b29b6e3ac": "GetPublicV1StatisticsByTypeByPlayerIdByTimeEntityRangeType",  # noqa: E501
    "2f0b7602d8727d1554e6117288066419": "GetExportPositionsSessionByTimeEntityIdentifierDeprecated",  # noqa: E501
    "518b3d20ddb1e4d6c4c1e1e5d7c8c280": "GetPublicV1ExportPositionsSessionByTimeEntityIdentifier",  # noqa: E501
    "fcf0afd2f23dde1f15154cc98707c6a1": "GetExportInertialSessionByTimeEntityIdentifierDeprecated",  # noqa: E501
    "2bd187efb4692eb25dfe220c2ca43e61": "GetPublicV1ExportInertialSessionByTimeEntityIdentifier",  # noqa: E501
    "45398dc6e355095495ff3d7b3af976cd": "GetSensorAssignmentByTimeEntityIdentifierDeprecated",  # noqa: E501
    "01b59cb8a2cb10b8a311829c5f4a8b9b": "GetPublicV1SensorAssignmentByTimeEntityIdentifier",  # noqa: E501
    "4b000d72fdb374144e95fc4c2cf75b1a": "GetTeamsByTeamIdSessionsAndPhasesDeprecated",
    "3709a95cd3000e6377d69b3a55d048e2": "GetPublicV1TeamsByTeamIdSessionsAndPhases",
    "2a9ca44b0734126f65503a9cb9a0260b": "GetStatisticsBySessionIdCategoriesDeprecated",
    "7e09029201135344482130236d7d3626": "GetPublicV1StatisticsBySessionIdCategories",
}


def replace_operation_ids(data: Any) -> Any:
    """Recursively traverse OpenAPI spec and replace operationId values."""
    if isinstance(data, dict):
        if "operationId" in data and data["operationId"] in OPID_MAP:
            old = data["operationId"]
            new = OPID_MAP[old]
            data["operationId"] = new
            print(f"Replaced {old} -> {new}")
        for _k, v in data.items():
            replace_operation_ids(v)
    elif isinstance(data, list):
        for item in data:
            replace_operation_ids(item)
    return data


def main() -> None:
    with open("openapi/sport_app.json", encoding="utf-8") as f:
        spec = json.load(f)

    updated = replace_operation_ids(spec)

    with open("sports_app_opids.json", "w", encoding="utf-8") as f:
        json.dump(updated, f, indent=2, ensure_ascii=False)

    print("Updated file written to sports_app.with-opids.json")


if __name__ == "__main__":
    main()
