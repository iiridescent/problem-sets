# Widgets

## Text

```yaml
options:
    text: HTML escaped string
```

## Graph

``` yaml
options:
    functions: [{
        expression: math.js compatible expression string
        minX: double
        maxX: double
        step: double
        title: string (optional)
        color: color (optional)
    }]
    tables: [{
        xValues: [int]
        yValues: [int]
        title: string (optional)
        color: color (optional)
    }]
    
```
