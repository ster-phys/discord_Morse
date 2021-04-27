#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Load .env and apply to environment variables
"""

from dotenv import load_dotenv
load_dotenv()

import os
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
