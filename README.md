# martha

![Github Actions Status](https://github.com/marthacryan/martha/workflows/Build/badge.svg)

A JupyterLab extension.


## Requirements

* JupyterLab >= 1.0

## Install
Lab extension
```bash
jupyter labextension install .
```
Server extension
```bash
pip install jupyterlab===2.2.8 jupyter_server
pip install -e .
jupyter serverextension enable martha
```

## Contributing

### Install

The `jlpm` command is JupyterLab's pinned version of
[yarn](https://yarnpkg.com/) that is installed with JupyterLab. You may use
`yarn` or `npm` in lieu of `jlpm` below.

```bash
# Clone the repo to your local environment
# Move to martha directory
# Install dependencies
jlpm
# Build Typescript source
jlpm build
# Link your development version of the extension with JupyterLab
jupyter labextension link .
# Rebuild Typescript source after making changes
jlpm build
# Rebuild JupyterLab after making any changes
jupyter lab build
```

You can watch the source directory and run JupyterLab in watch mode to watch for changes in the extension's source and automatically rebuild the extension and application.

```bash
# Watch the source directory in another terminal tab
jlpm watch
# Run jupyterlab in watch mode in one terminal tab
jupyter lab --watch
```

### Uninstall

```bash
jupyter labextension uninstall martha
```

