# YAML vs JSON Size Benchmark

### Scenario

Deeply nested Power Automate-style payload including nested objects, arrays, and multiple layers.

### Result

- JSON Size: 1029 bytes
- YAML Size: 619 bytes
- Reduction: ~40%

### Takeaway

When scaled to millions of messages:
- Less bandwidth
- Faster transmission
- Lower cloud storage and CPU cost
- Higher human readability
