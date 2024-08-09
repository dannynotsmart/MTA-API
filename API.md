# MTA API Documentation
My documentation of the MTA API. Currently only supports the subway lines (I'll get to the other services!)

## DISCLAIMER (Important)
This is **not** a documentation of their official developer API. Rather, this API documentation was made from reverse-engineering their website. That being said, I don't even know if I'm allowed to do this but **please don't sue me!**

## Table of Contents
1. [Logos](#logos)

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
