"""
Configuration for Kinexon Handball API client.
This module defines the settings for the Kinexon Handball API client,
including authentication credentials and API endpoints.
"""

from pydantic import Field, AliasChoices
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """
    Settings for Kinexon Handball API client.
    This class uses environment variables for configuration.
    """

    model_config = SettingsConfigDict(
        env_file=".env",  # optional if you already call load_dotenv()
        env_file_encoding="utf-8",
        env_prefix="",  # no implicit prefix
        case_sensitive=True,  # keep exact case
    )

    username_session: str = Field(
        validation_alias=AliasChoices("USERNAME_KINEXON_SESSION")
    )
    password_session: str = Field(
        validation_alias=AliasChoices("PASSWORD_KINEXON_SESSION")
    )
    endpoint_session: str = Field(
        validation_alias=AliasChoices("ENDPOINT_KINEXON_SESSION")
    )

    username_main: str = Field(
        validation_alias=AliasChoices("USERNAME_KINEXON_MAIN")
    )
    password_main: str = Field(
        validation_alias=AliasChoices("PASSWORD_KINEXON_MAIN")
    )
    endpoint_main: str = Field(
        validation_alias=AliasChoices("ENDPOINT_KINEXON_MAIN")
    )

    api_key: str = Field(validation_alias=AliasChoices("API_KEY_KINEXON"))
    endpoint_api: str = Field(
        validation_alias=AliasChoices("ENDPOINT_KINEXON_API")
    )
    verify_ssl: bool = Field(
        True, validation_alias=AliasChoices("VERIFY_SSL_KINEXON", "VERIFY_SSL")
    )
