#!/usr/bin/env python3
"""
Demo MCP Server using FAST MCP framework.
Provides tools for text processing and data transformation.
"""

from fastmcp import FastMCP
import json
from typing import Any

# Initialize FastMCP server
mcp = FastMCP("demo-mcp-server")


@mcp.tool()
def get_weather(location: str) -> dict[str, Any]:
    """
    Get weather information for a location.
    
    Args:
        location: The location to get weather for
    
    Returns:
        Weather data for the location
    """
    return {
        "location": location,
        "temperature": 72,
        "condition": "Sunny",
        "humidity": 60
    }


@mcp.tool()
def process_text(text: str, operation: str) -> str:
    """
    Process text with various operations.
    
    Args:
        text: The text to process
        operation: The operation to perform (uppercase, lowercase, reverse)
    
    Returns:
        Processed text
    """
    if operation == "uppercase":
        return text.upper()
    elif operation == "lowercase":
        return text.lower()
    elif operation == "reverse":
        return text[::-1]
    else:
        return f"Unknown operation: {operation}"


@mcp.tool()
def calculate_stats(numbers: list[float]) -> dict[str, float]:
    """
    Calculate statistics for a list of numbers.
    
    Args:
        numbers: List of numbers
    
    Returns:
        Dictionary with mean, median, min, and max
    """
    if not numbers:
        return {"error": "Empty list"}
    
    sorted_nums = sorted(numbers)
    n = len(numbers)
    
    return {
        "count": n,
        "sum": sum(numbers),
        "mean": sum(numbers) / n,
        "median": sorted_nums[n // 2] if n % 2 else (sorted_nums[n // 2 - 1] + sorted_nums[n // 2]) / 2,
        "min": min(numbers),
        "max": max(numbers)
    }


if __name__ == "__main__":
    mcp.run()
