from TestDataForFrontEnd import autors
def GetAllAuotorsByLanguage(language):
    autorsDict=autors.auotors
    language_autors=autorsDict[language]
    return language_autors
def GetAuotorsByLangugageAndRequestForm(requestform):
    language=requestform['language']
    language_autors=GetAllAuotorsByLanguage(language)
    return  language_autors
