def convhelper(theString, which):
    from bijoy2unicode import converter
    conv = converter.Unicode()
    if(not theString or len(theString) == 0):
        return ""
    elif which == "U":
        newString = conv.convertBijoyToUnicode(theString)
    elif which == "A":
        newString = conv.convertUnicodeToBijoy(theString)
    return newString


def convertion(which):
    import string

    xModel = XSCRIPTCONTEXT.getDocument()
    xSelectionSupplier = xModel.getCurrentController()
    xIndexAccess = xSelectionSupplier.getSelection()
    count = xIndexAccess.getCount()
    if(count >= 1):
        j = 0
    while j < count:
        xTextRange = xIndexAccess.getByIndex(j)
        theString = xTextRange.getString()
        if len(theString) == 0:
            xText = xTextRange.getText()
            xWordCursor = xText.createTextCursorByRange(xTextRange)
            if not xWordCursor.isStartOfWord():
                xWordCursor.gotoStartOfWord(False)
            xWordCursor.gotoNextWord(True)
            theString = xWordCursor.getString()
            newString = convhelper(theString, which)
            if newString:
                xWordCursor.setString(newString)
                xSelectionSupplier.select(xWordCursor)
        else:

            newString = convhelper(theString,which)
            if newString:
                xTextRange.setString(newString)
                xSelectionSupplier.select(xTextRange)
        j += 1


def ToUni():
    convertion("U")


def ToANSI():
    convertion("A")


g_exportedScripts = ToUni, ToANSI,
