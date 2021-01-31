 
# %%
curl http://localhost:5000/todos {"todo1": {"task": "build an API"}, "todo3": {"task": "profit!"}, "todo2": {"task": "?????"}}


# %%
curl http://localhost:5000/todos/todo3 {"task": "profit!"}


curl http://localhost:5000/todos/todo2 -X DELETE -v


curl http://localhost:5000/todos -d "task=something new" -X POST -v


curl http://localhost:5000/todos/todo3 -d "task=something different" -X PUT -v