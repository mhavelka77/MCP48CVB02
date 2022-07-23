# Controlling MCP48CVB02 DAC with Raspberry Pi and Python

This repository contains working examples of controlling a MCP48CXBXX DAC through SPI interface on Raspberry Pi. 

## Prerequisites

- Python3 running on Raspberry Pi
- DAC connected to the SPI1 interface

## Usage

setup the DACs:
```
python3 dac_setup.py
```

set value to DAC
```
python3 dac.py [dac_number] [internal_dac_number] [value]
```
