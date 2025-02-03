from ct001.encryption import PostQuantumCrypto

def test_key_generation():
    pqc = PostQuantumCrypto()
    assert pqc.get_public_key() is not None
    assert pqc.get_private_key() is not None
    print("✅ Encryption Test Passed!")

if __name__ == "__main__":
    test_key_generation()
