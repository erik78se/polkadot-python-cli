# polkacli - A Dwellir polkadot admin tool

polkacli communicates (rpc) with a local polkadot instance to make life easy when admin:ing 
a local polkadot node.

Use it to:

* Check node sync status
* Check node running version
* Get session keys
* Check if the node runs a validation role/mode.

  
    usage: polkacli [-h] {polkaversion,syncing,validating,sessionkey}

## About 

Dwellir is a polkadot staking operation and this software is used to help operating a polkadot validator node.

Stake your polkadot with us! https://dwellir.com

## Setup
The setup.py file includes some advanced patterns and best 
practices for setup.py, as well as some commented–out nice–to–haves. For example, it provides a `python 
setup.py upload` command, which creates a universal wheel (and sdist) and uploads your package to PyPi using Twine. 
It also creates/uploads a new git tag, automatically.

```
virtualenv env
source env/bin/activate
pip install -r requirements.txt
python -m polkacli --help
```

## Packaging 

    python -m build

## Contributing

- Fork the project and clone locally.
- Create a new branch for what you're going to work on.
- Push to your origin repository.
- Create a new pull request in GitHub.

## Attribution
* The cli is based on the work of https://github.com/AnthonyBloomer/python-cli-template
* Advanced python cli constructions inspired by: https://mike.depalatis.net
* Polkadot - The project