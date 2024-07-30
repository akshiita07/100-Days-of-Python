This project implements a basic Caesar Cipher, a classic encryption technique where each letter in the plaintext is shifted a certain number of places down or up the alphabet. The provided code includes functionalities for both encoding and decoding messages.

Key features:
1. **Alphabet Array**: The alphabet is represented twice in the array to handle wrap-around shifts.
2. **Caesar Function**: 
   - Accepts `start_text`, `shift_amount`, and `cipher_direction` (either "encode" or "decode").
   - Adjusts `shift_amount` to negative if decoding.
   - Iterates through each character in the `start_text`, finds its position in the alphabet, calculates the new position based on the shift amount, and constructs the `end_text`.
   - Prints the final encoded or decoded result.

3. **Handling Special Characters** (TODO-3):
   - The code should be adjusted to handle numbers, symbols, and spaces without altering them during the encoding/decoding process.

4. **Shift Modulus Calculation** (TODO-2):
   - The program needs a modification to handle shift amounts greater than 26 (the number of letters in the alphabet). This can be achieved using the modulus operator.

5. **Logo Import** (TODO-1):
   - Imports and prints a logo from an external `art.py` file when the program starts.

6. **User Inputs**:
   - Asks the user to input the direction (encode/decode), the message, and the shift amount.

This project offers a practical example of string manipulation and basic cryptography, making it a useful exercise for beginners in programming.
