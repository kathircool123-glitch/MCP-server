# MCP-server

A demo MCP (Model Context Protocol) server built with **FAST MCP** - a Python-first framework for creating MCP servers, clients, and AI apps.

## Overview

This project demonstrates a fully functional MCP server with several tools showcasing different capabilities:

- **Weather Tool**: Fetch weather information for locations
- **Text Processing Tool**: Transform text (uppercase, lowercase, reverse)
- **Statistics Tool**: Calculate statistical metrics (mean, median, min, max)

## Prerequisites

- Python 3.8+
- pip

## Installation

1. Clone the repository:
```bash
git clone https://github.com/kathircool123-glitch/MCP-server.git
cd MCP-server
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Running the Server

Start the MCP server:

```bash
python server.py
```

The server will start and be ready to receive requests.

## Available Tools

### 1. get_weather
Get weather information for a specified location.

**Parameters:**
- `location` (string): The location to get weather for

**Returns:** Weather data including temperature, condition, and humidity

### 2. process_text
Process text with various operations.

**Parameters:**
- `text` (string): The text to process
- `operation` (string): Operation type - "uppercase", "lowercase", or "reverse"

**Returns:** Processed text

### 3. calculate_stats
Calculate statistics for a list of numbers.

**Parameters:**
- `numbers` (array of numbers): List of numbers to analyze

**Returns:** Dictionary containing count, sum, mean, median, min, and max

## Example Usage

Once the server is running, clients can call the available tools:

```python
# Example: Process text
result = client.call_tool("process_text", {
    "text": "Hello World",
    "operation": "uppercase"
})
# Returns: "HELLO WORLD"

# Example: Calculate statistics
result = client.call_tool("calculate_stats", {
    "numbers": [1, 2, 3, 4, 5]
})
# Returns: {"count": 5, "sum": 15, "mean": 3.0, "median": 3.0, "min": 1, "max": 5}
```

## About FAST MCP

FAST MCP is a modern Python framework that simplifies the creation of:
- **MCP Servers**: Expose tools and resources via the Model Context Protocol
- **MCP Clients**: Consume tools and resources from MCP servers
- **AI Applications**: Build intelligent applications that interact with MCP servers

For more information, visit the [FAST MCP documentation](https://github.com/gofastapi/fastmcp).

## License

MIT License

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
