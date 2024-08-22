# MTA API Documentation
My documentation of the MTA API. Currently only supports the subway lines (I'll get to the other services!)

## DISCLAIMER (Important)
This is **not** a documentation of their official developer API. Rather, this API documentation was made from reverse-engineering their website. That being said, I don't even know if I'm allowed to do this but **please don't sue me!**

## Table of Contents
1. [Logos](#logos)
2. [Routes](#routes)
3. [Stops](#stops)

## Logos
| Name     | Rendered SVG                                                                                       | Link                                                                                                         |
|----------|-----------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------|
| MTA Logo | ![MTA Logo](https://new.mta.info/themes/custom/bootstrap_mta/favicon.ico)                           | [Link](https://new.mta.info/themes/custom/bootstrap_mta/favicon.ico)                                          |
| 1        | ![1](https://new.mta.info/themes/custom/bootstrap_mta/js/apps/f615303877866360408d22d028c7e1d2.svg) | [Link](https://new.mta.info/themes/custom/bootstrap_mta/js/apps/f615303877866360408d22d028c7e1d2.svg)         |
| 2        | ![2](https://new.mta.info/themes/custom/bootstrap_mta/js/apps/12b76417962028dc5dd46a5f7da4e257.svg) | [Link](https://new.mta.info/themes/custom/bootstrap_mta/js/apps/12b76417962028dc5dd46a5f7da4e257.svg)         |
| 3        | ![3](https://new.mta.info/themes/custom/bootstrap_mta/js/apps/a78ac9d7ebbb00594f70070c3867e8d5.svg) | [Link](https://new.mta.info/themes/custom/bootstrap_mta/js/apps/a78ac9d7ebbb00594f70070c3867e8d5.svg)         |
| 4        | ![4](https://new.mta.info/themes/custom/bootstrap_mta/js/apps/085719a34ab709a927f368bf0e764777.svg) | [Link](https://new.mta.info/themes/custom/bootstrap_mta/js/apps/085719a34ab709a927f368bf0e764777.svg)         |
| 5        | ![5](https://new.mta.info/themes/custom/bootstrap_mta/js/apps/b370f0e0c62c4b8f36b928178df6b4ae.svg) | [Link](https://new.mta.info/themes/custom/bootstrap_mta/js/apps/b370f0e0c62c4b8f36b928178df6b4ae.svg)         |
| 6        | ![6](https://new.mta.info/themes/custom/bootstrap_mta/js/apps/af9ae1b0bcfd30bc6c3626dae98074ef.svg) | [Link](https://new.mta.info/themes/custom/bootstrap_mta/js/apps/af9ae1b0bcfd30bc6c3626dae98074ef.svg)         |
| 7        | ![7](https://new.mta.info/themes/custom/bootstrap_mta/js/apps/903c05438d54ff7a5d0036a769f10bf6.svg) | [Link](https://new.mta.info/themes/custom/bootstrap_mta/js/apps/903c05438d54ff7a5d0036a769f10bf6.svg)         |
| A        | ![A](https://new.mta.info/themes/custom/bootstrap_mta/js/apps/9041d815e07d7dd93ebaa6bd466b6b67.svg) | [Link](https://new.mta.info/themes/custom/bootstrap_mta/js/apps/9041d815e07d7dd93ebaa6bd466b6b67.svg)         |
| C        | ![C](https://new.mta.info/themes/custom/bootstrap_mta/js/apps/ec805c7415caff62cc2641469574683c.svg) | [Link](https://new.mta.info/themes/custom/bootstrap_mta/js/apps/ec805c7415caff62cc2641469574683c.svg)         |
| E        | ![E](https://new.mta.info/themes/custom/bootstrap_mta/js/apps/5500549a75e2a20cfc18d6f87babfe40.svg) | [Link](https://new.mta.info/themes/custom/bootstrap_mta/js/apps/5500549a75e2a20cfc18d6f87babfe40.svg)         |
| B        | ![B](https://new.mta.info/themes/custom/bootstrap_mta/js/apps/9156f755686e8e6b2935f07a393b611a.svg) | [Link](https://new.mta.info/themes/custom/bootstrap_mta/js/apps/9156f755686e8e6b2935f07a393b611a.svg)         |
| D        | ![D](https://new.mta.info/themes/custom/bootstrap_mta/js/apps/84bc409ef98ce69f9d36e9b2556ab7cf.svg) | [Link](https://new.mta.info/themes/custom/bootstrap_mta/js/apps/84bc409ef98ce69f9d36e9b2556ab7cf.svg)         |
| F        | ![F](https://new.mta.info/themes/custom/bootstrap_mta/js/apps/5b35921d073d41d80deeb17cac90d7fd.svg) | [Link](https://new.mta.info/themes/custom/bootstrap_mta/js/apps/5b35921d073d41d80deeb17cac90d7fd.svg)         |
| M        | ![M](https://new.mta.info/themes/custom/bootstrap_mta/js/apps/0e9163c71c7f9397f7d3e36d51546849.svg) | [Link](https://new.mta.info/themes/custom/bootstrap_mta/js/apps/0e9163c71c7f9397f7d3e36d51546849.svg)         |
| G        | ![G](https://new.mta.info/themes/custom/bootstrap_mta/js/apps/8f8f3abaabc85122841fe5df41fbc344.svg) | [Link](https://new.mta.info/themes/custom/bootstrap_mta/js/apps/8f8f3abaabc85122841fe5df41fbc344.svg)         |
| J        | ![J](https://new.mta.info/themes/custom/bootstrap_mta/js/apps/bca69e5237ed3e7d0d78320261f99f2d.svg) | [Link](https://new.mta.info/themes/custom/bootstrap_mta/js/apps/bca69e5237ed3e7d0d78320261f99f2d.svg)         |
| Z        | ![Z](https://new.mta.info/themes/custom/bootstrap_mta/js/apps/3f0bb849f47ead835e0241104f337a6d.svg) | [Link](https://new.mta.info/themes/custom/bootstrap_mta/js/apps/3f0bb849f47ead835e0241104f337a6d.svg)         |
| L        | ![L](https://new.mta.info/themes/custom/bootstrap_mta/js/apps/8c1bfa6816b539fd63ca8f26e4dc8b65.svg) | [Link](https://new.mta.info/themes/custom/bootstrap_mta/js/apps/8c1bfa6816b539fd63ca8f26e4dc8b65.svg)         |
| N        | ![N](https://new.mta.info/themes/custom/bootstrap_mta/js/apps/4a1b0077917e37bf08502f6ec21b04c8.svg) | [Link](https://new.mta.info/themes/custom/bootstrap_mta/js/apps/4a1b0077917e37bf08502f6ec21b04c8.svg)         |
| Q        | ![Q](https://new.mta.info/themes/custom/bootstrap_mta/js/apps/b746451c38ae7d57f8a4d0b72b369328.svg) | [Link](https://new.mta.info/themes/custom/bootstrap_mta/js/apps/b746451c38ae7d57f8a4d0b72b369328.svg)         |
| R        | ![R](https://new.mta.info/themes/custom/bootstrap_mta/js/apps/9c6333dc2424c01e4740f5c3c56d362f.svg) | [Link](https://new.mta.info/themes/custom/bootstrap_mta/js/apps/9c6333dc2424c01e4740f5c3c56d362f.svg)         |
| W        | ![W](https://new.mta.info/themes/custom/bootstrap_mta/js/apps/566ed247e9487d43c1f1cc7e8ea5f456.svg) | [Link](https://new.mta.info/themes/custom/bootstrap_mta/js/apps/566ed247e9487d43c1f1cc7e8ea5f456.svg)         |
| S        | ![S](https://new.mta.info/themes/custom/bootstrap_mta/js/apps/da91e0c35571668af52eb6164a71f33e.svg) | [Link](https://new.mta.info/themes/custom/bootstrap_mta/js/apps/da91e0c35571668af52eb6164a71f33e.svg)         |
| SR       | ![SR](https://new.mta.info/themes/custom/bootstrap_mta/js/apps/ee2e30facb9a6c4b8bf0c43e531a36ab.svg) | [Link](https://new.mta.info/themes/custom/bootstrap_mta/js/apps/ee2e30facb9a6c4b8bf0c43e531a36ab.svg)         |
| SF       | ![SF](https://new.mta.info/themes/custom/bootstrap_mta/js/apps/c01e0840361272a0585e94a540d6755f.svg) | [Link](https://new.mta.info/themes/custom/bootstrap_mta/js/apps/c01e0840361272a0585e94a540d6755f.svg)         |
| SIR      | ![SIR](https://new.mta.info/themes/custom/bootstrap_mta/js/apps/ab18baf2d2d8ea7f1902ce1751d5fdf2.svg) | [Link](https://new.mta.info/themes/custom/bootstrap_mta/js/apps/ab18baf2d2d8ea7f1902ce1751d5fdf2.svg)         |

## Routes
To get the routes of a subway line, you have to send a GET request to:
```
https://collector-otp-prod.camsys-apps.com/schedule/MTASBWY/stopsForRoute?apikey=qeqy84JE7hUKfaI0Lxm2Ttcm6ZA0bYrP&&routeId={route_id}
```
where `route_id` is the route ID of the subway line.

For most of the subway lines, the ID will be `MTASBWY:{line}` where `line` is the subway line.

For example, the route ID for the ![1](https://new.mta.info/themes/custom/bootstrap_mta/js/apps/f615303877866360408d22d028c7e1d2.svg) train is `MTASBWY:1`, and the API URL will be `https://collector-otp-prod.camsys-apps.com/schedule/MTASBWY/stopsForRoute?apikey=qeqy84JE7hUKfaI0Lxm2Ttcm6ZA0bYrP&&routeId=MTASBWY:1`.

The only exceptions to this are the shuttle trains and the Staten Island railroad. The route IDs for them are:
- ![S](https://new.mta.info/themes/custom/bootstrap_mta/js/apps/da91e0c35571668af52eb6164a71f33e.svg) : `MTASBWY:GS`
- ![SR](https://new.mta.info/themes/custom/bootstrap_mta/js/apps/ee2e30facb9a6c4b8bf0c43e531a36ab.svg) : `MTASBWY:H`
- ![SF](https://new.mta.info/themes/custom/bootstrap_mta/js/apps/c01e0840361272a0585e94a540d6755f.svg) : `MTASBWY:FS`
- ![SIR](https://new.mta.info/themes/custom/bootstrap_mta/js/apps/ab18baf2d2d8ea7f1902ce1751d5fdf2.svg) : `MTASBWY:SI`

I included a table at the end of this section containing all the route IDs and their respective API URLs.

Calling this endpoint will return a array of dictionaries as a response in this format:
```json
[
    {
        "stopSequence": "",
        "routeId": "",
        "notes": "",
        "stopId": "",
        "stopType": "",
        "stopStatus": "",
        "borough": "",
        "stopName": "",
        "ada": ""
    },
    ... // more stops
]
```

If the array is empty, then that means the route ID/URL is invalid.

| Field         | Explanation                                                                                                                                                                                                                           | Example        |
|---------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|----------------|
| `stopSequence` | The stop position.                                                                                                                                                                                                                     | `"1"`          |
| `routeId`      | The route ID.                                                                                                                                                                                                                          | `"MTASBWY:4"`  |
| `notes`        | The notes about this stop. So far, no notes have been found for any stops.                                                                                                                                                             | `""`           |
| `stopId`       | The stop ID.                                                                                                                                                                                                                           | `"MTASBWY:401"` |
| `stopType`     | The stop type, used for checking how the requested train is being serviced at this stop/station. <br> Possible values are `"0"`, `"1"`, `"2"`, `"3"`. <br> `"0"` indicates that the train always operates and always stops at this station. <br> `"1"` indicates that the train does not always operate or sometimes skips this station; e.g. the train might skip this stop during rush hours in the peak direction or the train is/is not serviced during evenings, late nights, and weekends. <br> `"2"` indicates that the train stops at this station late night hours only. This is primarily found on express lines at local stops. <br> `"3"` indicates that the train operates in one direction only during rush hours. | `"0"`          |
| `stopStatus`   | The stop status, used for checking whether platform(s) are closed at a stop. <br> So far, only values found are `""`, `"-1"`, `"-2"`, `"-3"`. <br> `""` indicates that the stop is serviced normally. <br> `"-1"` indicates that the stop is closed. <br> `"-2"` indicates that the southbound platform is closed for the time being. <br> `"-3"` indicates that the northbound platform is closed for the time being. | `""`           |
| `borough`      | The borough. Self-explanatory.                                                                                                                                                                                                        | `"Bronx"`      |
| `stopName`     | The stop name. Self-explanatory.                                                                                                                                                                                                      | `"Woodlawn"`   |
| `ada`          | Whether this stop supports accessibility in accordance with the [ADA](https://en.wikipedia.org/wiki/Americans_with_Disabilities_Act_of_1990). <br> `"0"` means there is no accessibility support, `"1"` means there is full accessibility support, and `"2"` means there is partial accessibility support. | `"0"`          |

| Subway Line     | Route ID | Link                                                                                                                |
|-----------------|-----------|---------------------------------------------------------------------------------------------------------------------|
| ![1](https://new.mta.info/themes/custom/bootstrap_mta/js/apps/f615303877866360408d22d028c7e1d2.svg)  | MTASBWY:1 | [Link](https://collector-otp-prod.camsys-apps.com/schedule/MTASBWY/stopsForRoute?apikey=qeqy84JE7hUKfaI0Lxm2Ttcm6ZA0bYrP&&routeId=MTASBWY:1) |
| ![2](https://new.mta.info/themes/custom/bootstrap_mta/js/apps/12b76417962028dc5dd46a5f7da4e257.svg)  | MTASBWY:2 | [Link](https://collector-otp-prod.camsys-apps.com/schedule/MTASBWY/stopsForRoute?apikey=qeqy84JE7hUKfaI0Lxm2Ttcm6ZA0bYrP&&routeId=MTASBWY:2) |
| ![3](https://new.mta.info/themes/custom/bootstrap_mta/js/apps/a78ac9d7ebbb00594f70070c3867e8d5.svg)  | MTASBWY:3 | [Link](https://collector-otp-prod.camsys-apps.com/schedule/MTASBWY/stopsForRoute?apikey=qeqy84JE7hUKfaI0Lxm2Ttcm6ZA0bYrP&&routeId=MTASBWY:3) |
| ![4](https://new.mta.info/themes/custom/bootstrap_mta/js/apps/085719a34ab709a927f368bf0e764777.svg)  | MTASBWY:4 | [Link](https://collector-otp-prod.camsys-apps.com/schedule/MTASBWY/stopsForRoute?apikey=qeqy84JE7hUKfaI0Lxm2Ttcm6ZA0bYrP&&routeId=MTASBWY:4) |
| ![5](https://new.mta.info/themes/custom/bootstrap_mta/js/apps/b370f0e0c62c4b8f36b928178df6b4ae.svg)  | MTASBWY:5 | [Link](https://collector-otp-prod.camsys-apps.com/schedule/MTASBWY/stopsForRoute?apikey=qeqy84JE7hUKfaI0Lxm2Ttcm6ZA0bYrP&&routeId=MTASBWY:5) |
| ![6](https://new.mta.info/themes/custom/bootstrap_mta/js/apps/af9ae1b0bcfd30bc6c3626dae98074ef.svg)  | MTASBWY:6 | [Link](https://collector-otp-prod.camsys-apps.com/schedule/MTASBWY/stopsForRoute?apikey=qeqy84JE7hUKfaI0Lxm2Ttcm6ZA0bYrP&&routeId=MTASBWY:6) |
| ![7](https://new.mta.info/themes/custom/bootstrap_mta/js/apps/903c05438d54ff7a5d0036a769f10bf6.svg)  | MTASBWY:7 | [Link](https://collector-otp-prod.camsys-apps.com/schedule/MTASBWY/stopsForRoute?apikey=qeqy84JE7hUKfaI0Lxm2Ttcm6ZA0bYrP&&routeId=MTASBWY:7) |
| ![A](https://new.mta.info/themes/custom/bootstrap_mta/js/apps/9041d815e07d7dd93ebaa6bd466b6b67.svg)  | MTASBWY:A | [Link](https://collector-otp-prod.camsys-apps.com/schedule/MTASBWY/stopsForRoute?apikey=qeqy84JE7hUKfaI0Lxm2Ttcm6ZA0bYrP&&routeId=MTASBWY:A) |
| ![C](https://new.mta.info/themes/custom/bootstrap_mta/js/apps/ec805c7415caff62cc2641469574683c.svg)  | MTASBWY:C | [Link](https://collector-otp-prod.camsys-apps.com/schedule/MTASBWY/stopsForRoute?apikey=qeqy84JE7hUKfaI0Lxm2Ttcm6ZA0bYrP&&routeId=MTASBWY:C) |
| ![E](https://new.mta.info/themes/custom/bootstrap_mta/js/apps/5500549a75e2a20cfc18d6f87babfe40.svg)  | MTASBWY:E | [Link](https://collector-otp-prod.camsys-apps.com/schedule/MTASBWY/stopsForRoute?apikey=qeqy84JE7hUKfaI0Lxm2Ttcm6ZA0bYrP&&routeId=MTASBWY:E) |
| ![B](https://new.mta.info/themes/custom/bootstrap_mta/js/apps/9156f755686e8e6b2935f07a393b611a.svg)  | MTASBWY:B | [Link](https://collector-otp-prod.camsys-apps.com/schedule/MTASBWY/stopsForRoute?apikey=qeqy84JE7hUKfaI0Lxm2Ttcm6ZA0bYrP&&routeId=MTASBWY:B) |
| ![D](https://new.mta.info/themes/custom/bootstrap_mta/js/apps/84bc409ef98ce69f9d36e9b2556ab7cf.svg)  | MTASBWY:D | [Link](https://collector-otp-prod.camsys-apps.com/schedule/MTASBWY/stopsForRoute?apikey=qeqy84JE7hUKfaI0Lxm2Ttcm6ZA0bYrP&&routeId=MTASBWY:D) |
| ![F](https://new.mta.info/themes/custom/bootstrap_mta/js/apps/5b35921d073d41d80deeb17cac90d7fd.svg)  | MTASBWY:F | [Link](https://collector-otp-prod.camsys-apps.com/schedule/MTASBWY/stopsForRoute?apikey=qeqy84JE7hUKfaI0Lxm2Ttcm6ZA0bYrP&&routeId=MTASBWY:F) |
| ![M](https://new.mta.info/themes/custom/bootstrap_mta/js/apps/0e9163c71c7f9397f7d3e36d51546849.svg)  | MTASBWY:M | [Link](https://collector-otp-prod.camsys-apps.com/schedule/MTASBWY/stopsForRoute?apikey=qeqy84JE7hUKfaI0Lxm2Ttcm6ZA0bYrP&&routeId=MTASBWY:M) |
| ![G](https://new.mta.info/themes/custom/bootstrap_mta/js/apps/8f8f3abaabc85122841fe5df41fbc344.svg)  | MTASBWY:G | [Link](https://collector-otp-prod.camsys-apps.com/schedule/MTASBWY/stopsForRoute?apikey=qeqy84JE7hUKfaI0Lxm2Ttcm6ZA0bYrP&&routeId=MTASBWY:G) |
| ![J](https://new.mta.info/themes/custom/bootstrap_mta/js/apps/bca69e5237ed3e7d0d78320261f99f2d.svg)  | MTASBWY:J | [Link](https://collector-otp-prod.camsys-apps.com/schedule/MTASBWY/stopsForRoute?apikey=qeqy84JE7hUKfaI0Lxm2Ttcm6ZA0bYrP&&routeId=MTASBWY:J) |
| ![Z](https://new.mta.info/themes/custom/bootstrap_mta/js/apps/3f0bb849f47ead835e0241104f337a6d.svg)  | MTASBWY:Z | [Link](https://collector-otp-prod.camsys-apps.com/schedule/MTASBWY/stopsForRoute?apikey=qeqy84JE7hUKfaI0Lxm2Ttcm6ZA0bYrP&&routeId=MTASBWY:Z) |
| ![L](https://new.mta.info/themes/custom/bootstrap_mta/js/apps/8c1bfa6816b539fd63ca8f26e4dc8b65.svg)  | MTASBWY:L | [Link](https://collector-otp-prod.camsys-apps.com/schedule/MTASBWY/stopsForRoute?apikey=qeqy84JE7hUKfaI0Lxm2Ttcm6ZA0bYrP&&routeId=MTASBWY:L) |
| ![N](https://new.mta.info/themes/custom/bootstrap_mta/js/apps/4a1b0077917e37bf08502f6ec21b04c8.svg)  | MTASBWY:N | [Link](https://collector-otp-prod.camsys-apps.com/schedule/MTASBWY/stopsForRoute?apikey=qeqy84JE7hUKfaI0Lxm2Ttcm6ZA0bYrP&&routeId=MTASBWY:N) |
| ![Q](https://new.mta.info/themes/custom/bootstrap_mta/js/apps/b746451c38ae7d57f8a4d0b72b369328.svg)  | MTASBWY:Q | [Link](https://collector-otp-prod.camsys-apps.com/schedule/MTASBWY/stopsForRoute?apikey=qeqy84JE7hUKfaI0Lxm2Ttcm6ZA0bYrP&&routeId=MTASBWY:Q) |
| ![R](https://new.mta.info/themes/custom/bootstrap_mta/js/apps/9c6333dc2424c01e4740f5c3c56d362f.svg)  | MTASBWY:R | [Link](https://collector-otp-prod.camsys-apps.com/schedule/MTASBWY/stopsForRoute?apikey=qeqy84JE7hUKfaI0Lxm2Ttcm6ZA0bYrP&&routeId=MTASBWY:R) |
| ![W](https://new.mta.info/themes/custom/bootstrap_mta/js/apps/566ed247e9487d43c1f1cc7e8ea5f456.svg)  | MTASBWY:W | [Link](https://collector-otp-prod.camsys-apps.com/schedule/MTASBWY/stopsForRoute?apikey=qeqy84JE7hUKfaI0Lxm2Ttcm6ZA0bYrP&&routeId=MTASBWY:W) |
| ![S](https://new.mta.info/themes/custom/bootstrap_mta/js/apps/da91e0c35571668af52eb6164a71f33e.svg)  | MTASBWY:GS | [Link](https://collector-otp-prod.camsys-apps.com/schedule/MTASBWY/stopsForRoute?apikey=qeqy84JE7hUKfaI0Lxm2Ttcm6ZA0bYrP&&routeId=MTASBWY:GS) |
| ![SR](https://new.mta.info/themes/custom/bootstrap_mta/js/apps/ee2e30facb9a6c4b8bf0c43e531a36ab.svg)  | MTASBWY:H | [Link](https://collector-otp-prod.camsys-apps.com/schedule/MTASBWY/stopsForRoute?apikey=qeqy84JE7hUKfaI0Lxm2Ttcm6ZA0bYrP&&routeId=MTASBWY:H) |
| ![SF](https://new.mta.info/themes/custom/bootstrap_mta/js/apps/c01e0840361272a0585e94a540d6755f.svg)  | MTASBWY:FS | [Link](https://collector-otp-prod.camsys-apps.com/schedule/MTASBWY/stopsForRoute?apikey=qeqy84JE7hUKfaI0Lxm2Ttcm6ZA0bYrP&&routeId=MTASBWY:FS) |
| ![SIR](https://new.mta.info/themes/custom/bootstrap_mta/js/apps/ab18baf2d2d8ea7f1902ce1751d5fdf2.svg)  | MTASBWY:SI | [Link](https://collector-otp-prod.camsys-apps.com/schedule/MTASBWY/stopsForRoute?apikey=qeqy84JE7hUKfaI0Lxm2Ttcm6ZA0bYrP&&routeId=MTASBWY:SI) |

## Stops
To get information about a specific stop, you have to call a GET request to this API:
```
https://otp-mta-prod.camsys-apps.com/otp/routers/default/nearby?stops={stop}&apikey=Z276E3rCeTzOQEoBPPN4JCEc6GfvdnYE
```
where `stop` is the stop ID that you want to look up.

In [urls.json](./urls.json), there is a list of stop IDS for each route ID.

Note that you have to sanitize your parameters before calling the API. For example, the stop Id `MTASBWY:101` would be sanitized into `MTASBWY%3A101` and the URL would be `https://otp-mta-prod.camsys-apps.com/otp/routers/default/nearby?stops=MTASBWY%3A101&apikey=Z276E3rCeTzOQEoBPPN4JCEc6GfvdnYE`.

Calling this endpoint will return a array of dictionaries as a response in this format:
```json
[
    {
        "stop": stopFields,
        "alerts": [
            alertsFields...
        ],
        "groups": [
            groupsFields...
        ]
    }
]
```

The `alerts` and `groups` fields are arrays that contain dictionaries with fields that are noted in [`alertsFields`](#alertsfields) and [`groupsFields`](#groupsfields), respectively.

Note: The fields that return text, primarily `"alertDescriptionText"`, may contain special characters, such as `"\n"` for new lines. 

### **IMPORTANT**
For some reason, this specific endpoint is extremely inconsistent. Some fields may not show up, and all of the documented fields may very easily be `null` values. I have documented most fields that I could find, but there could be more fields that only show up at a certain time period, at certain stops, etc. Just be sure to handle these issues accordingly. 

### stopFields
| Field            | Explanation                                                     | Example                |
|------------------|-----------------------------------------------------------------|------------------------|
| `id`             | The stop ID.                                                    | `"MTASBWY:101"`        |
| `name`           | The name of the stop.                                           | `"Van Cortlandt Park-242 St"` |
| `lat`            | The latitude coordinates.                                       | `40.889246`            |
| `lon`            | The longitude coordinates.                                      | `-73.898584`           |
| `parentStation`  | The ID of the parent station.                                   | `"101"`                |

### alertsFields
The alerts fields sometimes contain extra fields (see below).

**These fields will always show up:**
| Field                        | Explanation                                                                                                                         | Example                                                                                                                                                                 |
|------------------------------|-------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `alertHeaderText`            | The alert header.                                                                                                                   | `"Subways are running on a Sunday Schedule"`                                                                                                                            |
| `createdAtDate`              | The timestamp for when the alert was created, in milliseconds.                                                                      | `1722959658000`                                                                                                                                                         |
| `updatedAtDate`              | The timestamp for when the alert was updated, in milliseconds.                                                                      | `1722970811000`                                                                                                                                                         |
| `alertDescriptionText`       | The alert description. Can be an empty string.                                                                                      | `"Use nearby Rector St [1] or Chambers St accessibility icon | [1][2][3].\n\nConsider nearby Cortlandt St accessibility icon | [N][R], World Trade Center accessibility icon | [E] or Fulton St accessibility icon | [2][3][4][A][C][J].\n\nWhat's happening?\n9/11 Memorial Ceremony"` |
| `effectiveStartDate`         | The timestamp of the effective start date.                                                                                          | `1726029900000`                                                                                                                                                         |
| `effectiveEndDate`           | The timestamp of the effective end date.                                                                                            | `1725335959000`                                                                                                                                                         |
| `displayBeforeActiveMillis`  | Not exactly clear what this is. Returns an integer resembling milliseconds for something. Can be 0.                                  | `0`                                                                                                                                                                     |
| `alertType`                  | The alert type.                                                                                                                     | `"Sunday Schedule"`                                                                                                                                                     |
| `humanReadableActivePeriod`  | A human-readable datetime of the alert active period.                                                                               | `"Sep 2, Monday, Labor Day"`                                                                                                                                             |
| `id`                         | The ID of the alert.                                                                                                                | `"lmm:planned_work:19031"`                                                                                                                                              |

**These fields might show up:**
| Field                  | Explanation                                                                                                   | Example                                                                                                                                                                      |
|------------------------|---------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `servicePlanNumbers`    | An array of service plans.                                                                                     | `[ "A-37-07" ]`                                                                                                                                                              |
| `generalOrderNumbers`   | An array of general orders.                                                                                    | `[ "1675-24" ]`                                                                                                                                                              |
| `stationAlternates`     | Contains an array of dictionaries with string fields: `"notes"`, `"agencyId"`, and `"stopId"`.                | ```[{"notes": "accessibility icon \| [7][G] and Manhattan-bound [E]\nshuttle bus icon Jackson Ave at Thomson Ave", "agencyId": "MTASBWY", "stopId": "F09"}, {"notes": "accessibility icon \| Manhattan-bound [E]\nshuttle bus icon Jackson Ave at Queens Blvd", "agencyId": "MTASBWY", "stopId": "G21"}, {"notes": "accessibility icon \| [F] and Jamaica Center-bound [E]\nshuttle bus icon 21 St at 41 Ave", "agencyId": "MTASBWY", "stopId": "B04"}]``` |
| `alertUrl`              | The alert URL. I have not found an instance of this having a value.                                            | `null`                                                                                                                                                                       |

If you want to view the example for `stationAlternates` you can copy and paste it into a JSON viewer like [this one](https://jsonformatter.org/json-pretty-print)

There might be other fields, but these are the ones that I found that sometimes show up. Just be wary when you handle the response.

Note: These extra fields can still show up, but have a `null` value, so be sure to handle that.

### groupsFields
Each of these group fields are for a different route. This accounts for stops that multiple trains stop at, such as Time Squares, and also accounts for trains going in different directions (uptown and downtown).

These group fields will be a dictionary formatted like this:
```json
{
    "route": routeFields,
    "times": [
        timesFields...
    ]
}
```

#### routeFields
| Field                     | Explanation                                                                        | Example                           |
|---------------------------|------------------------------------------------------------------------------------|-----------------------------------|
| `"id"`                    | The route ID.                                                                      | `"MTASBWY:1"`                     |
| `"shortName"`             | The short name of the route.                                                       | `"1"`                             |
| `"longName"`              | The long name of the route.                                                        | `"Broadway - 7 Avenue Local"`     |
| `"mode"`                  | The mode of transportation.                                                        | `"SUBWAY"`                        |
| `"color"`                 | The color of the route, in base 16 / hex format.                                   | `"EE352E"`                        |
| `"agencyName"`            | The name of the agency operating the route.                                        | `"MTA New York City Transit"`     |
| `"paramId"`               | The param ID used internally by the system.                                        | `"MTASBWY__1"`                    |
| `"sortOrder"`             | The order in which the route appears, often used for sorting purposes.             | `1`                               |
| `"routeType"`             | The type of the route.                                                             | `1`                               |
| `"regionalFareCardAccepted"` | Whether the route accepts MetroCards. Returns a boolean value.                 | `true`                            |

#### timesFields
| Field                        | Explanation                                                                                                                  | Example                                         |
|------------------------------|------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------|
| `"stopId"`                   | The stop ID.                                                                                                                 | `"MTASBWY:101N"`                                |
| `"stopName"`                 | The stop name.                                                                                                               | `"Van Cortlandt Park-242 St"`                   |
| `"stopLat"`                  | The latitude of the stop.                                                                                                    | `40.889246`                                     |
| `"stopLon"`                  | The longitude of the stop.                                                                                                   | `-73.898584`                                    |
| `"stopIndex"`                | The stop index.                                                                                                              | `37`                                            |
| `"stopCount"`                | The total number of stops on the route.                                                                                      | `38`                                            |
| `"scheduledArrival"`         | The scheduled time of arrival in seconds since midnight (00:00:00) on the same day.                                          | `81510`                                         |
| `"scheduledDeparture"`       | The scheduled time of departure in seconds since midnight (00:00:00) on the same day. Usually the same as `scheduledArrival`. | `81510`                                         |
| `"realtimeArrival"`          | The realtime time of arrival in seconds since midnight (00:00:00) on the same day.                                           | `81901`                                         |
| `"realtimeDeparture"`        | The realtime time of departure in seconds since midnight (00:00:00) on the same day. Usually the same as `realtimeArrival`.   | `81901`                                         |
| `"arrivalDelay"`             | The difference between `realtimeArrival` and `scheduledArrival`.                                                             | `391`                                           |
| `"departureDelay"`           | The difference between `realtimeDeparture` and `scheduledDeparture`.                                                         | `391`                                           |
| `"timepoint"`                | Assumed: Whether there is data on the arrival and departure times. Returns a boolean.                                         | `true`                                          |
| `"realtime"`                 | Assumed: Whether the data is being updated in realtime. Returns a boolean.                                                   | `true`                                          |
| `"realtimeState"`            | Assumed: The state of the realtime data. Only value found so far is `"UPDATED"`.                                              | `"UPDATED"`                                     |
| `"serviceDay"`               | The timestamp of the service day, in seconds. This timestamp only returns the date.                                           | `1724212800`                                    |
| `"tripId"`                   | The trip ID.                                                                                                                 | `"MTASBWY:899"`                                 |
| `"blockId"`                  | Unknown field.                                                                                                               | `null`                                          |
| `"tripHeadsign"`             | The trip head sign of the train.                                                                                             | `"Van Cortlandt Park-242 St"`                   |
| `"arrivalFmt"`               | The arrival time, formatted in datetime.                                                                                     | `"2024-08-21T23:01:31-04:00"`                   |
| `"departureFmt"`             | The departure time, formatted in datetime.                                                                                   | `"2024-08-21T23:01:31-04:00"`                   |
| `"stopHeadsign"`             | The stop head sign.                                                                                                          | `"242 St"`                                      |
| `"track"`                    | The track number.                                                                                                            | `"4"`                                           |
| `"peakOffpeak"`              | Unknown field. Returns an integer.                                                                                           | `0`                                             |
| `"pattern"`                  | Returns a dictionary with two fields, `"id"` and `"desc"`.                                                                   | `{ "id": "MTASBWY:1:0:01", "desc": "1 to Van Cortlandt Park-242 St (MTASBWY:101N)"}` |
| `"timestamp"`                | The current timestamp, in seconds.                                                                                           | `1724295503`                                    |
| `"directionId"`              | Indicates the direction of the train. `"0"` indicates uptown direction. `"1"` indicates downtown direction.                  | `"0"`                                           |
| `"vehicleInfo"`              | Assumed: The vehicle information. Have not found any values other than `null`.                                               | `null`                                          |
| `"stopsForTrip"`             | Assumed: The stops for the train's route. Have not found any values other than `null`.                                       | `null`                                          |
| `"realtimeSignText"`         | Unknown field.                                                                                                               | `""`                                            |
| `"regionalFareCardAccepted"` | Whether they accept MetroCards. Returns a boolean.                                                                           | `true`                                          |
