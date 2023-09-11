# weather-scheduler

## Overview

This Python script allows you to receive daily weather reports via text messages. It uses the Twilio API to send SMS messages to your phone with the current weather conditions for your specified location.

I got the inspiration for this very short project after watching a TikTok video (by user @tech_sis8) as it looked like a beginner-friendly project that I can up-scale at a later date when I want to get into tools that use CRON scheduling or SMS messaging.

## Prerequisites

Before running the script, you need to:

- Install any dependancies by running:

```
pip3 install schedule
pip3 install python-dotenv
pip3 install requests
```

- Create a .env file and insert your Twilio credentials
- If needed, change the longitude and latitude to wherever you want the weather data for
