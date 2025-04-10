# Euro Quote Widget

A macOS widget that displays Euro currency quotes.

## Prerequisites

- Python 3.x
- pip3
- macOS operating system

## Installation

1. Clone this repository:
```bash
git clone https://github.com/Andre3004/widget-macos-wise-eur-to-brl.git
cd widget-macos-wise-eur-to-brl
```
2. Update widget path in com.euro-quote.widget.plist
```bash
<key>ProgramArguments</key>
<array>
    <string>/Users/yourusername/widget-macos-wise-eur-to-brl/widget.py</string>
</array>
```

2. Run the setup script:
```bash
chmod +x setup.sh
./setup.sh
```

The setup script will:
- Install required Python dependencies
- Configure the widget to start automatically on login
- Start the widget immediately

## Managing the Widget

### Start the Widget
```bash
launchctl load ~/Library/LaunchAgents/com.euro-quote.widget.plist
```

### Stop the Widget
```bash
launchctl unload ~/Library/LaunchAgents/com.euro-quote.widget.plist
```

### Disable Autostart
```bash
rm ~/Library/LaunchAgents/com.euro-quote.widget.plist
```

### Check Widget Status
```bash
launchctl list | grep euro-quote
```

### View Error Logs
```bash
cat /tmp/euro-quote.widget.err
```

## Manual Start
To run the widget manually without the launch agent:
```bash
python3 widget.py
```

## Troubleshooting

If you encounter any issues:
1. Check the error log at `/tmp/euro-quote.widget.err`
2. Ensure all dependencies are correctly installed
3. Try stopping and restarting the widget using the commands above
