# Getting Started with PyInvoke

https://www.pyinvoke.org 

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

## c = Context object

It has many methods, for configurations, for example:
 - c.run(command)
 - c.sudo(command)
 - c.cd(path)
 - c.prefix(command)
 - c.config.run.echo
 - c.config.project_name

## c.run(command)

Executes shell commands:

```python
@task
def test(c):
    c.run("pytest tests/")
    c.run("flake8 .")
```

## c.sudo(command)

Runs commands with sudo privileges:
```python
@task
def install(c):
    c.sudo("apt-get install nginx")
```

## c.cd(path)
Changes directory (as a context manager):

```python
@task
def build(c):
    with c.cd('frontend'):
        c.run("npm run build")

## c.prefix(command)
Prefixes subsequent commands:

```python
@task
def venv_test(c):
    with c.prefix('source venv/bin/activate'):
        c.run("pip install -r requirements.txt")
        c.run("pytest")
```

## Configuration Properties
The Context object also holds configuration:
```python
@task
def info(c):
    print(c.config.run.echo)  # Access configuration
    print(c.config.project_name)  # Custom config values
```

## Common run() Options
```python
@task
def deploy(c):
    # Hide output
    c.run("git push", hide=True)
    
    # Don't raise exception on failure
    result = c.run("test -f file.txt", warn=True)
    
    # Capture output
    result = c.run("git rev-parse HEAD", hide=True)
    print(f"Current commit: {result.stdout.strip()}")
    
    # Run in pseudoterminal (for interactive commands)
    c.run("vim file.txt", pty=True)
```

## Return Values
c.run() returns a Result object with useful properties:
```python
@task
def check(c):
    result = c.run("echo 'Hello'", hide=True)
    print(result.stdout)      # "Hello\n"
    print(result.stderr)      # ""
    print(result.return_code) # 0
    print(result.ok)          # True (return_code == 0)
    print(result.failed)      # False
```

## Summary
The Context object (c) is your interface to:
- Execute commands (run, sudo)
- Control execution environment (cd, prefix)
- Access configuration (c.config)
- Handle command results (return values from run())

It's the glue that connects your Python task definitions to actual system commands!

Check the official docs for namespaces, configuration, and error handling!

https://www.pyinvoke.org 
