*** Settings ***
Resource  resource.robot
Resource  login_resource.robot
Suite Setup     Open And Configure Browser
Suite Teardown  Close Browser
Test Setup      Reset Application Create User And Go To Register Page


*** Test Cases ***
Register With Valid Username And Password
    Set Username  testi
    Set Password  testi123
    Set Password confirmation  testi123
    Submit Register Credentials
    Register Should Succeed

Register With Too Short Username And Valid Password
    Set Username  xx
    Set Password  testi123
    Set Password confirmation  testi123
    Submit Register Credentials
    Register Should Fail With Message  Username must be at least 3 characters long

Register With Valid Username And Too Short Password
    Set Username  testi
    Set Password  xx
    Set Password confirmation  xx
    Submit Register Credentials
    Register Should Fail With Message  Password must be at least 8 characters long

Register With Valid Username And Invalid Password
    Set Username  testi
    Set Password  testitesti
    Set Password confirmation  testitesti
    Submit Register Credentials
    Register Should Fail With Message  Invalid password

Register With Nonmatching Password And Password Confirmation
    Set Username  testi
    Set Password  testitesti1
    Set Password confirmation  testitesti2
    Submit Register Credentials
    Register Should Fail With Message  Passwords do not match

Register With Username That Is Already In Use
    Set Username  kalle
    Set Password  testi123
    Set Password confirmation  testi123
    Submit Register Credentials
    Register Should Fail With Message  User with username kalle already exists

Login After Successful Registration
    Set Username  testi
    Set Password  testi123
    Set Password confirmation  testi123
    Submit Register Credentials
    Go To Login Page
    Set Username  testi
    Set Password  testi123
    Submit Login Credentials
    Login Should Succeed

Login After Failed Registration
    Set Username  xx
    Set Password  testi123
    Set Password confirmation  testi123
    Submit Register Credentials
    Register Should Fail With Message  Username must be at least 3 characters long
    Go To Login Page
    Set Username  xx
    Set Password  testi123
    Submit Login Credentials
    Login Should Fail With Message  Invalid username or password


*** Keywords ***
Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Text  password  ${password}

Set Password confirmation
    [Arguments]  ${password_confirmation}
    Input Text  password_confirmation  ${password_confirmation}

Submit Register Credentials
    Click Button  Register

Reset Application Create User And Go To Register Page
    Reset Application
    Create User  kalle  kalle123
    Go To Register Page

Register Should Succeed
    Welcome Page Should Be Open

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}