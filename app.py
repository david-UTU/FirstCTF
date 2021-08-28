from flask import Flask, render_template, request
import numpy as np
import matplotlib.pyplot as mpl

app = Flask(__name__)
app.config.from_object(__name__)


# PAGE LOADING FUNCTIONS


@app.route('/')  # Master home page
def welcome():
    return render_template('index.html')


@app.route('/Simple/simple/')  # Simple cipher tools home page
def simple():
    return render_template('/Simple/simple.html')


@app.route('/CommonTools/common/')  # Common tools home page
def common():
    return render_template('/CommonTools/common.html')


@app.route('/Submit/submit/')  # Simple cipher tools home page
def submit():
    return render_template('/Submit/submit.html')


@app.route('/CommonTools/charFreq/')  # Character frequency home page
def charFreq():
    return render_template('/CommonTools/charFreq.html')


@ app.route('/Simple/subCiphers/')  # Substitution ciphers home page
def subCiphers():
    return render_template('/Simple/subCiphers.html')


@ app.route('/Simple/caesar/')  # Caesar cipher page
def caesarCipher():
    return render_template('/Simple/caesar.html')


@app.route('/Simple/digraph/')  # Digraph ciphers page
def digraph():
    return render_template('/Simple/digraph.html')


@app.route('/CommonTools/binary/')  # Binary converter page load
def binary():
    return render_template('/CommonTools/binary.html')


@app.route('/CommonTools/base64/')  # Binary converter page load
def base64():
    return render_template('/CommonTools/base64.html')


@ app.route('/CommonTools/pStrength/')  # Password strength evaluator page
def pStrength():
    return render_template('/CommonTools/pStrength.html')


@app.route('/CommonTools/frequency/', methods=['POST'])
def frequency():
    textChunk = str(request.form.get('textChunk'))
    phrase = str(request.form.get('phrase'))
    letter_frequency = {}
    for i in textChunk:
        for x in i.upper():
            if x in letter_frequency and x != " " and x in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
                letter_frequency[x] += 1
            elif x in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
                letter_frequency[x] = 1
    result = str(sorted(letter_frequency.items(), key=lambda i: i[1]))
    result = result[1:-1]
    entry = f"Your character count totals: {result}"
    phraseCount = f"The phrase '{phrase}' appears {textChunk.count(phrase)} times"
    return render_template('/CommonTools/frequency.html', **locals())


@app.route('/CommonTools/binaryEncode.html', methods=['POST'])
def binaryEncode():
    originalNonBinary = str(request.form.get('binaryEncrypt')).lower()
    binaryMessage = ' '.join(format(ord(i), 'b') for i in originalNonBinary)
    return render_template('/CommonTools/binaryEncode.html', **locals())


@app.route('/CommonTools/binaryDecode.html', methods=['POST'])
def binaryDecode():
    originalBinary = str(request.form.get('binaryDecrypt'))
    binaryValues = originalBinary.split()
    binaryDecoded = ''
    for i in binaryValues:
        almostASCII = int(i, 2)
        letter = chr(almostASCII)
        binaryDecoded += letter
    return render_template('/CommonTools/binaryDecode.html', **locals())


@app.route('/Simple/digraphEncrypt/', methods=['POST'])
def digraphEncrypt():
    unencoded = str(request.form.get('digraphMessage')).lower()
    digraphEncoded = ''
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    sub1 = str(request.form.get('digraphSub1'))
    sub2 = str(request.form.get('digraphSub2'))
    count = 0
    for i in unencoded:
        if i in alphabet:
            count += 1
            if count % 2 == 1:
                index = alphabet.find(i)
                digraphEncoded += sub1[index]
            else:
                index = alphabet.find(i)
                digraphEncoded += sub2[index]
        else:
            digraphEncoded += i
    return render_template('/Simple/digraphEncrypt.html', **locals())


@app.route('/Simple/digraphDecrypt/', methods=['POST'])
def digraphDecrypt():
    digraphUnDecoded = str(request.form.get('digraphDeMessage')).lower()
    digraphDecodedMessage = ''
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    sub1 = str(request.form.get('digraphDeSub1'))
    sub2 = str(request.form.get('digraphDeSub2'))
    count = 0
    for i in digraphUnDecoded:
        if i in alphabet:
            count += 1
            if count % 2 == 1:
                index = sub1.find(i)
                digraphDecodedMessage += alphabet[index]
            else:
                index = sub2.find(i)
                digraphDecodedMessage += alphabet[index]
        else:
            digraphDecodedMessage += i
    return render_template('/Simple/digraphDecrypt.html', **locals())


@ app.route('/CommonTools/strength/', methods=['POST'])
def strength():
    password = str(request.form.get('passChunk'))
    A = int(request.form.get('A'))
    N = len(password)
    T = (A**N)  # total possibilities
    D = T/((10**9)*3600)  # Bruteforce time in years
    X = 2*np.log2(D)
    if X > 0:
        possible = (f"\nTotal possibilities: {T}")
        years = f"Years to Guess: {D}"
        brute = f"Bruteforce hours: {X}"
    else:
        possible = (f"\nTotal possibilities: {T}")
        years = f"Years to Guess: {D}"
        brute = "You may want to change that password..."
    return render_template('/CommonTools/strength.html', **locals())


@ app.route('/Simple/encode/', methods=['POST'])
def encode():
    text = str(request.form.get('encryptChunk')).lower()
    subCiph = str(request.form.get('subciphChunk')).lower().strip()
    alph = 'abcdefghijklmnopqrstuvwxyz'
    encrypted = ''
    for i in text:
        if i in alph:
            index = alph.find(i)
            encrypted += subCiph[index]
        else:
            encrypted += i
    return render_template('/Simple/encode.html', **locals())


@ app.route('/Simple/decode/', methods=['POST'])
def decode():
    text = str(request.form.get('decryptChunk')).lower()
    subCiph = str(request.form.get('subChunk')).lower().strip()
    alph = 'abcdefghijklmnopqrstuvwxyz'
    decrypted = ''
    for i in text:
        if i in alph:
            index = subCiph.find(i)
            decrypted += alph[index]
        else:
            decrypted += i
    return render_template('/Simple/decode.html', **locals())


@ app.route('/Simple/caesarEncryption/', methods=['POST'])
def caesarEncryption():
    unEncryptedCaesar = (request.form.get('unEncryptedCaesar'))
    encryptionShift = int(request.form.get('encryptionShift'))
    unEncryptedCaesar = unEncryptedCaesar.lower()
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    postEncryption = ""
    newAlphabet = (alphabet[encryptionShift:])+alphabet[:encryptionShift]
    for i in unEncryptedCaesar:
        if i in alphabet:
            postEncryption += newAlphabet[alphabet.index(i)]
        else:
            postEncryption += i
    return render_template('/Simple/caesarEncryption.html', **locals())


@ app.route('/Simple/caesarDecryption/', methods=['POST'])
def caesarDecryption():
    encryptedCaesar = (request.form.get('encryptedCaesar'))
    decryptionShift = int(request.form.get('decryptionShift'))
    encryptedCaesar = encryptedCaesar.lower()
    postDecryption = ''
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    newAlphabet = (alphabet[decryptionShift:])+alphabet[:decryptionShift]
    for i in encryptedCaesar:
        if i in alphabet:
            postDecryption += alphabet[newAlphabet.index(i)]
        else:
            postDecryption += i
    return render_template('/Simple/caesarDecryption.html', **locals())


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")
