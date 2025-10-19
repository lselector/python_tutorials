# Getting Started with PyInvoke

PyInvoke is a Python task execution tool that helps you define and run command-line tasks. Think of it as a Pythonic alternative to Makefiles.

## Installation

```bash
pip install invoke
```

## Basic Usage

### 1. Create a `tasks.py` file

```python
from invoke import task

@task
def hello(c):
    """Say hello"""
    print("Hello, World!")

@task
def build(c):
    """Build the project"""
    c.run("python setup.py build")

@task
def test(c):
    """Run tests"""
    c.run("pytest tests/")
```

### 2. Run tasks from the command line

```bash
# List available tasks
invoke --list

# Run a task
invoke hello
invoke build
invoke test
```

## Task Parameters

```python
@task
def greet(c, name="World"):
    """Greet someone by name"""
    print(f"Hello, {name}!")
```

```bash
invoke greet --name=Alice
invoke greet -n Bob
```

## Chaining Tasks

```python
@task
def clean(c):
    """Clean build artifacts"""
    c.run("rm -rf build/ dist/")

@task(pre=[clean])
def build(c):
    """Build after cleaning"""
    c.run("python setup.py build")
```

## Common Patterns

### Running shell commands
```python
@task
def deploy(c):
    c.run("git push origin main")
    c.run("ssh server 'sudo systemctl restart app'")
```

### Using task context
```python
@task
def serve(c, port=8000):
    """Start development server"""
    with c.cd('src'):
        c.run(f"python -m http.server {port}")
```

## Learn More

That's it! PyInvoke makes task automation simple and Pythonic. 

Check the [official docs](https://www.pyinvoke.org/) for more advanced features like namespaces, configuration, and error handling.

