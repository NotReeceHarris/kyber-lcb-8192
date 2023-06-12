# kyber-lcb-8281

<img src="assets/snowflake_2744-fe0f_padding.gif" align="right" height="240" width="290"/>

![License](https://img.shields.io/github/license/NotReeceHarris/kyber-lcb)

**kyber-lcb-8281** is a hybrid encryption algorithm that implements the [Kyber](https://pq-crystals.org/kyber/) key encapsulation mechanism (KEM) and an 8281-bit matrix encryption algorithm.

Kyber security is based on the hardness of solving the learning-with-errors (LWE) problem over module lattices. Kyber is one of the candidate algorithms submitted to the [NIST post-quantum cryptography project](https://csrc.nist.gov/Projects/Post-Quantum-Cryptography).

## Security disclaimer
Please be aware that the encryption algorithm implemented in this repository should be considered experimental and not relied upon for secure communications or sensitive data protection. The algorithm was solely developed by an amateur enthusiast, needing more expertise and rigorous scrutiny typically associated with professional-grade cryptographic systems.

Furthermore, it is essential to note that the Kyber Key Encapsulation Mechanism (KEM) employed in this implementation has yet to be tested or utilized in conjunction with matrix encryption. This lack of prior usage may introduce unforeseen vulnerabilities, compromising the security and reliability of the encryption process.

**I cannot accept responsibility for any data breaches that may occur due to using this algorithm.**

## What is matrix encryption

THE PLAN IS READY

a | b | c | d | e | f | g | h | i | j | k | l | m | n | o | p | q | r | s | t | u | v | w | x | y | z
--- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | ---
0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 21 | 22 | 23 | 24 | 25


```math

KEY = \begin{bmatrix}
1 & 2 & 3 \\
4 & 5 & 6 \\
7 & 8 & 9
\end{bmatrix}
.
\begin{bmatrix}
19 & 15 & 13 & 17 & 3\\
7 & 11 & 8 & 4 & 24\\
4 & 0 & 18 & 0 & 26
\end{bmatrix}

```

now in comparason the key size here is 3x3 or 9 bits, kyber-lcb-8281 is a 8281 bit encryption algorithm meaning the key size will be 91x91 
