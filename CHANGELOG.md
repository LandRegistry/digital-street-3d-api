# Changelog

Note that requirements updates are not listed here unless they result in more changes than just updating the version number.

|Date|Summary|Comparison to previous|
|---|---|---|
|2019-01-24| Improve exception handling, support github common-dev-env, fix logging with Flask 1.0 | [Here](http://git.dev.ctp.local/skeletons/digital-street-3d-api/commit/013cd44f28611567f9e826055f92153a727f9310)|
|2018-03-08|Add configurable default timeout to g.requests so that http requests aren't allowed to hang indefintely | [Here](http://git.dev.ctp.local/skeletons/digital-street-3d-api/merge_requests/29) |
|2018-04-10|Fix `make unittest` command so that it only runs tests in the unit_test folder instead of integration tests as well | [Here](http://git.dev.ctp.local/skeletons/digital-street-3d-api/merge_requests/26) |
|2018-01-09|Change ApplicationError handling to allow non-500 errors to be logged at info instead of debug if required, and return stack trace in JSON if Flask log level is DEBUG| [Here](http://git.dev.ctp.local/skeletons/digital-street-3d-api/compare/ce36d29d6c66db44d3a8f0f9a2ee73fb93917088...a8f55194d85ca644f267b06b17a83c2f564bdabd)|
|2017-11-09|Change base flask iamge to v4| [Here](http://git.dev.ctp.local/skeletons/digital-street-3d-api/commit/ec3d9b371a32f3ad87619acf9d4859fe43a18727)|
|2017-09-15|Change requirements to be generated by pip-compile via requirements.in| [Here](http://git.dev.ctp.local/skeletons/digital-street-3d-api/commit/18d5f14dad5049f327e038ad97e28aed8735ab5e)|
|2017-06-30|Move logging and traceid code into an app-agnostic custom extension| [Here](http://git.dev.ctp.local/skeletons/digital-street-3d-api/compare/2d29ed8508015262822597856ad582df819b1832...ddf0e6d2b2e8060fd0460521e427e7d853a7d8be)|
|2017-04-20|BugFix: Exception responses now return `application/json` mimetype.| [Here](http://git.dev.ctp.local/skeletons/digital-street-3d-api/commit/244abe82bfa89a4864e1f1000181da32e0ea38be)|
|2017-04-11|BugFix: Cascading health route updated to no longer always return a status of OK.| [Here](http://git.dev.ctp.local/skeletons/digital-street-3d-api/compare/fb43404b39a843fa0ae4c49efb51716178cf7cf4...7744e96b4b8250fbf0f9609b4a9923154dd852c3) |
|2017-04-07|Dockerfile updated to use base Flask image version 3| [Here](http://git.dev.ctp.local/skeletons/digital-street-3d-api/commit/40754a1825169d2f2c3f534c79bd4afe82dbe8d5) |
|2017-04-07|Improved database cascade health check code| [Here](http://git.dev.ctp.local/skeletons/digital-street-3d-api/commit/bbec454542c27aabe55084abb98a65b6c7b17897) |
|2017-03-14|Added code and config for Cascading Health route| [Here](http://git.dev.ctp.local/skeletons/digital-street-3d-api/commit/5915ed4be42b93d1e8998a54626c632741c5dad7)|
