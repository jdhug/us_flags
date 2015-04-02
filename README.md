# US FLAGS 


###### *Single page app to convert US Flags from svg to png or jpg.*
---
But really this a python app to evaluate hosted Continuous Integration:

* [Bottle](http://bottlepy.org/docs/dev/index.html).
* [CircleCI](https://circleci.com/), [Codeship](https://codeship.com/) and [TravisCI](https://travis-ci.com/) with some tests.
* Automated [Heroku](https://www.heroku.com/) deployment.
* [Bootstrap](http://getbootstrap.com/) and [modal dialog](http://getbootstrap.com/javascript/#modals).
* [JQuery Resizable](https://jqueryui.com/resizable/).
* [Wand] (http://docs.wand-py.org/en/0.4.0/).

---

###### Continuous Integration:
|               | **[CircleCI](https://circleci.com/)**       | **[Codeship](https://codeship.com/)**       | **[TravisCI](https://travis-ci.com/)**       |
| ------------  |:--------------:| :-------------:|:--------------:|
| **Master**  | ![alt tag](https://circleci.com/gh/wigglyworld/us_flags/tree/master.svg) | ![alt tag](https://codeship.com/projects/126f5060-b176-0132-d033-3edef27c5b65/status?branch=master) | ![alt tag](https://travis-ci.org/wigglyworld/us_flags.svg?branch=master) |
| **Develop** | ![alt tag](https://circleci.com/gh/wigglyworld/us_flags/tree/develop.svg ) | ![alt tag](https://codeship.com/projects/126f5060-b176-0132-d033-3edef27c5b65/status?branch=develop) | ![alt tag](https://travis-ci.org/wigglyworld/us_flags.svg?branch=develop) |
| **Config**        | [circleci.yml](https://github.com/wigglyworld/us_flags/blob/master/circleci.yml) | [Procfile](https://github.com/wigglyworld/us_flags/blob/master/Procfile) | [.travis.yml](https://github.com/wigglyworld/us_flags/blob/master/.travis.yml) |
| **Delivery**     | TBD | [Flags](http://calm-plateau-1307.herokuapp.com/) | TBD |
| **Free Level<sup>*</sup>**    | Unlimited public repos | Unlimited public repos | Unlimited public repos |
|                | 1 concurrent build     | 1 concurrent build     | 1 concurrent build     |
| Private repos  | Unlimited              | 5 private repos | Unlimited but... |
| Private builds | Unlimited             | 100 private builds/mo | First 100 private builds |
| Artifacts      | [Yes](http://circleci.com/docs/build-artifacts) | [Upload to S3](https://codeship.com/documentation/continuous-integration/keep-build-artifacts/) | [Upload to S3](http://docs.travis-ci.com/user/uploading-artifacts/) |
| Selenium Firefox | Yes | Yes | Working on it | 

<sup>*</sup> It may have changed...


