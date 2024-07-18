#!/usr/bin/env python3
"""
web cache and tracker
"""
import requests
import redis
from functools import wraps

# Initialize Redis connection
store = redis.Redis()


def count_url_access(method):
    """ Decorator counting how many times
    a URL is accessed """
    @wraps(method)
    def wrapper(url):
        cached_key = "cached:" + url
        cached_data = store.get(cached_key)
        if cached_data:
            print(f"Cache hit for {url}")
            return cached_data.decode("utf-8")

        count_key = "count:" + url
        html = method(url)

        # Increment the access count and cache the HTML content
        store.incr(count_key)
        store.set(cached_key, html)
        store.expire(cached_key, 10)  # Cache expires after 10 seconds
        print(f"Cache miss for {url}. Fetching from the web.")
        return html
    return wrapper


@count_url_access
def get_page(url: str) -> str:
    """ Returns HTML content of a url """
    res = requests.get(url)
    return res.text


# Example usage
if __name__ == "__main__":
    test_url = ("http://slowwly.robertomurray.co.uk/delay/5000/"
                "url/http://www.google.com")
    print(get_page(test_url))
    print(get_page(test_url))
    print(get_page(test_url))
