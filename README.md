SublimeLinter-contrib-generic
================================

[![Build Status](https://travis-ci.org/SublimeLinter/SublimeLinter-contrib-generic.svg?branch=master)](https://travis-ci.org/SublimeLinter/SublimeLinter-contrib-generic)

This linter plugin for [SublimeLinter](https://github.com/SublimeLinter/SublimeLinter) provides an interface to any generic linter.

## Installation
SublimeLinter must be installed in order to use this plugin.

Please use [Package Control](https://packagecontrol.io) to install the linter plugin.

In order for the required linter to be executed by SublimeLinter, you must ensure that its path is available to SublimeLinter. The docs cover [troubleshooting PATH configuration](http://sublimelinter.readthedocs.io/en/latest/troubleshooting.html#finding-a-linter-executable).

## Settings
- SublimeLinter settings: http://sublimelinter.readthedocs.org/en/latest/settings.html
- Linter settings: http://sublimelinter.readthedocs.org/en/latest/linter_settings.html

Additional SublimeLinter-generic settings:

|Setting     |Description    |
|:-----------|:--------------|
|name        |Name of the linter to show in annotations (default: 'generic'). |
|executable* |The linters executable. |
|selector*   |The scope name which the linter should be applied to. (eg.: 'source.yaml') |
|regexp*.    |The regexp matching the linters output. (`\` should be escaped) |

Use the regexp to match:

- line (`(?P<line>\\d+)`)
- col (`(?P<col>\\d+)`)
- error
- warning
- message (`(?P<message>.+)`)
- near
- filename (`(?P<file_name>.+)`)
- error_type (`(?P<error_type>[warning|error]+)`)
- code (`(?P<code>\\d+)`)
- end_line (`(?P<end_line>\\d+)`)
- end_col (`(?P<end_col>\\d+)`)

### Example for [spectral](https://meta.stoplight.io/docs/spectral/674b27b261c3c-overview)

Given spectral's output:

```bash
   1:1   warning  oas3-api-servers  OpenAPI "servers" must be present and non-empty array.
  10:9   warning  operation-tags    Operation must have non-empty "tags" array.             paths./v1/foo/{id}.get
  13:9     error  oas3-schema       "tags" property type must be array.                     paths./v1/bar/complete.get
  36:9   warning  operation-tags    Operation must have non-empty "tags" array.             paths./v1/baz/index.get
```

The following setting will match `line`, `col`, `error_type` and `message`:

```json
...
  "generic": {
    "name": "spectral",
    "args": ["lint", "--ruleset", "~/.config/.spectral.yaml"],
    "executable": "spectral",
    "selector": "source.yaml",
    "regexp": "\\s*(?P<line>\\d+):(?P<col>\\d+)\\s+(?P<error_type>[warning|error]+)\\s+(?P<message>.+)"
  },
...
```
