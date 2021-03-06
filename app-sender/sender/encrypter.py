from cryptography.fernet import Fernet
import logging
import os


class Encrypter:
    """
    This is an Encryption handler.
    It will load a symmetric key for each object and allow encryption based on the loaded key.
    """
    def __init__(self, path_to_key):
        """
        Constructor for Encrypter object
        :param path_to_key: Provide the path to the symmetric key
        """
        self.__encryption_keypath = path_to_key
        self.__load_encryption_key()
        self.__fernet_obj = Fernet(self.__encryption_key)

    def __load_encryption_key(self):
        """
        Loads symmetric key from provided path to the Encrypter object.
        :return: None
        """
        if os.path.isfile(self.__encryption_keypath):
            key = open(self.__encryption_keypath, "r")
            self.__encryption_key = str.encode(key.read().rstrip('\n'))
        else:
            logging.error("Encryption key is not available in {}.".format(self.__encryption_keypath))
            self.__encryption_key = Fernet.generate_key()
            logging.error("Autogenerated key {} will be used.".format(self.__encryption_key))

    def encrypt_file(self, file_to_encrypt, output_file):
        """
        Encrypts a given file using the loaded key.
        :param file_to_encrypt: File to encrypt.
        :param output_file: Path to encrypted file.
        :return: None
        """
        with open(file_to_encrypt, "rb") as fileobj:
            file_data = fileobj.read()
        encrypted_data = self.__fernet_obj.encrypt(file_data)
        with open(output_file, "wb") as fileobj:
            fileobj.write(encrypted_data)

