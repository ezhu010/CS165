# team13:$1$hfT7jp2q$0RPgvB3kOEwELDU03lY/k0:16653:0:99999:7:::(eelxru)
import base64
import hashlib
import binascii


class MD5Ddecreption:
    password = ""
    salt = ""

    def calc_alternateSum(self, password, salt):
        alternate_sum = hashlib.md5(password + salt + password).hexdigest()
        return alternate_sum

    def calc_intermediateSum(self, password, salt, magic):
        intermediatSum1 = password + magic + salt
        alternateSum = self.calc_alternateSum(password, salt)
        print(temp)
        # print(intermediatSum1)
        passwordLength = len(password)

        # concatenatedPass = intermediatSum1 +


if __name__ == "__main__":

    mdAlgorithm = MD5Ddecreption()
    password = "zhgnnd"
    salt = "hfT7jp2q"
    magic = "$1$"
    # print(mdAlgorithm.calc_alternateSum(password.encode(), salt.encode()))
    mdAlgorithm.calc_intermediateSum(password.encode(), salt.encode(), magic.encode())

    # ?ü†çÇG¨Oâ…Àú"U

