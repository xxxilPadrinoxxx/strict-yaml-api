# StrictYAML for APIs — Specification (Draft)

## Goals

- Fully interoperable with JSON (1:1 mapping)
- No YAML anchors, aliases, or custom tags
- Only explicit typing — no magic booleans or nulls
- Safe parsing — no execution, no object construction
- Schema validation using existing or future YAML-compatible schema language

## Disallowed Features

- Anchors (`&`) and Aliases (`*`)
- Custom Tags (e.g., `!!python/object`)
- Implicit booleans (`on`, `off`, `yes`, `no`) — must use `true`/`false`
- Nulls must be written as `null`, not `~` or empty

## Allowed Types

- Strings
- Numbers (integer, float)
- Booleans: `true`, `false`
- Null: `null`
- Arrays
- Maps (dictionaries)

## Compatibility

- Round-trip convertibility with JSON is required
- Parsers must be run in strict/safe mode
- The YAML file should be linearly and deterministically parsed, like JSON
