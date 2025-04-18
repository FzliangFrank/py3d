# py3d
Python API for visualizing complex network data (and more) using d3.js

## Installation

You can install py3d using pip:

```bash
pip install py3d
```

For development installation:

```bash
git clone https://github.com/yourusername/py3d.git
cd py3d
pip install -e .
```

## Usage

[Add usage instructions here]

```py
from pyd3 import *

json_data = {
        'nodes': [{'id': 0, 'name': 'A'}
                , {'id': 1, 'name': 'B'}
                , {'id': 2, 'name': 'C'}
                ,{'id': 3, 'name': 'D'} ],
        'links': [{'source': 0, 'target': 1}
                , {'source': 1, 'target': 2}
                , {'source': 1, 'target': 3}
                , {'source':2, 'target': 3}]
    }


d3_force_graph(json_data)
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
