# A Bottery Extension - Context and flow management for your bots views
:battery: Bottery - a framework for building bots

[![Build Status](https://travis-ci.org/IvanBrasilico/bcontext.svg?branch=master)](https://travis-ci.org/IvanBrasilico/bcontext)


```python
# quick example of a input bot
On an Application:
app = App()
ch = ContextHandler(app)

On Patterns:
hang_user_pattern = HangUserPattern(example_view)
input.set_hang(hang_user_pattern, 'project')
patterns = [
    hang_user_pattern,
    Pattern('project', example_view),

On a View:
def notebook_view(message):
    words = shlex.split(message.text)
    command = words[0]
    params = None
    result = _(
        'Sorry. I cannot understand you. Type notebook for a list of options.')
    if len(words) > 1:
        params = words[1:]
    if command == 'notebook':
        ***ch.hang_in(message)***
        result = _('Welcome to notebooks Application! \n'
                   'Type "list" to view your notebooks \n'
                   'Type "add" "name" to add a notebook \n'
                   'Type "exit" to get out off application \n')
        if params:
            if params[0] in ['list', 'add']:
                command = params[0]
                if len(params) > 1:
                    params = params[1:]
                else:
                    params = []

    if command == 'list':
        notebooks = session.query(Notebook).all()
        result = [str(n.id) + ' - ' + n.name for n in notebooks]
        result = '\n'.join(result)
    elif command == 'add':
        if params:
            notebook = Notebook(params[0])
            result = _('Notebook ') + notebook.name + \
                _(' added!')
            session.add(notebook)
            session.commit()
        else:
            result = _('Error! Parameter "name" not entered.')
    elif command == 'exit':
        ***ch.hang_out(message)***
        result = _('Exiting...')

    return result

```

The complete example is packaged within this repository

* [Usage](#usage)
  * [Installing](#installing)
  * [Creating a project](#creating-a-project)


## Usage
Just import it on a bottery project. 
```python
# On bottery app
from botteryext.bcontext.contexthandler import ContextHandler
import botteryext.bcontext.localizations

app = App()
ch = ContextHandler(App)

# On patterns.py
from botteryext.bcontext.patterns import HangUserPattern
hang_user_pattern = HangUserPattern(aview)
ih.set_hang(hang_user_pattern, 'apattern')

patterns = [
    hang_user_pattern,
    Pattern('apattern', input_example),
***
# On views
from app import ch
```

### Installing
```bash
$ git clone https://github.com/IvanBrasilico/bcontext.git
$ cd bcontext
$ pip install -e . # optional, you can just put botteryext folder inside your project
```

### Creating a project 

Refer to [bottery](https://github.com/rougeth/bottery/) documentation


