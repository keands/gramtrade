import logging
import re
from typing import Optional

from gramTradeConstants import buy_pattern, short_pattern, buy_limit_pattern, sell_limit_pattern, regex_decimal, \
    major_pairs, minor_pairs

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

logger = logging.getLogger(__name__)


def clean_values(value: str) -> str:
    """Remove whitespaces and comma from str

       Args:
           value (str): decimal value with whitespaces and comma

       Returns:
           str: the value without whitespaces and a dot
       """

    return value.replace(" ", "").replace(",", ".")


def find_pair(message: str) -> Optional[str]:
    """Retrieve pair defined in first parameters and returned it

    Args:
        message (str): line or message

    Returns:
        str: The return pair founded or None.
    """

    pair_list = major_pairs + minor_pairs
    for pair in pair_list:
        if pair in message:
            return pair
    return None


def retrieve_position(sl: str, tps: list[str]) -> str:
    """Check with tp and sl if the position is a buy or sell

           Args:
               sl (str): stop loss
               tps (list[str]) : list of tps

           Returns:
               str: position type
           """
    if float(sl) > float(tps[0]):
        order = "SELL"
    elif float(sl) < float(tps[0]):
        order = "BUY"
    return order


def find_values(line: str) -> Optional[str]:
    """Retrieve decimal value from regex

               Args:
                   line (str): a line of message with values

               Returns:
                   str: value ready to use as float
               """
    raw_value = re.findall(regex_decimal, line)
    if len(raw_value) >= 1:
        return clean_values(raw_value[0])
    else:
        return None


def order_type(message: str) -> Optional[str]:
    """Retrieve position type

           Args:
               message (str): str containing the position type

           Returns:
               str: position
           """

    if re.search(buy_limit_pattern, message, re.IGNORECASE):
        return "BUY LIMIT"
    elif re.search(sell_limit_pattern, message, re.IGNORECASE):
        return "SELL LIMIT"
    elif re.search(buy_pattern, message, re.IGNORECASE):
        return "BUY"
    elif re.search(short_pattern, message, re.IGNORECASE):
        return "SELL"
    else:
        logger.debug("No order type in {}".format(message))
        return None
