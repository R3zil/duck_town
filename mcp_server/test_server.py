#!/usr/bin/env python3
"""Simple test script for the MCP server tools."""

import asyncio
import tempfile
from pathlib import Path

from server import call_tool


async def test_file_operations():
    """Test file system operations."""
    print("Testing file system tools...\n")

    # Create a temporary directory for testing
    with tempfile.TemporaryDirectory() as tmpdir:
        test_dir = Path(tmpdir)
        test_file = test_dir / "test.txt"
        test_content = "Hello, MCP Server!"

        # Test 1: Write file
        print("1. Testing write_file...")
        result = await call_tool("write_file", {
            "path": str(test_file),
            "content": test_content
        })
        print(f"   Result: {result[0].text}")
        assert test_file.exists(), "File should exist after write"

        # Test 2: Read file
        print("\n2. Testing read_file...")
        result = await call_tool("read_file", {
            "path": str(test_file)
        })
        print(f"   Result: {result[0].text}")
        assert result[0].text == test_content, "File content should match"

        # Test 3: List directory
        print("\n3. Testing list_directory...")
        result = await call_tool("list_directory", {
            "path": str(test_dir)
        })
        print(f"   Result:\n{result[0].text}")
        assert "test.txt" in result[0].text, "File should be listed"

        # Test 4: Read non-existent file
        print("\n4. Testing read_file with non-existent file...")
        result = await call_tool("read_file", {
            "path": str(test_dir / "nonexistent.txt")
        })
        print(f"   Result: {result[0].text}")
        assert "Error" in result[0].text, "Should return error for non-existent file"

        # Test 5: List non-existent directory
        print("\n5. Testing list_directory with non-existent directory...")
        result = await call_tool("list_directory", {
            "path": str(test_dir / "nonexistent")
        })
        print(f"   Result: {result[0].text}")
        assert "Error" in result[0].text, "Should return error for non-existent directory"

    print("\n✅ All file system tests passed!")


async def test_basic_tools():
    """Test basic tools."""
    print("\nTesting basic tools...\n")

    # Test echo
    print("1. Testing echo...")
    result = await call_tool("echo", {"message": "Hello, World!"})
    print(f"   Result: {result[0].text}")
    assert result[0].text == "Hello, World!"

    # Test add
    print("\n2. Testing add...")
    result = await call_tool("add", {"a": 5, "b": 3})
    print(f"   Result: {result[0].text}")
    assert result[0].text == "8"

    # Test get_time
    print("\n3. Testing get_time...")
    result = await call_tool("get_time", {})
    print(f"   Result: {result[0].text}")
    assert len(result[0].text) > 0

    print("\n✅ All basic tool tests passed!")


async def main():
    """Run all tests."""
    print("=" * 60)
    print("MCP Server Test Suite")
    print("=" * 60)

    await test_basic_tools()
    await test_file_operations()

    print("\n" + "=" * 60)
    print("🎉 All tests passed successfully!")
    print("=" * 60)


if __name__ == "__main__":
    asyncio.run(main())
