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

## 🛣 Roadmap

This roadmap outlines key milestones toward a stable StrictYAML specification and tooling ecosystem.

### ✅ v0.1 – Strict Parsing + CLI
- ✅ Disallow YAML anchors, aliases, and unsafe tags
- ✅ Require explicit types (`true`, `false`, `null`)
- ✅ Python CLI validator (`strictyaml.py`)
- ✅ Real-world examples and benchmarks
- ✅ Launch GitHub Action for validation
- 📝 Spec draft in progress

### 🛠 v0.2 – Schema + Validation Layer
- ❓ Decide between JSON Schema vs YAML-native schema
- 🧪 Schema validation for example files
- 🧰 Improve CLI UX: config options, validation output
- 🧼 Add unit tests and edge cases

### 🚀 v1.0 – Public Release
- 📘 Finalized StrictYAML specification
- 📦 Publish CLI as PyPI package (`strictyaml-api`)
- 🌐 Optional web validator or GitHub App integration
- 📣 Community outreach and adoption

## Specification

See `spec/strict-yaml-api-spec.md`

## License

MIT

## 📣 Join the Launch Discussion

We’re talking about the future of YAML-based APIs here:  
👉 [Discussion #1: Launching StrictYAML for APIs](https://github.com/xxxilPadrinoxxx/strict-yaml-api/discussions/1)

## 🐍 Python CLI Usage

You can run StrictYAML from the command line using the Python-based CLI.

### 🐚 Bash / Shell

📦 Install (from source):

```bash
pip install pyyaml
```

Run the StrictYAML validator:

```bash
python strictyaml_api/cli.py ./examples/power-automate.yaml
```

### ✅ Expected Output

```text
✅ Valid StrictYAML
{
  "workflow": {
    "id": "abc123",
    "steps": [
      { "name": "Trigger", "type": "HttpRequest", ... }
    ]
  }
}
```

> 💡 Tip: Want it globally? Use `pip install .` inside the project root.

---

## ⚡ PowerShell Support

StrictYAML can also be used directly in PowerShell for validation and JSON conversion.

### 📥 Import and Use

```powershell
# Import the module
Import-Module ./powershell/StrictYAML.psm1

# Validate and convert a YAML file
Test-StrictYAML -Path ./examples/power-automate.yaml
```

### ✅ Expected Output

```text
✅ Valid StrictYAML
{
  "workflow": {
    "id": "abc123",
    "steps": [
      { "name": "Trigger", "type": "HttpRequest", ... }
    ]
  }
}
```

> ⚠️ Requires: PowerShell 5.1+ and the `powershell-yaml` module  
(Install with `Install-Module powershell-yaml` if needed)
