# Dispatch Model
This is a demonstration/test package. It uses pydantic to validate YAML manifests. The manifests 
that it validates against are chosed based on the `apiVersion` field of the manifest. `apiVersion` 
is required to be in the form `package_name/api_version` where `package_name` is the name of an 
installed python package and `api_version` is the name of a directory that exists at 
`package_name/pydantic/api_version`.

The package contains two API versions, v1 and v2. They can be referenced using `apiVersion: 
dispatch_model/v1` and `apiVersion: dispatch_model/v2`, respectively. Also provided are a test 
script, `test_manifest.py` and test manifests under `./manifests`.

`test_manifests.py` accepts a single argument. That argument should be the path to a manifest to be 
tested. Calling `test_manifests.py` with the three provided test manifests should result in the 
following:

```bash
> python test_manifest.py ./manifests/good_v1.yaml
<class 'dispatch_model.pydantic.v1.models.TestPluginModel'>
apiVersion='dispatch_model/v1' kind='Test' test='test'
(pydantic)

> python test_manifest.py ./manifests/good_v2.yaml
<class 'dispatch_model.pydantic.v2.models.TestPluginModel'>
apiVersion='dispatch_model/v2' kind='Test' test='test' test2='test2'
(pydantic)

> python test_manifest.py ./manifests/bad_v1.yaml
Traceback (most recent call last):
  File "/Users/jsolbrig/dispatch_model/test_manifest.py", line 9, in <module>
    plg = load_plugin(plg_dict)
          ^^^^^^^^^^^^^^^^^^^^^
  File "/Users/jsolbrig/dispatch_model/dispatch_model/dispatch_model.py", line 35, in load_plugin
    return model_class.model_validate(data)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/Users/jsolbrig/miniconda3/envs/pydantic/lib/python3.11/site-packages/pydantic/main.py", line 703, in model_validate
    return cls.__pydantic_validator__.validate_python(
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
pydantic_core._pydantic_core.ValidationError: 1 validation error for TestPluginModel
test2
  Extra inputs are not permitted [type=extra_forbidden, input_value='test2', input_type=str]
    For further information visit https://errors.pydantic.dev/2.11/v/extra_forbidden
