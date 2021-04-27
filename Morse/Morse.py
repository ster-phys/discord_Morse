#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

ROOTPATH = os.path.dirname(os.path.abspath(__file__))

import json

import discord
import pykakasi
from pydub import AudioSegment

class Morse:
    def __init__(self,ctx,arg):
        self._ctx = ctx
        try:
            self._arg = arg.split()[0]
        except:
            self._arg = arg
        self._morse = ""
        self._path = "/tmp/{}.wav".format(ctx.author.id)
        self._assetsPath = "{}/assets/".format(ROOTPATH)
        self._sound = {
            "1": AudioSegment.from_file("{}1.wav".format(self._assetsPath), format="wav"),
            "3": AudioSegment.from_file("{}3.wav".format(self._assetsPath), format="wav"),
            "_": AudioSegment.from_file("{}_.wav".format(self._assetsPath), format="wav")
        }

    def _genMorse(self):
        """
        `self._arg` -> `self._morse`
        """
        # kanji -> iroha
        hiraStr = ""
        kks = pykakasi.kakasi()
        for elm in kks.convert(self._arg):
            hiraStr += elm["hira"]

        # e.g. が -> か + ゛
        with open(self._assetsPath + "trans.json", 'r') as f:
            trans = json.load(f)
        hiraStr = hiraStr.translate(str.maketrans(trans))

        # alphabet -> （alphabet）
        reHiraStr = ""
        alphaList = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        for ch in hiraStr:
            reHiraStr += ch if not ch in alphaList else ("（"+ ch +"）")
        reHiraStr = reHiraStr.replace("）（","")
        reHiraStr = '#'.join(reHiraStr) + '#'

        # normal string -> Morse
        trans = {}
        for kind in ["iroha","number","symbol","alphabet"]:
            with open("{}{}.json".format(self._assetsPath,kind), 'r') as f:
                trans.update(json.load(f))

        self._morse = reHiraStr.translate(str.maketrans(trans))

        return

    def _convertWAV(self):
        """
        `self._morse` -> wav save to `self._path`
        """
        sound = self._sound["_"]
        for ch in self._morse:
            if ch in "13_":
                sound += self._sound[ch]

        sound.export(self._path, format="wav")
        return

    def _sendMorse(self):
        """
        play wav @`self._path`
        """
        audioSource = discord.FFmpegPCMAudio(self._path)
        voiceClient = self._ctx.guild.voice_client
        voiceClient.play(audioSource)
        return

    async def main(self):
        if self._arg == "":
            await self._ctx.send("Need the string to be converted to Morse code.")
            return

        # arg to Morse string
        self._genMorse()
        # Morse string to wav and save
        self._convertWAV()
        # play wav
        self._sendMorse()

        return
