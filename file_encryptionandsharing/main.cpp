// File: main.cpp

#include <iostream>
#include <fstream>
#include "encryption.h"
#include "network.h"

int main() {
    std::string inputFile = "data.txt";
    std::string encryptedFile = "data_encrypted.txt";
    std::string decryptedFile = "data_decrypted.txt";
    
    std::string key = generateKey();
    
    // Encrypt the file
    if (encryptFile(inputFile, encryptedFile, key)) {
        std::cout << "File successfully encrypted.\n";
    } else {
        std::cerr << "Encryption failed.\n";
        return 1;
    }
    
    // Decrypt the file
    if (decryptFile(encryptedFile, decryptedFile, key)) {
        std::cout << "File successfully decrypted.\n";
    } else {
        std::cerr << "Decryption failed.\n";
        return 1;
    }
    
    // Simulate file transfer over the network
    if (transferFile(encryptedFile)) {
        std::cout << "File successfully transferred over the network.\n";
    } else {
        std::cerr << "File transfer failed.\n";
        return 1;
    }
    
    return 0;
}
