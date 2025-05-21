from typing import Literal
from pydantic import BaseModel, ConfigDict, Field


class TestPluginModel(BaseModel):
    model_config = ConfigDict(extra="forbid")
    apiVersion: Literal["dispatch_model/v2"] = "dispatch_model/v2"
    kind: str
    test: str
    test2: str
