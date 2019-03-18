from JSONRequest.DatabaseDriver import Modules

modules = Modules()

def GetAuotorsByLangugageAndRequestForm(requestform):
    language_from = requestform['language_from']
    language_to = requestform['language_to']
    return modules.select_by_language(language_from, language_to)
