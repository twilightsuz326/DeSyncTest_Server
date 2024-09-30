# DeSyncTest_Server

## Description
This repository provides a Docker-based environment for testing **Client-side Desync attacks**.   
It uses a simple HTTP server built with Python and HAProxy to recreate scenarios where desynchronization occurs in requests.   
The setup allows you to use Burp Suite to test and simulate such attacks.  

## Setup
```
git clone https://github.com/twilightsuz326/DeSyncTest_Server.git
cd DeSyncTest_Server
docker-compose up
```

## Site
[Client-side desync 検証環境を作成し、BurpSuiteでテストしてみる](https://tetrislove.com/burp-desynctest/)

