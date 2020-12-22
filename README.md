# Text-Extractor
Python script to extract text from a HTML file and export it as a text file. 

## Usage
To use this script you need to install [python](https://www.python.org/downloads/) on you machine if you do not already have it.
You need to install [html2text](https://pypi.org/project/html2text/) library as well. You can do that through pip. 
Just type the following command in your terminal:  
```
$ pip install html2text
```
### Example of usage:
```python
from text_extractor import TextExtractor

tx = TextExtractor(html_file_path)
tx.get_text()
```

### 
