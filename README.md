# sphinx-seibootcamps

A Sphinx extension that includes all the things you want while supporting customizations.

## Installing for development

If you'll only be working on the Sphinx extension, you're only required to follow the instructions under [Install Python dependencies](#install-git-hooks), then skip ahead to [Install git hooks](#install-git-hooks). If you'll be doing SCSS development, you'll **need to follow all sets of instructions,** including [Install Node dependencies](#install-node-dependencies).

### Install Python dependencies

Environments managed by Poetry and virtualenv are supported, but using Poetry is strongly recommended.

Install dependencies using your favorite package manager.

```sh
poetry install

# or, with virtualenv
virtualenv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### Install Node dependencies

Using yarn or npm:

```sh
yarn install

# or
npm install
```

### Install git hooks

Then, install [pre-commit](https://pre-commit.com/) hooks.

```sh
poetry run pre-commit install

# or, after activing your virtual env
pre-commit install
```
