"""CRUD for EmailVerifier / DomainSearch / EmailFinder.

One (RunHunter) interface for processing different classes is implemented.
Fixing the following requirements is not appropriate as it unnecessarily increases the amount of code.
Also, these requirements do not affect the code itself.
classes.py:57:20 / 105:20 / 153:20: P103 other string does contain unindexed parameters
classes.py:57:20 / 105:20 / 153:20 / 211:30: WPS305 Found `f` string
classes.py:87:12 / 135:12 / 185:12: WPS332 Found walrus operator
classes.py:159:9: WPS221 Found line with high Jones Complexity: 15 > 14
"""

import time
from abc import ABC, abstractmethod

import requests


class Interface(ABC):
    """Abstract base class for creating, reading, updating, and deleting data."""

    # Constants for HTTP status codes
    status_accepted = 200
    api_call_again = 202
    status_retry_later = 222
    status_bad_request = 400
    status_too_many_requests = 429
    prohibition_to_process = 451
    # Error messages
    error222 = {'error': 'make try later'}
    error400 = {'error': 'invalid email or wrong params'}
    error429 = {'error': 'too_many requests'}
    error451 = {'error': 'prohibition of personal data processing'}

    @abstractmethod
    def create(self, incoming_data):
        """Abstract method for creating data."""
        raise NotImplementedError("Method 'create' must be implemented in subclass.")

    @abstractmethod
    def read(self, incoming_data):
        """Abstract method for reading data."""
        raise NotImplementedError("Method 'read' must be implemented in subclass.")

    @abstractmethod
    def update(self, old_data, new_data):
        """Abstract method for updating data."""
        raise NotImplementedError("Method 'update' must be implemented in subclass.")

    @abstractmethod
    def delete(self, incoming_data):
        """Abstract method for deleting data."""
        raise NotImplementedError("Method 'delete' must be implemented in subclass.")


class EmailVerifier(Interface):
    """Class for verifying email addresses using the Hunter API."""

    __slots__ = ('url', 'api_key', 'json_data')

    def __init__(self, apikey):
        """Initialize the EmailVerifier instance with the provided API key."""
        self.api_key = apikey
        self.url = f'https://api.hunter.io/v2/email-verifier?email={{}}&api_key={self.api_key}'
        self.json_data = {}

    def create(self, email):
        """Verify the provided email address."""
        while True:
            response = requests.get(self.url.format(email), timeout=5)
            if response.status_code == self.api_call_again:
                return False
            break
        if response.status_code == self.status_retry_later:
            time.sleep(5)
            response = requests.get(self.url.format(email), timeout=5)
            if response.status_code == self.status_retry_later:
                return self.error222
        if response.status_code == self.status_bad_request:
            return self.error400
        if response.status_code == self.status_too_many_requests:
            return self.error429
        if response.status_code == self.prohibition_to_process:
            return self.error451
        if response.status_code == self.status_accepted:
            self.json_data[email] = response.json()

    def read(self, email):
        """Retrieve information about a verified email address."""
        return self.json_data[email]

    def update(self, old_email, new_email):
        """Update the verification for an email address."""
        if error_msg := self.create(new_email):
            return error_msg
        else:
            self.json_data.pop(old_email, None)

    def delete(self, email):
        """Remove a verified email address from the stored data."""
        self.json_data.pop(email, None)


class DomainSearch(Interface):
    """Class for domain search using the Hunter API."""

    __slots__ = ('url', 'api_key', 'json_data')

    def __init__(self, apikey):
        """Initialize the DomainSearch instance with the provided API key."""
        self.api_key = apikey
        self.url = f'https://api.hunter.io/v2/domain-search?domain={{}}&api_key={self.api_key}'
        self.json_data = {}

    def create(self, domain):
        """Search the provided domain."""
        while True:
            response = requests.get(self.url.format(domain), timeout=5)
            if response.status_code == self.api_call_again:
                return False
            break
        if response.status_code == self.status_retry_later:
            time.sleep(5)
            response = requests.get(self.url.format(domain), timeout=5)
            if response.status_code == self.status_retry_later:
                return self.error222
        if response.status_code == self.status_bad_request:
            return self.error400
        if response.status_code == self.status_too_many_requests:
            return self.error429
        if response.status_code == self.prohibition_to_process:
            return self.error451
        if response.status_code == self.status_accepted:
            self.json_data[domain] = response.json()

    def read(self, domain):
        """Retrieve information about domain."""
        return self.json_data[domain]

    def update(self, old_domain, new_domain):
        """Refresh domain search."""
        if error_msg := self.create(new_domain):
            return error_msg
        else:
            self.json_data.pop(old_domain, None)

    def delete(self, domain):
        """Remove a domain from the stored data."""
        self.json_data.pop(domain, None)


class EmailFinder(Interface):
    """Class for email search using the Hunter API."""

    __slots__ = ('url', 'api_key', 'json_data')

    def __init__(self, apikey):
        """Initialize the EmailFinder instance with the provided API key."""
        self.api_key = apikey
        self.url = (f'https://api.hunter.io/v2email-finder?domain={{}}'
                    f'&first_name={{}}&last_name={{}}&api_key={self.api_key}')
        self.json_data = {}

    def create(self, incoming_data):
        """Search the provided email."""
        parts = incoming_data.split('&')
        formed_url = self.url.format(parts[0], parts[1], parts[2])
        while True:
            response = requests.get(formed_url, timeout=5)
            if response.status_code == self.api_call_again:
                return False
            break
        if response.status_code == self.status_retry_later:
            time.sleep(5)
            response = requests.get(formed_url, timeout=5)
            if response.status_code == self.status_retry_later:
                return self.error222
        if response.status_code == self.status_bad_request:
            return self.error400
        if response.status_code == self.status_too_many_requests:
            return self.error429
        if response.status_code == self.prohibition_to_process:
            return self.error451
        if response.status_code == self.status_accepted:
            self.json_data[incoming_data] = response.json()

    def read(self, incoming_data):
        """Retrieve information about email."""
        return self.json_data[incoming_data]

    def update(self, old_data, new_data):
        """Refresh email search."""
        if error_msg := self.create(new_data):
            return error_msg
        else:
            self.json_data.pop(old_data, None)

    def delete(self, incoming_data):
        """Remove email from the stored data."""
        self.json_data.pop(incoming_data, None)


class HunterClient(object):
    """Interface to run EmailVerifier / DomainSearch / EmailFinder."""

    __slots__ = ('instance',)

    usage_class = {
        'email_finder': EmailFinder,
        'email_verifier': EmailVerifier,
        'domain_search': DomainSearch,
    }

    def __init__(self, service_type, apikey):
        """Initialize the RunHunter instance with the provided API key and Service type."""
        if service_type in self.usage_class:
            self.instance = self.usage_class.get(service_type)(apikey)
        else:
            raise ValueError(f'Unsupported service: {service_type}')

