# PyVii

A simple to use http request json data validator.
Note: This validator does not have a decorator implementation

## Installation
Installing using pip (recommended)
Note: This package is currently in development so you can only install from test.pypi repository for now

```bash
pip install --index-url https://test.pypi.org/simple/ pyvii
```
## Usage

```python
from pyvii.validator import Validator
validator = Validator()
schema = {
    'name': ['required'],
    'email': ['email']
}
payload = request.json ### your http request json data
validator.validate(schema, payload)
```

## Available methods
```python
    """
    checks if the validator has errors
    """
    has_errors()
    
    """
    checks if the validator has a specific error
    """
    has_error(key)
    
    """
    returns the errors dictionary
    """
    get_errors()
```