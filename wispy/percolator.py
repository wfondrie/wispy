"""
This module contains functions that are useful for interacting with
Percolator input and output files in Python.
"""
import tqdm
import pandas as pd

def read(txt_file: str) -> pd.DataFrame:
    """
    Read a Percolator tab-delimited file to a pandas DataFrame.

    This works for either the Percolator INput format (PIN) or the
    Percolator output files from the stand-alone version and crux.
    After import, all columns that can be converted to a numeric data
    type will be.

    Parameters
    ----------
    txt_file : str
        The Percolator tab-delimited file to read.

    Returns
    -------
    pandas.DataFrame
        A pandas DataFrame of the input file.
    """
    with open(txt_file, "r") as psms:
        header = psms.readline().replace("\n", "").split("\t")
        rows = [l.replace("\n", "").split("\t", len(header)-1) for l
                in tqdm.tqdm(psms, ascii=True, desc=txt_file, unit=" lines")]
        psms_df = pd.DataFrame(columns=header, data=rows)

        return psms_df.apply(pd.to_numeric, errors="ignore")


def write_pin(pin_df: pd.DataFrame, pin_file: str) -> str:
    """
    Write a pandas DataFrame to PIN format

    Writes a pandas DataFrame to Percolator INput (PIN) format. The
    columns of the DataFrame must contain the necessary Percolator
    columns for the file to work correctly.

    Parameters
    ----------
    pin_df : pandas.DataFrame
        The PSMs to write to a PIN file.
    pin_file : str
        The pin file to write.

    Returns
    -------
    str
        The pin file that was written.
    """
    with open(pin_file, "w") as pin_out:
        header = "\t".join(pin_df.columns.tolist()) + "\n"
        data = ((pin_df.astype(str) + "\t").sum(axis=1) + "\n").tolist()
        pin_out.writelines(tqdm.tqdm([header] + data, ascii=True,
                                     desc=pin_file, unit=" lines"))

    return pin_file
