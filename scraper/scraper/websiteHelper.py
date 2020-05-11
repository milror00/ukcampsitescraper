import re


class websiteHelper():

    @classmethod
    def extractSiteNameFromString(self, input):
        sitenameRegex = ">(.+?)</span>"
        p = re.compile(sitenameRegex)
        result = p.search(input)
        if result is None:
            return ''
        else:
            siteName = result.group(1).strip()
            searchStr = 'Certi'
            if siteName.find(searchStr) < 0:
                return siteName
            else:
                end = siteName.find(searchStr)
                return siteName[0:end].strip()

    @classmethod
    def extractTelephoneFromString(self, input):
        telephoneRegex = 'Tel:(.+?)<br>'
        p = re.compile(telephoneRegex)
        result = p.search(input)
        if result is None:
            return ''
        else:
            telephone = result.group(1).strip()
            if len(telephone) == 12:
              return telephone
            else:
                return telephone[0:11]

    @classmethod
    def extractPostcodeFromString(self, input):
        postcodeRegex = '(?:[A-Za-z]\d ?\d[A-Za-z]{2})|(?:[A-Za-z][A-Za-z\d]\d ?\d[A-Za-z]{2})|(?:[A-Za-z]{2}\d{2} ?\d[A-Za-z]{2})|(?:[A-Za-z]\d[A-Za-z] ?\d[A-Za-z]{2})|(?:[A-Za-z]{2}\d[A-Za-z] ?\d[A-Za-z]{2})'
        p = re.compile(postcodeRegex)
        result = p.search(input)
        if result is None:
            return ''
        else:
            return result.group(0)


    @classmethod
    def splice(self, original, start, end):
        a = original.find(start)
        b = original.find(end)
        if (a == -1) or (b == -1):
            return ''
        else:
            a = a + len(start)
            return original[a:b]
