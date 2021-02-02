# %%
from requests import put, get

# %%
put('http://localhost:5000/todo1', data={'data': 'Remember the milk'}).json()
{u'todo1': u'Remember the milk'}

# %%
get('http://localhost:5000/todo1').json()
{u'todo1': u'Remember the milk'}

# %%
put('http://localhost:5000/todo2', data={'data': 'Change my brakepads'}).json()
{u'todo2': u'Change my brakepads'}

# %%
get('http://localhost:5000/todo2').json()
{u'todo2': u'Change my brakepads'}
