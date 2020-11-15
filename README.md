# Typer Boilerplate

A boilerplate making use of [typer](https://github.com/tiangolo/typer) + [pytest](https://github.com/pytest-dev/pytest) + docker.
This repository has been made for my students and my future-self, maybe for some people passing by too, who knows.

# Requirements

Docker.

Windows users: sorry, you wont be able to use the tiny shell scripts, please check the note at the end.
They don't do much in the present repository, this is a personal habit to have `run.sh` and `runtests.sh` at the root of my repositories.

# Usage

## Running

```bash
./run.sh
```

Or, as arguments are passed around :

```bash
./run.sh hello awesome
```

## Testing

```bash
./runtests.sh
```
Or, as arguments are passed around, you can pass your prefered pytest flags.

```bash
./runtests.sh --pdb
```

## Debugging

In case you want to enter your container environment :

```bash
docker build . -t mycli
docker run -it --entrypoint bash mycli
```

## Notes

Dont forget to : 
- change informations in the `setup.py`
- replace "mycli" all over the place with the name of your package.

Windows user, everything is inside the shell scripts, copy and paste will work.
Two notes : 
- ignore the clear command
- delete the `$@` symbol
