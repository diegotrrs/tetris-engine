
# 1. How to install

From the root folder:

## 1.1 Create virtual environment

```
python3 -m venv venv
```

## 1.2 Activate virtual environment
```
source venv/bin/activate
```

## 1.3 Install dependencies

```
pip install -r requirements.txt 
```

# 2. How to run

# 2.1 Execute the main program
From the root folder

Python script
```
python3 ./tetris_engine.py < input.txt > output.txt
```

Bash
```
./tetris < input.txt > output.txt
```

# 2.2 Execute Sample_test.py

```
python3 sample_test.py 
```

# 2.3 Execute Unit tests (not the one provided by Encord)

```
python -m unittest discover -s core/tests
```

