# StrictYAML for APIs

A strict, safe, and efficient YAML subset designed for machine-to-machine communication. Up to 40% smaller than JSON. More readable. Safer than vanilla YAML.

## Why?

JSON is the default for APIs, but:
- It's noisy and hard to read
- It's inefficient for deeply nested data
- It's not friendly for low-code, edge, or high-volume environments

YAML is better for humans — but too loose for machines.

**StrictYAML for APIs** aims to fix that.

## Goals

- 🚫 No anchors, aliases, or executable tags
- 🔐 Schema-validated and parse-safe
- 🔁 Fully convertible to/from JSON
- 📉 Smaller payloads, faster performance

## Status

🔧 Early-stage. Looking for collaborators!

## Examples

See the `examples/` folder for real-world comparisons.

## Benchmarks

YAML: 619 bytes  
JSON: 1029 bytes  
(~40% reduction)

## Specification

See `spec/strict-yaml-api-spec.md`

## License

MIT
