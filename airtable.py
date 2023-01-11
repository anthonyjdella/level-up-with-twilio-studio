import os

from pyairtable import Table
from dotenv import load_dotenv


load_dotenv()

# Connect to Airtable
table = Table(
    os.getenv('AIRTABLE_API_KEY'),
    os.getenv('AIRTABLE_BASE_ID'),
    os.getenv('AIRTABLE_TABLE_ID')
)


# Get all unique phone numbers in Airtable
def get_unique_numbers():
    unique_numbers = set(record.get('fields').get('Phone Number') for record in table.all())
    return unique_numbers


# Get names and phone numbers from Airtable
def get_names_numbers():
    team = dict()

    for record in table.all():
        team_member_name = record.get('fields').get('Name')
        team_member_number = record.get('fields').get('Phone Number')
        team[team_member_number] = team_member_name
    return team


# print(get_unique_numbers())
# > {'+1XXXXXXXXXX', '+1XXXXXXXXXX'}
