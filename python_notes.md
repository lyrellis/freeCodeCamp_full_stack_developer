# Python Notes

## Basics

### Print Function

There's a lot more to the `print` function than first meets the eye. There are four other arguments you can pass to it, so here's the full syntax of the function.

```python
print(*objects sep=' ', end='\n', file=sys.stdout, flush=False)
```

> - `objects` : The data you want to print. The `*` sign means that yu can print multiple things to the terminal by passing in multiple objects.
> - `sep` : The seperator between the obsects. This defaults to a single space character.  
> - `end` : What to print at the end of the object. This defaults to a new line character.
> - `file` : Determines where to send the output. The default is in the terminal, but it can be a file.
> - `flush` : Determines whether to show the output data right away. The default is `False`, which means Python may wait before displaying the output.