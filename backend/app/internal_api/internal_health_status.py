'''
API wrapper for pulling data from internal system's health status reports.

TODO: This is an example assuming how the endpoints are defined. An updated example would have the real paths to the data.

Features:
    - Pull data of system health metrics
    - Pull service status
    - Pull network health data
    - Pull security and compliance checks
'''
from backend.app.internal_api.InternalAPIClient import InternalAPIClient as IAPIC
from backend.app.config import INTERNAL_API_BASE, INTERNAL_API_KEY

health_status_api = IAPIC(INTERNAL_API_BASE, INTERNAL_API_KEY)

async def fetch_health_data():
    '''
    Pull data of system health metrics.

    ie. CPU usage, memory usage, disk usage, uptime, system load avgs
    '''
    return await health_status_api.get("/health")

async def fetch_service_data():
    '''
    Pull service status.

    ie. Running/stopped states, response times, restart counts, ping checks
    '''
    return await health_status_api.get("/health/service")

async def fetch_network_data():
    '''
    Pull network health data

    ie. latency, packet loss, bandwidth usage, open/closed ports, DNS resolution times
    '''
    return await health_status_api.get("health/network")

async def fetch_security_data():
    '''
    Pull security and compliance checks

    ie. antivirus status, firewall status, open vulnerabilities, certificate expirations
    '''
    return await health_status_api.get("health/security")