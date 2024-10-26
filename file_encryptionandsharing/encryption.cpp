// File: encryption.cpp

#include "encryption.h"
#include <fstream>
#include <openssl/aes.h>
#include <openssl/rand.h>

std::string generateKey() {
    unsigned char key[AES_BLOCK_SIZE];
    RAND_bytes(key, AES_BLOCK_SIZE);
    return std::string(reinterpret_cast<const char*>(key), AES_BLOCK_SIZE);
}

bool encryptFile(const std::string& inputFile, const std::string& outputFile, const std::string& key) {
    std::ifstream in(inputFile, std::ios::binary);
    std::ofstream out(outputFile, std::ios::binary);
    if (!in.is_open() || !out.is_open()) {
        return false;
    }

    AES_KEY encryptKey;
    AES_set_encrypt_key(reinterpret_cast<const unsigned char*>(key.c_str()), 128, &encryptKey);

    unsigned char inbuf[AES_BLOCK_SIZE];
    unsigned char outbuf[AES_BLOCK_SIZE];

    while (in.read(reinterpret_cast<char*>(inbuf), AES_BLOCK_SIZE)) {
        AES_encrypt(inbuf, outbuf, &encryptKey);
        out.write(reinterpret_cast<char*>(outbuf), AES_BLOCK_SIZE);
    }

    return true;
}

bool decryptFile(const std::string& inputFile, const std::string& outputFile, const std::string& key) {
    std::ifstream in(inputFile, std::ios::binary);
    std::ofstream out(outputFile, std::ios::binary);
    if (!in.is_open() || !out.is_open()) {
        return false;
    }

    AES_KEY decryptKey;
    AES_set_decrypt_key(reinterpret_cast<const unsigned char*>(key.c_str()), 128, &decryptKey);

    unsigned char inbuf[AES_BLOCK_SIZE];
    unsigned char outbuf[AES_BLOCK_SIZE];

    while (in.read(reinterpret_cast<char*>(inbuf), AES_BLOCK_SIZE)) {
        AES_decrypt(inbuf, outbuf, &decryptKey);
        out.write(reinterpret_cast<char*>(outbuf), AES_BLOCK_SIZE);
    }

    return true;
}