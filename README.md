# lipotes-vexillifer

## Introduction

    lipotes-vexillifer is 白鱀豚.[wiki](https://en.wikipedia.org/wiki/Baiji)

    This's my persional website.

## Setup

### local

install dependencies  
`npm install`

run serve  
`npm run serve`

### docker-compose

[docker-compose.yaml](docker-compose.yaml)

### auto update

``` shell
cp generator-cron /etc/cron.d/generator-cron
chmod 0644 /etc/cron.d/generator-cron
crontab /etc/cron.d/generator-cron
```

## File Tree

``` bash
public                             # public file folder
├── config                         # config file folder
│   └── footer.json                # footer config
├── favicon.ico                    # website favicon
├── generator.py                   # generate list.json
├── index.html
├── note                           # node file folder
│   ├── list.json
├── picture                        # picture file folder
│   └── list.json
└── WebGL-Fluid-Simulation.json
```

## Markdown head

``` yaml
---
title:
author:
date:
tag:
  - tag1
  - tag2
public:
cover:
summary:
---
```

> public
> * true: will show in article page
> * false: only show in note page
> * home: will show in home page
> * about: will show in about page

## TODO list

- [ ] home page
- [ ] fix toc bug
- [ ] modify colorscheme
- [ ] about page
- [ ] tag list
- [ ] picture page

## References

[vue](https://vuejs.org/index.html)
[vue-router](https://router.vuejs.org/)
[bootstrap](https://getbootstrap.com/)
[nginx](https://www.nginx.com/)
[WebGL-Fluid-Simulation](https://paveldogreat.github.io/WebGL-Fluid-Simulation/)

## License

[license](License)
