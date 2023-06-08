# kyber-lcb-8192

<img src="assets/snowflake_2744-fe0f_padding.gif" align="right" height="240" width="290"/>

![License](https://img.shields.io/github/license/NotReeceHarris/kyber-lcb)

**kyber-lcb-8192** is a hybrid encryption algorithm that implements the [Kyber](https://pq-crystals.org/kyber/) key encapsulation mechanism (KEM) and an 8192-bit matrix encryption algorithm.

Kyber security is based on the hardness of solving the learning-with-errors (LWE) problem over module lattices. Kyber is one of the candidate algorithms submitted to the [NIST post-quantum cryptography project](https://csrc.nist.gov/Projects/Post-Quantum-Cryptography).

## Security disclaimer
Please be aware that the encryption algorithm implemented in this repository should be considered experimental and not relied upon for secure communications or sensitive data protection. The algorithm was solely developed by an amateur enthusiast, needing more expertise and rigorous scrutiny typically associated with professional-grade cryptographic systems.

Furthermore, it is essential to note that the Kyber Key Encapsulation Mechanism (KEM) employed in this implementation has yet to be tested or utilized in conjunction with matrix encryption. This lack of prior usage may introduce unforeseen vulnerabilities, compromising the security and reliability of the encryption process.

**I cannot accept responsibility for any data breaches that may occur due to using this algorithm.**
