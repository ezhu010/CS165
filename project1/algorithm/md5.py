# team13:$1$hfT7jp2q$0RPgvB3kOEwELDU03lY/k0:16653:0:99999:7:::(eelxru)
# team13:$1$4fTgjp6q$cDHwA2gMX6mKVmYQELy4A1:16653:0:99999:7:::  (??????) brute force a -> zzzzzz

import base64
import hashlib
import binascii
import math
import string


class MD5Decreption:
    def iterate(self, password, salt, intermediateSum):

        # TODO: iterate 1000 times
        for i in range(1000):
            temp = b""
            if i % 2 == 0:  # even
                temp += intermediateSum
            else:  # odd
                temp += password
            if not (i % 3 == 0):
                temp += salt

            if not (i % 7 == 0):
                temp += password

            if i % 2 == 0:
                temp += password
            else:
                temp += intermediateSum

            intermediateSum = hashlib.md5(temp).digest()
        return intermediateSum

    def calc_crpytBase64(self, intermediateSum1000):
        base64 = "./0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
        temp = b""

        ordering = [11, 4, 10, 5, 3, 9, 15, 2, 8, 14, 1, 7, 13, 0, 6, 12]
        # print(intermediateSum1000)
        for i in ordering:
            temp += intermediateSum1000[i : i + 1]

        # print(int(binascii.hexlify(temp), 16))
        temp = int(binascii.hexlify(temp), 16)
        hashedPassword = ""
        for i in range(22):
            hashedPassword += base64[temp % 64]
            temp //= 64

        return hashedPassword

    def computeHash(self, password, salt, magic):
        intermediateSum1 = self.calc_intermediateSum(password, salt, magic)

        intermediateSum1000 = self.iterate(
            password, salt, binascii.unhexlify(intermediateSum1)
        )

        intermediateSumBase64 = self.calc_crpytBase64(intermediateSum1000)

        finalHashedPassword = magic + salt + b"$" + intermediateSumBase64.encode()

        return finalHashedPassword

    # print(intermediateSumBase64)

    def calc_alternateSum(self, password, salt):
        alternate_sum = hashlib.md5(password + salt + password).hexdigest()
        return alternate_sum

    def calc_intermediateSum(self, password, salt, magic):
        intermediatSum1 = password + magic + salt
        alternateSum = self.calc_alternateSum(password, salt)
        passwordLength = len(password)
        # TODO: concatenate the first n characters of the alternateSum to the intermediate step,  n = password length
        temp = binascii.unhexlify(alternateSum)[0:passwordLength]
        intermediatSum1 += temp

        # TODO: check binary version of the password length and if bit = 1, append NUL byte else append first byte of the input password. Goes from least sig to highest sig

        while passwordLength > 0:
            if passwordLength & 1:
                # append null byte
                nullBtye = "\x00"
                intermediatSum1 += nullBtye.encode()

            else:
                # append first character of input password
                intermediatSum1 += password[0:1]
            passwordLength >>= 1

        return hashlib.md5(intermediatSum1).hexdigest()


if __name__ == "__main__":
    res = []
    ltrs = string.ascii_lowercase

    res += [
        "".join([a, b, c, d, e])
        for a in ltrs
        for b in ltrs
        for c in ltrs
        for d in ltrs
        for e in ltrs
    ]  # aaaaa -> zzzzz
    salt = "hfT7jp2q"
    magic = "$1$"
    matchingHashPassword = b"$1$hfT7jp2q$0RPgvB3kOEwELDU03lY/k0"
    mdAlgorithm = MD5Decreption()
    for x in res:
        if (
            mdAlgorithm.computeHash(x.encode(), salt.encode(), magic.encode())
            == matchingHashPassword
        ):
            print(x)

