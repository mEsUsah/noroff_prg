class Package:
    spam = ''

    def __init__(self, content):
        Package.spam += content + ";"


envelope1 = Package("Caps")
envelope2 = Package("Trans")
print(envelope2.spam)