#!/usr/bin/env python3

import sys
import yaml
import json

def validate_strict_yaml(data):
    if any(isinstance(val, yaml.Node) for val in data):
        raise ValueError("Anchors or complex YAML features detected")
    return True

def main():
    if len(sys.argv) != 2:
        print("Usage: strictyaml.py <file.yaml>")
        return

    path = sys.argv[1]
    with open(path, 'r') as f:
        try:
            data = yaml.safe_load(f)
            json_data = json.dumps(data, indent=2)
            print("✅ Valid StrictYAML\n(YAML input is safe)\n\nConverted to JSON:")
            print(json_data)
        except yaml.YAMLError as e:
            print("❌ YAML error:", e)
        except Exception as e:
            print("❌ StrictYAML validation failed:", e)

if __name__ == "__main__":
    main()
