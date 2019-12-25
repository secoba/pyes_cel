## Python-Elastic-CEL

Convert common expression language to elasticsearch dsl query string

### Feature
- Logic Negation
- Logic AND
- Logic OR
- Logic Nesting
- Equation
- Range

### Demo
```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Author: lynn
# Date: 2019-12-25
"""
test.py
"""

import json

from pyes_cel.cel import parser_expr

if __name__ == '__main__':
    exprs = ["port >= 20",
             "sip == '1.1.1.1' and (port > 80 or dip == '2.2.2.2')"]
    for i in exprs:
        print(json.dumps(parser_expr(i), indent=4))
```

TODO:
- Attribution
- ...