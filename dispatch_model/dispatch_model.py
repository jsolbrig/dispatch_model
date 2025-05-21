from pydantic import BaseModel, ValidationError, model_validator
from typing import Any, Optional
import importlib


def load_plugin(data: dict) -> BaseModel:
    try:
        api_version = data["apiVersion"]
        kind = data["kind"]
    except KeyError as e:
        raise ValueError(f"Missing required field: {e}")

    # Split "package_name/model_version"
    # We can use package_name to select the appropriate package to search for the api.
    # This way, we could access the api from geoips_real_time by using geoips_real_time/v1.
    try:
        package_name, model_version = api_version.split("/")
    except ValueError:
        raise ValueError(f"Invalid apiVersion format: {api_version}")

    # Construct module path and import
    try:
        module = importlib.import_module(f"{package_name}.pydantic.{model_version}")
    except ImportError as e:
        raise ImportError(f"Could not import models from '{api_version}': {e}")

    # Get the class matching `kind`
    model_name = f"{kind}PluginModel"
    try:
        model_class = getattr(module, model_name)
    except AttributeError:
        raise ValueError(f"Model for kind '{kind}' not found in '{api_version}'")

    # Validate using the correct class
    return model_class.model_validate(data)

