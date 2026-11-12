# USP Device Validation Automation

Reconstructed from the portfolio's Nokia validation-automation case: Python and Robot Framework test automation, with a reported roughly 30% reduction in validation time. No Nokia firmware, operator credentials, proprietary test suites, or device logs are included. The historical impact is not re-measured by this generic demo.

## Run

`python3 validate.py sample_plan.json sample_device.json` executes a JSON validation plan against a fixture and writes a timestamped report. Supported operations are `equals`, `contains`, `truthy`, and `type`; each check names a field path. The adapter boundary is deliberately local and safe; it does not connect to live devices or MQTT.

## Verify

`python3 -m unittest -v`
