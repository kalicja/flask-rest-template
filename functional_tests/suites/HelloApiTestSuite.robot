*** Settings ***
Documentation     A test suite for /hello rest endpoint
...
Library           ../lib/HelloApiLib.py


*** Test Cases ***
Get all posted hello, when there is no hellos
    Service is running on       ${HOST_URL}
    There was no posted hellos
    Requesting all hello
    Result is empty list

Add and retrieve hello
    Service is running on       ${HOST_URL}
    There was no posted hellos
    add hello    greeting to all     from space
    get hello with id   1
    result is    greeting to all     from space