import time
import alphabet

BLANK_SIGN = [
    '• • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • •',
    '• • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • •',
    '• • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • •',
    '• • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • •',
    '• • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • • •'
]

SIGN_LENGTH = len(BLANK_SIGN[0])
SIGN_HEIGHT = len(BLANK_SIGN)

def printSign(sign):
    """Print sign to terminal."""
    for row in sign:
        print(row)

def generateBackspace(i, msg_length):
    """Determine the string that should follow the message across the screen,
    which we'll call the 'backspace'."""

    backspace = ""

    if i % 2 == 0:
        start = '•'
    else:
        start = ' '

    if SIGN_LENGTH - i > msg_length:
        backspace_length = SIGN_LENGTH - (i + msg_length)
        last = start
        while backspace_length > 0:
            backspace += last
            if last == '•':
                last = ' '
            else:
                last = '•'
            backspace_length -= 1
    return backspace

def generateExitBackspace(i):
    """Determine the backspace string when the msg is exiting the board."""

    backspace = ""

    if i % 2 == 0:
        start = '•'
    else:
        start = ' '

    backspace_length = SIGN_LENGTH - i
    last = start
    while backspace_length > 0:
            backspace += last
            if last == '•':
                last = ' '
            else:
                last = '•'
            backspace_length -= 1
    return backspace


def createMessage(msg):

    chars = [alphabet.alphabet[c] for c in msg]

    # msg is now a 5 x 5*len(msg) array
    # [ [] [] [] [] [] ]
    msg = []
    msg_row = ""
    
    for i in range(SIGN_HEIGHT):
        for j, char in enumerate(chars):
            msg_row += "".join(char[i])
            if j < len(chars) - 1:
                msg_row += " "
        msg.append(msg_row)
        msg_row = ""
    
    return msg



def main():
    """Scroll message across sign."""
    sign = BLANK_SIGN
    printSign(sign)
    msg = input('Type a message to display: ')
    # all characters translated and appended into 5 x len(msg) array
    msg = createMessage(msg)
    msg_length = len(msg[0])

    i = len(sign[0])
    while i >= 0:
        for r, row in enumerate(msg):
            backspace = generateBackspace(i, msg_length)
            sign[r] = sign[r][:i+1] + row[:SIGN_LENGTH - i] + backspace
        printSign(sign)
        time.sleep(.05)
        i-=1

    i = msg_length
    while i >= 0:
        for r, row in enumerate(msg):
            backspace = generateExitBackspace(i)
            sign[r] = row[msg_length-i:SIGN_LENGTH + (msg_length-i)] + backspace
        printSign(sign)
        time.sleep(.05)
        i-=1


    print()

main()