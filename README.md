For each line of the input file, your program should output the resulting height of the remaining blocks
within the grid.


For me https://chat.openai.com/share/3c3b6d22-51d9-4e77-bf16-4792830c56bf
# How to setup

## Active virtual environment
From the project's directory execute the following command


```
python3 -m venv venv
```

```
source venv/bin/activate
```

```
deactivate
```

## Install dependencies
```
pip install
```


```
python tetris.py < ../input.txt > ../output.txt
```

```
./tetris < input.txt > output.txt
```

```
pip freeze > requirements.txt
```

Run all tests
```
python -m unittest discover -s core/tests
```


Install all
```
pip install -r requirements.txt 
```

TODO
Remember to move things to config files or constants.
Formatting
Factory (dependecy injection Engine)
Block versus BlockType (que sea consistente el naming)
Deletions from the array, is that the best approach?
Change code so when I add a new piece it's only in one place
Consider  EMPTY_SPACE = "0" being number
Spaces vs cells vs blocks
Use BLACK to format code


If you only need to append rows to the top (or the left end of the deque) and not the bottom, then collections.deque remains an excellent choice due to its efficient O(1) appendleft() operation.

However, if you are seeking something simpler and don't want to deal with the overhead of an additional data structure, you can use a regular Python list. With a list, you can use the insert() method to add elements to the start, but keep in mind that this operation is O(n), where n is the length of the list. For a game like Tetris, this might not be noticeably inefficient unless you have a very large board or require frequent additions to the top.


https://codereview.stackexchange.com/questions/245876/determine-the-height-of-a-tetris-games-board-after-a-sequence-of-moves

```
black ./core
```