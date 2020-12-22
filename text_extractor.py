import html2text


class TextExtractor:
    """Get raw text from a HTML file and store it as text file."""

    def __init__(self, html_file_path):
        self.html_file_path = html_file_path

    def get_text(self, as_string=False):
        text_maker = html2text.HTML2Text()
        text_maker.ignore_links = True
        text_maker.escape_snob = True
        text_maker.links_each_paragraph = True
        text_maker.skip_internal_links = True
        text_maker.protect_links = True
        text_maker.ignore_anchors = True
        text_maker.single_line_break = True
        text_maker.unifiable = True
        text_maker.decode_errors = 'ignore'
        text_maker.ignore_images = True
        with open(self.html_file_path) as f:
            raw_text = f.read()
            text = text_maker.handle(raw_text)

        if as_string:
            return text
        else:
            with open("html_text.txt", mode='w') as f:
                f.write(text)
            return
