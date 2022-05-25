from dataclasses import dataclass
from typing import Optional

from subclasses import (
    AuthenticationConfig,
    BaseConfig,
    InitialTaskConfig,
    TaskConfig,
    ErrorConfig,
)


@dataclass
class ConfigModel:
    config: BaseConfig
    initial_task: InitialTaskConfig
    tasks: dict[str, TaskConfig]
    authentication: Optional[AuthenticationConfig] = AuthenticationConfig()
    error_handling: ErrorConfig = ErrorConfig(
        class_type="ErrorTask",
        data=dict(
            error_type="<Response(error_response).error_type>", error_code="<Response(error_response).error_code>"
        ),
    )
