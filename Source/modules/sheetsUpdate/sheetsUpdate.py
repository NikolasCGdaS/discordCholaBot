import discord
from discord.ext import commands
import json
import gspread
from oauth2client.service_account import ServiceAccountCredentials

serviceID = 
servicePassword =
spreadsheetName =

class SheetsUpdate:

    def __init__(self, spreadsheetName, credentialFile='')