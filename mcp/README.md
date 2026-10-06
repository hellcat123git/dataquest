# MCP Server Setup Guide

## What is MCP?
Model Context Protocol (MCP) servers give your AI agent "hands" — the ability to search the web, query databases, and read files. Without MCP, the AI only knows what you type to it. With MCP, the AI can search Kaggle, read your CSV, and write code all in one response.

## How to Activate (Claude Desktop)
1. Copy the contents of `mcp/mcp_config.json`.
2. Open Claude Desktop settings → Developer → Edit Config.
3. Paste the JSON. Save. Restart Claude Desktop.

## How to Activate (Cursor)
1. Open Cursor Settings → MCP Servers.
2. Add each server from `mcp/mcp_config.json` individually.

## Required Environment Variables (add to .env)
