from .bitcoin import BaseCoin
from ..explorers import sochain


class Doge(BaseCoin):
    coin_symbol = "DOGE"
    display_name = "Dogecoin"
    segwit_supported = False
    magicbyte = 30
    script_magicbyte = 22
    wif_prefix = 0x9e
    hd_path = 3
    explorer = sochain
    xpriv_prefix = 0x02facafd
    xpub_prefix = 0x02fac398
    testnet_overrides = {
        'display_name': "Dogecoin Testnet",
        'coin_symbol': "DOGETEST",
        'magicbyte': 113,
        'script_magicbyte': 196,
        'wif_prefix': 0xf1, #https://github.com/dogecoin/dogecoin/blob/master/src/chainparams.cpp#L157 => base58Prefixes[SECRET_KEY]
        'hd_path': 1,
        'xpriv_prefix': 0x04358394,
        'xpub_prefix': 0x043587cf
    }