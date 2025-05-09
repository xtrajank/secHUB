'''
API wrapper for pulling data from FireMon. Forms and sends the HTTP requests. Returns JSONified data.

TODO: This is an example assuming how the endpoints are defined. An updated example would have the real paths to the data.

Features:
    - Get firewall data
    - Get changes made to firewall
    - Get policy violation reports
'''
from backend.app.internal_api.InternalAPIClient import InternalAPIClient as IAPIC
from backend.app.config import INTERNAL_API_BASE, INTERNAL_API_KEY

firemon_api = IAPIC(INTERNAL_API_BASE, INTERNAL_API_KEY)

async def fetch_firewall_data():
    '''
    Get firewall base data.

    ie. rule ID, name, description, source/destination IPs, ports/protocols, action, rule hit count, rule last date hit, rule status
    '''
    return await firemon_api.get("/firewall")

async def fetch_firewall_changes():
    '''
    Get changes made to firewall.

    ie. who made change, what change, when, approval status
    '''
    return await firemon_api.get("/firewall/changes")
    
async def fetch_firewall_violations():
    '''
    Get policy violation reports

    ie. rule violations, security gaps, risk scoring
    '''
    return await firemon_api.get("/firewall/violations")