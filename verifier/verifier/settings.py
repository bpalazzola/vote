import logging
import os
# Configuration
API_URL = 'http://nathanhourt.com:3001/rpc'
API_USER = 'bob'
API_PASS = 'bob'
DEBUG = True
SECRET_KEY = 'development_key'
SITE_NAME = 'Follow My Vote - ID Verification'
COMPANY_NAME = 'Follow My Vote'
LOG_LEVEL_FILE = logging.ERROR
LOG_LEVEL_CONSOLE = logging.DEBUG
APP_ROOT = os.path.dirname(os.path.abspath(__file__))  # refers to application_top
APP_LOGS = os.path.join(APP_ROOT, 'logs')
APP_CACHE = os.path.join(APP_ROOT, 'cache')
APP_STATIC = os.path.join(APP_ROOT, 'static')
APP_DATA = os.path.join(APP_ROOT, 'data')
DB_CONNECTION_STRING = 'sqlite:///{0}'.format(os.path.join(APP_DATA, 'voter.db'))
DB_TEST_CONNECTION_STRING = 'sqlite:///{0}'.format(os.path.join(APP_DATA, 'sample_voter.db'))

WALLET_PASSWORD = 'helloworld'
WALLET_NAME = 'default'

#Major.Minor.Revision.Build, this number is going to be appended as a query string to css and javascript as well
#to make it so that we can force users to download changes
VERSION = '1.0.0.3'

APP_SAMPLE_IMAGES = os.path.join(APP_STATIC, 'content', 'images', 'sample')

STATES = [
    ('', 'Select State...'),
    ('AL', 'Alabama'),
    ('AK', 'Alaska'),
    ('AS', 'American Samoa'),
    ('AZ', 'Arizona'),
    ('AR', 'Arkansas'),
    ('AE', 'Armed Forces Africa'),
    ('AA', 'Armed Forces Americas'),
    ('AE', 'Armed Forces Canada'),
    ('AE', 'Armed Forces Europe'),
    ('AE', 'Armed Forces Middle East'),
    ('AP', 'Armed Forces Pacific'),
    ('CA', 'California'),
    ('CO', 'Colorado'),
    ('CT', 'Connecticut'),
    ('DE', 'Delaware'),
    ('DC', 'District Of Columbia'),
    ('FM', 'Federated States Of Micronesia'),
    ('FL', 'Florida'),
    ('GA', 'Georgia'),
    ('GU', 'Guam'),
    ('HI', 'Hawaii'),
    ('ID', 'Idaho'),
    ('IL', 'Illinois'),
    ('IN', 'Indiana'),
    ('IA', 'Iowa'),
    ('KS', 'Kansas'),
    ('KY', 'Kentucky'),
    ('LA', 'Louisiana'),
    ('ME', 'Maine'),
    ('MH', 'Marshall Islands'),
    ('MD', 'Maryland'),
    ('MA', 'Massachusetts'),
    ('MI', 'Michigan'),
    ('MN', 'Minnesota'),
    ('MS', 'Mississippi'),
    ('MO', 'Missouri'),
    ('MT', 'Montana'),
    ('NE', 'Nebraska'),
    ('NV', 'Nevada'),
    ('NH', 'New Hampshire'),
    ('NJ', 'New Jersey'),
    ('NM', 'New Mexico'),
    ('NY', 'New York'),
    ('NC', 'North Carolina'),
    ('ND', 'North Dakota'),
    ('MP', 'Northern Mariana Islands'),
    ('OH', 'Ohio'),
    ('OK', 'Oklahoma'),
    ('OR', 'Oregon'),
    ('PW', 'Palau'),
    ('PA', 'Pennsylvania'),
    ('PR', 'Puerto Rico'),
    ('RI', 'Rhode Island'),
    ('SC', 'South Carolina'),
    ('SD', 'South Dakota'),
    ('TN', 'Tennessee'),
    ('TX', 'Texas'),
    ('UT', 'Utah'),
    ('VT', 'Vermont'),
    ('VI', 'Virgin Islands'),
    ('VA', 'Virginia'),
    ('WA', 'Washington'),
    ('WV', 'West Virginia'),
    ('WI', 'Wisconsin'),
    ('WY', 'Wyoming')]

REJECTION_REASONS = [
    ('', 'Select or enter rejection reason...'),
    ('Registration Not Found', 'Registration Not Found'),
    ('ID not legible', 'ID not legible'),
    ('Photos do not match', 'Photos do not match'),
    ('Expired ID', 'Expired ID')]

