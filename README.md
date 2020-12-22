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

### More options:

You can adjust the script to fit your needs by changing these parameters in ```get_text function``` as you see below: 

![Bildschirmfoto 2020-12-22 um 20 09 05](https://user-images.githubusercontent.com/8310720/102924557-1d27e580-4492-11eb-8cdf-5b34cdbce5bd.png)
