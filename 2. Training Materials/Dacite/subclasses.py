from dataclasses import dataclass
from typing import Literal, List, Union, Optional, TypedDict


@dataclass
class AuthenticationConfig:
    base_url: Optional[str] = None
    browser: Optional[Literal["chromium", "firefox", "webkit"]] = None
    auth_objects: Optional[dict] = None
    max_uses: Optional[int] = 0
    count: Optional[int] = 0


@dataclass
class BaseConfig:
    base_url: Optional[str]
    base_headers: dict
    max_attempts: int


@dataclass
class ErrorConfig:
    class_type: Literal['ErrorTask']
    data: dict
    response_methods: Optional[None] = None


@dataclass
class InitialTaskConfig:
    class_type: Literal["HexagonInitializer", "CountyInitializer", "ProviderInitializer"]
    data: Optional[Union[dict, None]]
    response_methods: List[str]


@dataclass
class TaskConfig:
    class_type: Literal[
        "RequestTask",
        "AtomizerTask",
        "LocationParserTask",
        "PersonalParserTask",
        "FacilityParserTask",
        "NetworkParserTask",
        "HTML2JSONTask"
    ]
    data: dict
    response_methods: Union[List[str], None]
