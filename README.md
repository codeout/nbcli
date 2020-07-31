# NetBox Client

Extensible command-line interface for Netbox using pynetbox module. 

[![asciicast](https://asciinema.org/a/348204.svg)](https://asciinema.org/a/348204)

```
usage: nbcli [-h] <command> ...

Extensible CLI for Netbox

optional arguments:
  -h, --help  show this help message and exit

Commands:
  <command>
    init      Initialize nbcli.
    search    Search Netbox Objects
    show      Show detail view of Netbox Object
    shell     Launch interactive shell
    pynb      Wrapper for pynetbox

General Options:
  -h, --help           show this help message and exit
  -v, --verbose        Show more logging messages
  -q, --quiet          Show fewer logging messages
```

## Notable Features

- [Search](docs/nbsearch.md) Netbox instance from command line
- [Show](docs/show.md) detail view of objects
- [pynb](docs/pynb.md) Command line wrapper for pynetbox
- [Shell](docs/shell.md) with preloaded pynetbox endpoints
    - Run scripts in shell environment.
- [Customizable](docs/views.md) table/detail views
- [Extensible](docs/commands.md) by adding custom commands

## Quickstart

```
$ pip install nbcli
$ nbcli init
Edit pynetbox 'url' and 'token' entries in user_config.yml:
        ~/.nbcli/user_config.yml
```

At the very minimum, you need to specify a url and token in the user_config.yml file

```yaml
pynetbox:
  url: http://localhost:8080
  token: 0123456789abcdef0123456789abcdef01234567
```

If you need to disable SSL verification, add (or uncomment) the following to your user_config.yml file. 

```yaml
requests:
  verify: false
```

More configuration options can be found [here](docs/init.md).

## Testing

Instructions for setting up a test environment are [here](docs/test-env.md).
