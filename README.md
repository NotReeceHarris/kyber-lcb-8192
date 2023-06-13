# lcb-9409

<!-- <img src="assets/snowflake_2744-fe0f_padding.gif" align="right" height="240" width="290"/> -->

![License](https://img.shields.io/github/license/NotReeceHarris/lcb-9409?style=flat-square)
![GitHub issues](https://img.shields.io/github/issues/NotReeceHarris/lcb-9409?style=flat-square)
![GitHub pull requests](https://img.shields.io/github/issues-pr/NotReeceHarris/lcb-9409?style=flat-square)

## Security disclaimer
Please be aware that the encryption algorithm implemented in this repository should be considered experimental and not relied upon for secure communications or sensitive data protection. The algorithm was solely developed by an amateur enthusiast, needing more expertise and rigorous scrutiny typically associated with professional-grade cryptographic systems.

**I cannot accept responsibility for any data breaches that may occur due to using this algorithm.**

## What is matrix encryption

Matrix encryption is a sophisticated cryptographic technique used to secure data by transforming it into an unintelligible form. It employs matrices, which are mathematical structures consisting of rows and columns, to encode information. The process begins by dividing the data into manageable blocks. Each block is then represented as a matrix, with the elements of the matrix corresponding to the numerical values of the data.

To encrypt the data, a specially designed matrix known as the encryption key is utilized. This encryption key matrix contains a predefined set of values that determine the encryption algorithm. The encryption process involves multiplying the data matrix by the encryption key matrix, using matrix multiplication rules. This operation scrambles the data by altering its numerical representation in a way that is computationally difficult to reverse-engineer without access to the encryption key.

To decrypt the encrypted data and retrieve the original information, the recipient must possess the decryption key, which is the inverse of the encryption key matrix. By multiplying the encrypted matrix with the decryption key matrix, the original data matrix is obtained, thereby recovering the plaintext. The encryption and decryption keys are carefully generated and kept confidential to ensure the security of the encoded information.


### Encryption

```math
KEY = \begin{bmatrix}
6 & 5 & 2 \\
4 & 4 & 5 \\
1 & 8 & 4
\end{bmatrix}

\\

CONTENT = \begin{bmatrix}
19 & 15 & 13 & 17 & 3\\
7 & 11 & 8 & 4 & 24\\
4 & 0 & 18 & 0 & 26
\end{bmatrix}
```

---

```math
\begin{bmatrix}
6 & 5 & 2 \\
4 & 4 & 5 \\
1 & 8 & 4
\end{bmatrix}
*
\begin{bmatrix}
19 & 15 & 13 & 17 & 3\\
7 & 11 & 8 & 4 & 24\\
4 & 0 & 18 & 0 & 26
\end{bmatrix}
=
\begin{bmatrix}
45 & 37 & 83 & 25 & 129\\
135 & 115 & 200 & 88 & 288\\
225 & 193 & 317 & 151 & 447
\end{bmatrix}
```


### Decryption

```math
inv\begin{bmatrix}
6 & 5 & 2 \\
4 & 4 & 5 \\
1 & 8 & 4
\end{bmatrix}
=
\begin{bmatrix}
0.167 & 0.027 & -0.118 \\
0.076 & -0.153 & 0.153 \\
-0.195 & 0.300 & -0.027
\end{bmatrix}
```

---

```math
\begin{bmatrix}
0.167 & 0.027 & -0.118 \\
0.076 & -0.153 & 0.153 \\
-0.195 & 0.300 & -0.027
\end{bmatrix}
*
\begin{bmatrix}
45 & 37 & 83 & 25 & 129\\
135 & 115 & 200 & 88 & 288\\
225 & 193 & 317 & 151 & 447
\end{bmatrix}
=
\begin{bmatrix}
19 & 15 & 13 & 17 & 3\\
7 & 11 & 8 & 4 & 24\\
4 & 0 & 18 & 0 & 26
\end{bmatrix}
```
