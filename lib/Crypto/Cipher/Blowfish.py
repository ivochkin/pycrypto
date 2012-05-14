# -*- coding: utf-8 -*-
#
#  Cipher/Blowfish.py : Blowfish
#
# ===================================================================
# The contents of this file are dedicated to the public domain.  To
# the extent that dedication to the public domain is not available,
# everyone is granted a worldwide, perpetual, royalty-free,
# non-exclusive license to exercise all rights associated with the
# contents of this file for any purpose whatsoever.
# No rights are reserved.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
# EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
# MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
# NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS
# BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN
# ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
# CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
# ===================================================================
"""Blowfish symmetric cipher

Blowfish_ is a symmetric block cipher designed by Bruce Schneier.

It has a fixed data block size of 8 bytes and its keys can vary in length
from 32 to 448 bits (4 to 56 bytes).

Blowfish is deemed secure and it is fast. However, its keys should be chosen
to be big enough to withstand a brute force attack (e.g. at least 16 bytes).

.. _Blowfish: http://www.schneier.com/blowfish.html

:undocumented: __revision__, __package__
"""

__revision__ = "$Id$"

from Crypto.Cipher import blockalgo
from blockalgo import *
from Crypto.Cipher import _Blowfish

class BlowfishCipher (blockalgo.BlockAlgo):
    """Blowfish cipher object"""

    def __init__(self, key, *args, **kwargs):
        """Initialize a Blowfish cipher object
        
        See also `new()` at the module level."""
        blockalgo.BlockAlgo.__init__(self, _Blowfish, key, *args, **kwargs)

def new(key, *args, **kwargs):
    """Create a new Blowfish cipher

    :Parameters:
      key : byte string
        The secret key to use in the symmetric cipher.
        Its length can vary from 4 to 56 bytes.
    :Keywords:
      mode : a *MODE_** constant
        The chaining mode to use for encryption or decryption.
        Default is `MODE_ECB`.
      IV : byte string
        The initialization vector to use for encryption or decryption.
        It must be `block_size` bytes longs. Ignored for `MODE_ECB`
        and `MODE_CTR`. The default value is all zeroes.
      counter : callable
        (*Only* `MODE_CTR`). A stateful function that returns the next
        *counter block*, which is a byte string of `block_size` bytes.
        For better performance, use `Crypto.Util.Counter`.
      segment_size : integer
        (*Only* `MODE_CFB`).The number of bits the plaintext and ciphertext
        are segmented in.
        It must be a multiple of 8. If 0 or not specified, it will be assumed to be 8.

    :Return: a `BlowfishCipher` object
    """
    return BlowfishCipher(key, *args, **kwargs)

#: Electronic Code Book (ECB). See `blockalgo.MODE_ECB`.
MODE_ECB = 1
#: Cipher-Block Chaining (CBC). See `blockalgo.MODE_CBC`.
MODE_CBC = 2
#: Cipher FeedBack (CFB). See `blockalgo.MODE_CFB`.
MODE_CFB = 3
#: This mode should not be used.
MODE_PGP = 4
#: Output FeedBack (OFB). See `blockalgo.MODE_OFB`.
MODE_OFB = 5
#: CounTer Mode (CTR). See `blockalgo.MODE_CTR`.
MODE_CTR = 6
#: Size of a data block (in bytes)
block_size = 8
#: Size of a key (in bytes)
key_size = xrange(4,56)
