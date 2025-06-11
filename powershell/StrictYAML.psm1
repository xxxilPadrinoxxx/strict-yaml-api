function Test-StrictYAML {
    param (
        [Parameter(Mandatory)]
        [string]$Path
    )

    if (-not (Test-Path $Path)) {
        throw "File not found: $Path"
    }

    $yamlContent = Get-Content -Raw -Path $Path

    if ($yamlContent -match '&' -or $yamlContent -match '\*') {
        throw "❌ Anchors or aliases are not allowed in StrictYAML."
    }

    if ($yamlContent -match '\b(yes|no|on|off|~)\b') {
        throw "❌ Implicit booleans or nulls are not allowed. Use true/false/null explicitly."
    }

    try {
        $parsed = $yamlContent | ConvertFrom-Yaml
        Write-Host "✅ Valid StrictYAML`n(YAML input is safe)`n`nConverted to JSON:"
        $parsed | ConvertTo-Json -Depth 10
    } catch {
        throw "❌ Failed to parse YAML: $_"
    }
}
