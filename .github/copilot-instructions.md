# Edison Scientific Integration

Integration with [Edison Scientific](https://edisonscientific.com/platform) (formerly FutureHouse) for AI-powered academic research assistance.

## Quick Start

```bash
# Install (using uv for faster installation)
uv pip install edison-client

# Or use regular pip
pip install edison-client

# Configure (get API key from https://edisonscientific.com)
export EDISON_API_KEY='your_api_key'

# Run example
python edison_example.py
```

## Usage

```python
from edison_client import EdisonClient, JobNames

client = EdisonClient()

# Literature search
task = {
    "name": JobNames.LITERATURE,
    "query": "Recent advances in battery materials"
}
response = client.run_tasks_until_done(task)
print(response[0].formatted_answer)
```

## Capabilities

- **Literature Search** (`JobNames.LITERATURE`) - Paper search with citations
- **Precedent Search** (`JobNames.PRECEDENT`) - Prior art verification
- **Data Analysis** (`JobNames.ANALYSIS`) - Scientific data processing
- **Chemistry Tools** (`JobNames.MOLECULES`) - Molecular experiment planning

## Resources

- [API Documentation](https://edisonscientific.gitbook.io/edison-cookbook/edison-client)
- [Edison Scientific Platform](https://edisonscientific.com/platform)
- [PyPI Package](https://pypi.org/project/edison-client/)
