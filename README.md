# datacap
A simple Flask server that runs locally to check current data cap of Internet.

## Running

- Make sure to have Flask, Request, and Python 2.7 installed.
- Run with `./start`
- Start the datacap server with a cap amount by connecting with: `http://datacaphostname/update?cap=0`

This server will run on port `8080` locally and is configured with the normal Raspian settings.

## Updating

`host.com/update?cap=<value>` - Updates the cap and redirects to the homepage.


