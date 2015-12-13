# datacap
A simple Flask server that runs locally to check current data cap of Internet.

## Running

- Make sure to have Flask, Request, and Python 2.7 installed.
- Run with `./start`

This server will run on port `8080` locally and is configured with the normal Raspian settings.

## Updating

To update the internet cap, running `./update cap` will prompt for the current limit. This script can run on other machines as the webserver has a `/update` HTTP POST request URL that updates it.


