#!/bin/bash

echo "Installing Python dependencies..."
pip3 install -r requirements.txt

echo "Creating Launch Agents directory if it doesn't exist..."
mkdir -p ~/Library/LaunchAgents

echo "Installing Launch Agent..."
cp com.euro-quote.widget.plist ~/Library/LaunchAgents/

echo "Loading Launch Agent..."
launchctl load ~/Library/LaunchAgents/com.euro-quote.widget.plist

echo "Setup complete! The widget should now start automatically when you log in."
echo "To start it now without restarting, run: python3 widget.py" 