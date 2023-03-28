class KeyAccount:
    def __init__(self, file_path: str):
        lines = self.get_account_information(file_path)
        self.private_mnemonic = lines.pop().replace('Private key mnemonic: ', '').replace('\n', '')
        self.account_address = lines.pop().replace('Account address: ', '').replace('\n', '')

    def get_account_information(self, file_path):
        f = open(file_path, 'r')
        lines = f.readlines()
        lines.reverse()
        return lines


if __name__ == '__main__':
    a = KeyAccount('../llaves/account-a.secret')
    print(a.private_mnemonic)
    print(a.account_address)
