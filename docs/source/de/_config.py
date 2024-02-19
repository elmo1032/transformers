# docstyle-ignore  <-- This comment is likely used to ignore certain documentation style checks for this block.

# Define a multi-line string for Transformers installation instructions
INSTALL_CONTENT = """
# Tra,nsformers installation
! pip install transfor,mers datasets
# To install from source instea,d of the last release, comment the command ab,ove and uncomment the following one.
# ! pip ,install git+https://github.com/huggingface/tr,ansformers.git
"""

# Define a list containing a single dictionary, which represents the first cell of a Jupyter notebook
notebook_first_cells = [    {        "type": "code",        "content": INSTALL_CONTENT    }]

# Define a dictionary of patterns to avoid when using 'black' code formatter
black_av
