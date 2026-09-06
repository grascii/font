# Developing

## Requirements

### FontForge

The current release of FontForge (2025-10-09) is sufficient for general
development. However, the build process of the font depends on newer FontForge
features introduced in this
[commit](https://github.com/fontforge/fontforge/commit/0bb1a2b28929059447d21869be8b098500798eb2).
Thus, building the font requires building FontForge from source or grabbing a
newer FontForge build from its Github Actions runs.

If using the FontForge AppImage, it is recommended to save it as
`FontForge.AppImage` in the root of the repository.

### Python

The minor version of Python used for development should match the version of
Python FontForge was built with. If using an official AppImage, that is Python
3.10. To check the Python version FontForge is using, run

```sh
$ fontforge --quiet -c "print(sys.version)"
```

### Inkscape

Inkscape is used for modeling glyphs. It is not required if not modeling.

### make

`make` is used to run scripts and perform various tasks.

## Getting Started

1. Clone the repository:
```sh
$ git clone https://github.com/grascii/font.git
$ cd font
```

2. Make sure the active python version is correct for your FontForge:
```sh
$ python --version
```

3. Create the python environment and install project dependencies:
```sh
$ make env
```

4. Install Grascii tools (optional, needed if editing/adding glyphs):
```sh
$ make install-tools
```

5. Open the Grascii project with FontForge:
```sh
$ make run
```

## Testing

Grascii contains a test suite that mostly tests substitution rules. To run the
tests:

```sh
$ make test
```

## Building

```sh
$ make build
```

The build process creates the `build/` directory and outputs the font in three
formats:

- `.otf`: Common format used to install the font on systems
- `.woff2`: Format optimized for web use
- `.sfd`: The built font in FontForge format, mostly for debugging purposes

## Modeling

For information on creating and editing glyphs, see [Modeling](./Modeling.md).

## OpenType Programming

Grascii uses OpenType Layout to draw Gregg Shorthand. Lookups are managed via
FontForge. See [Lookups](./Lookups.md) for details on Grascii's substitution
and positioning tables.
