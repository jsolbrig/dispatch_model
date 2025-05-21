from typing import Literal
from pydantic import BaseModel, ConfigDict, Field


class TestPluginModel(BaseModel):
    model_config = ConfigDict(extra="forbid")
    apiVersion: Literal["dispatch_model/v1"] = "dispatch_model/v1"
    kind: str
    test: str
