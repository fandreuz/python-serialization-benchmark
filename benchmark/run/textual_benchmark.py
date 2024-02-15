import random
import string

from benchmark.cases import Information, TextObject
from benchmark.run.base import pretty_print, run_backends


def generate_obj(size):
    abstract = "".join(random.choices(string.ascii_letters, k=size // 10))
    text = "".join(random.choices(string.ascii_letters, k=size))
    appendix = "".join(random.choices(string.ascii_letters, k=size // 4))

    info = Information(
        "Textual benchmark", "Data for textual benchmark", 0, "fandreuz@cern.ch"
    )
    return TextObject(information=info, abstract=abstract, text=text, appendix=appendix)


if __name__ == "__main__":
    pretty_print(run_backends(generate_obj))
