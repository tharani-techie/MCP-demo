# MCP Weather Server 🌦️

This is the companion code for the article **"The Missing Interface: How Model Context Protocol (MCP) Turns Chatbots into Agents"**.

It demonstrates how to build a simple **Model Context Protocol (MCP)** server in Python that connects an AI (like Claude or VS Code Copilot) to the OpenWeatherMap API.

## Prerequisites

*   Python 3.10+
*   An OpenWeatherMap API Key (Free)

## Setup

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/yourusername/mcp-weather-server.git
    cd mcp-weather-server
    ```

2.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Configure API Key:**
    *   Copy `.env.example` to `.env`
    *   Add your API key to `.env`:
        ```env
        OPENWEATHER_API_KEY=your_actual_api_key_here
        ```

## Running with VS Code

1.  Ensure the **Model Context Protocol** extension (or Copilot Chat) is installed.
2.  The project includes a `.vscode/mcp.json` configuration file.
3.  Reload VS Code.
4.  Open Copilot Chat and ask: *"What is the weather in London?"*

## Running Manually

You can run the server directly to see it listen on Stdio (it won't do much without a client):

```bash
python weather_server.py
```

## License

MIT
